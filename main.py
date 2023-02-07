import sys, os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from typing import Final
from src.ui_Ui_main import Ui_MainWindow
from Game import Player, Game
from util import ButtonStyles

VERSIONNUM: Final = "1.2"
BASE_DIR: Final = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.copyrightLabel.setText(f"Version {VERSIONNUM} | 2023 © S343o3")
        self.ui.stackedWidget.setCurrentWidget(self.ui.menuView)
        self.setWindowTitle("TicTacToe PySide6")
        self.Game: Game = Game()
        self.player_buttons = self.ui.gameField.children()
        self.setup_gamebuttons()
        self.gameover = False
        self.block_gamefield()
        self.round = 0

        self.AITimer = QTimer()
        self.AITimer.setSingleShot(True)
        self.AITimer.timeout.connect(lambda: self.ai_button_handler())
        def moveWindow(e):
            if self.isMaximized() == False: 
                if e.buttons() == Qt.LeftButton:
                    globalPos = e.globalPos() 
                    self.move(self.pos() + globalPos - self.clickPosition)
                    self.clickPosition = globalPos

        self.ui.label.mouseMoveEvent = moveWindow

    def setup_gamebuttons(self):
        self.ui.gridBtn_1.clicked.connect(lambda: self.player_button_handler(self.ui.gridBtn_1))
        self.ui.gridBtn_2.clicked.connect(lambda: self.player_button_handler(self.ui.gridBtn_2))
        self.ui.gridBtn_3.clicked.connect(lambda: self.player_button_handler(self.ui.gridBtn_3))
        self.ui.gridBtn_4.clicked.connect(lambda: self.player_button_handler(self.ui.gridBtn_4))
        self.ui.gridBtn_5.clicked.connect(lambda: self.player_button_handler(self.ui.gridBtn_5))
        self.ui.gridBtn_6.clicked.connect(lambda: self.player_button_handler(self.ui.gridBtn_6))
        self.ui.gridBtn_7.clicked.connect(lambda: self.player_button_handler(self.ui.gridBtn_7))
        self.ui.gridBtn_8.clicked.connect(lambda: self.player_button_handler(self.ui.gridBtn_8))
        self.ui.gridBtn_9.clicked.connect(lambda: self.player_button_handler(self.ui.gridBtn_9))

        self.ui.startBtn.clicked.connect(lambda: self.play_game())
        self.ui.resetBtn.clicked.connect(lambda: self.game_reset())
        self.ui.menuBtn.clicked.connect(lambda: self.switch_menu_view())
        self.ui.exitBtn.clicked.connect(lambda: self.close())

        self.ui.menuExitBtn.clicked.connect(lambda: self.close())
        self.ui.menuNewGameBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.newGameView))
        self.ui.startNewGameBtn.clicked.connect(lambda: self.setup_player())
        self.ui.startNewGameBackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.menuView))
        
        self.ui.newGameBtnFrame.setStyleSheet(ButtonStyles.MenuBtn)
        self.ui.menuBtnFrame.setStyleSheet(ButtonStyles.MenuBtn)

    def switch_menu_view(self):
        self.Game.game_over = True
        self.gameover = True
        self.ui.turnLabel.setText("")
        self.ui.gameStateLabel.setText("")
        self.reset_gamefield()
        self.block_gamefield()
        self.ui.stackedWidget.setCurrentWidget(self.ui.menuView)

    def game_reset(self):
        self.Game.reset_game()
        self.ui.turnLabel.setText(f"Its >>> {self.Game.turn.name} <<< turn!")
        self.ui.gameStateLabel.setText("Game started")
        self.reset_gamefield()
        self.gameover = False
        self.Game.start_game()

    def play_game(self):
        if self.gameover:
            return
        self.Game.start_game()
        self.ui.gameStateLabel.setText("Game started")
        self.ui.p1ScoreLabel.setText(str(self.Game.player1.score))
        self.ui.p2ScoreLabel.setText(str(self.Game.player2.score))
        self.ui.turnLabel.setText(f"Its >>> {self.Game.turn.name} <<< turn!")
        self.unlock_gamefield()

    def reset_gamefield(self):
        self.unlock_gamefield()
        self.ui.gridBtn_1.setText("?")
        self.ui.gridBtn_2.setText("?")
        self.ui.gridBtn_3.setText("?")
        self.ui.gridBtn_4.setText("?")
        self.ui.gridBtn_5.setText("?")
        self.ui.gridBtn_6.setText("?")
        self.ui.gridBtn_7.setText("?")
        self.ui.gridBtn_8.setText("?")
        self.ui.gridBtn_9.setText("?")
        self.ui.gridBtn_1.setStyleSheet(ButtonStyles.GameBtnNormal)
        self.ui.gridBtn_2.setStyleSheet(ButtonStyles.GameBtnNormal)
        self.ui.gridBtn_3.setStyleSheet(ButtonStyles.GameBtnNormal)
        self.ui.gridBtn_4.setStyleSheet(ButtonStyles.GameBtnNormal)
        self.ui.gridBtn_5.setStyleSheet(ButtonStyles.GameBtnNormal)
        self.ui.gridBtn_6.setStyleSheet(ButtonStyles.GameBtnNormal)
        self.ui.gridBtn_7.setStyleSheet(ButtonStyles.GameBtnNormal)
        self.ui.gridBtn_8.setStyleSheet(ButtonStyles.GameBtnNormal)
        self.ui.gridBtn_9.setStyleSheet(ButtonStyles.GameBtnNormal)

    def block_gamefield(self):
        self.ui.gridBtn_1.setDisabled(True)
        self.ui.gridBtn_2.setDisabled(True)
        self.ui.gridBtn_3.setDisabled(True)
        self.ui.gridBtn_4.setDisabled(True)
        self.ui.gridBtn_5.setDisabled(True)
        self.ui.gridBtn_6.setDisabled(True)
        self.ui.gridBtn_7.setDisabled(True)
        self.ui.gridBtn_8.setDisabled(True)
        self.ui.gridBtn_9.setDisabled(True)
    
    def unlock_gamefield(self):
        self.ui.gridBtn_1.setDisabled(False)
        self.ui.gridBtn_2.setDisabled(False)
        self.ui.gridBtn_3.setDisabled(False)
        self.ui.gridBtn_4.setDisabled(False)
        self.ui.gridBtn_5.setDisabled(False)
        self.ui.gridBtn_6.setDisabled(False)
        self.ui.gridBtn_7.setDisabled(False)
        self.ui.gridBtn_8.setDisabled(False)
        self.ui.gridBtn_9.setDisabled(False)

    def setup_player(self):
        p1Name = self.ui.p1NameInput.text()
        p2Name = self.ui.p2NameInput.text()
        p1Symbol = self.ui.p1IconBox.currentText()
        p2Symbol = self.ui.p2IconBox.currentText()
        if p1Name == p2Name == "":
            return
        
        if p1Symbol == p2Symbol:
            return

        player1 = Player(p1Name, p1Symbol)
        player2 = Player(p2Name, p2Symbol)

        if self.ui.vsComCheck.isChecked():
            player2.ai = True
            player2.name += " (AI)"
            print("AI is checked")

        self.Game.player1 = player1
        self.Game.player2 = player2

        self.ui.player1Label.setText(player1.name)
        self.ui.player2Label.setText(player2.name)
        self.ui.p1ScoreLabel.setText(str(player1.score))
        self.ui.p2ScoreLabel.setText(str(player2.score))

        print(self.Game.player1.name, self.Game.player2.name)
        self.ui.p1NameInput.setText("")
        self.ui.p2NameInput.setText("")
        self.reset_gamefield()
        self.block_gamefield()
        self.ui.turnLabel.setText("Please press Start!")
        self.ui.gameStateLabel.setText("Welcome!")
        self.gameover = False
        self.Game.reset_game()
        self.ui.stackedWidget.setCurrentWidget(self.ui.gameView)

    def player_button_handler(self, button:QPushButton):
        button.setText(self.Game.turn.symbol)
        if self.Game.turn.symbol == self.Game.player1.symbol:
            button.setEnabled(False)
            button.setStyleSheet("color: rgb(255, 0, 0);background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(13, 0, 0, 220), stop:0.994318 rgba(103, 0, 0, 220));")
        else:
            button.setStyleSheet("color: rgb(0, 85, 255);background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(13, 0, 0, 220), stop:0.994318 rgba(0, 0, 255, 220));")
        button.setDisabled(True)
        self.Game.move_player(button.objectName())

        if self.Game.winner == None and self.Game.game_over == True:        
            self.draw()
            return
        if self.Game.game_over:
            self.player_wins()
            return

        self.ui.turnLabel.setText(f"Its >>> {self.Game.turn.name} <<< turn!")
        if self.Game.turn == self.Game.player2 and self.Game.player2.ai:
            self.block_gamefield()
            self.AITimer.start(1500)
    
    def ai_button_handler(self):
        btn = self.findChild(QPushButton, "gridBtn_"+str(self.Game.ai_set_move()))
        btn.setDisabled(True)
        btn.setText(self.Game.player2.symbol)
        btn.setStyleSheet("color: rgb(0, 85, 255);background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(13, 0, 0, 220), stop:0.994318 rgba(0, 0, 255, 220));")
        print("AI Clicked btn: "+ btn.objectName())
        if self.Game.winner == None and self.Game.game_over == True:        
            self.draw()
            return
        if self.Game.game_over:
            self.player_wins()
            return
        self.unlock_gamefield()
        self.ui.turnLabel.setText(f"Its >>> {self.Game.turn.name} <<< turn!")

    def draw(self):
        self.gameover = True
        self.ui.gameStateLabel.setText("Game Over!")
        self.ui.turnLabel.setText(f"Sorry, its a draw!")
        self.block_gamefield()

    def player_wins(self):
        self.gameover = True
        self.ui.gameStateLabel.setText("Game Over!")
        self.ui.turnLabel.setText(f"Winner is {self.Game.winner.name}!")
        self.ui.p1ScoreLabel.setText(str(self.Game.player1.score))
        self.ui.p2ScoreLabel.setText(str(self.Game.player2.score))
        self.block_gamefield()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(BASE_DIR, 'appicon.ico')))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
