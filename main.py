import sys, os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from typing import Final
from src.ui_Ui_main import Ui_MainWindow
from Game import Player, TTTGame
from util import ButtonStyles
from tet import *

VERSIONNUM: Final = "2.1"
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

        self.tetBoard: TetrixBoard= TetrixBoard()
        layout = QGridLayout(self.ui.tetrisBoardWidget)
        layout.addWidget(self.tetBoard, 0, 1, 6, 1)
        self.tetBoard.set_next_piece_label(self.ui.nextTetLabel)
        self.tetBoard.game_over.connect(self.gameover_tetris)
        self.tetBoard.score_changed.connect(self.ui.tetScoreLCD.display)
        self.tetBoard.level_changed.connect(self.ui.tetLvlLCD.display)
        self.tetBoard.lines_removed_changed.connect(self.ui.tetLinesLCD.display)
        self.ui.tetrisBoardWidget.resize(225, 370)

        self.TTTGame: TTTGame = TTTGame()
        self.player_buttons = self.ui.gameField.children()
        self.setup_gamebuttons()
        self.gameover = False
        self.block_gamefield()
        # self.ui.p1NameInput.setText("Test 1")
        # self.ui.p2NameInput.setText("Test 2")
        self.round = 0
        self.winner_btn = []
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
        self.ui.resetBtn.clicked.connect(lambda: self.ttt_game_reset())
        self.ui.menuBtn.clicked.connect(lambda: self.switch_menu_view())
        self.ui.exitBtn.clicked.connect(lambda: self.close())

        self.ui.menuExitBtn.clicked.connect(lambda: self.close())
        self.ui.menuNewGameBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.newGameView))
        self.ui.menuTetBtn.clicked.connect(lambda: self.setup_tetris_view())
       
        self.ui.tetExitBtn.clicked.connect(lambda: self.close())
        self.ui.tetMenuBtn.clicked.connect(lambda: self.switch_menu_view())
        self.ui.tetStartBtn.clicked.connect(lambda: self.start_tetris())
        self.ui.tetPauseBtn.clicked.connect(lambda: self.pause_tetris())        

        self.ui.startNewGameBtn.clicked.connect(lambda: self.setup_player())
        self.ui.startNewGameBackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.menuView))
        
        self.ui.newGameBtnFrame.setStyleSheet(ButtonStyles.MenuBtn)
        self.ui.menuBtnFrame.setStyleSheet(ButtonStyles.MenuBtn)
        self.ui.tetBtnFrame.setStyleSheet(ButtonStyles.MenuBtn)
        self.ui.label_11.setStyleSheet(ButtonStyles.TetrisLabel)
        self.ui.label_12.setStyleSheet(ButtonStyles.TetrisLabel)
        self.ui.label_13.setStyleSheet(ButtonStyles.TetrisLabel)
        self.ui.tetLinesLCD.setStyleSheet(ButtonStyles.LCDTetris)
        self.ui.tetLvlLCD.setStyleSheet(ButtonStyles.LCDTetris)
        self.ui.tetScoreLCD.setStyleSheet(ButtonStyles.LCDTetris)

    ############ TETRIS ###############

    def setup_tetris_view(self):
        if self.tetBoard == None:
            self.tetBoard = TetrixBoard()
            layout = QGridLayout(self.ui.tetrisBoardWidget)
            layout.addWidget(self.tetBoard, 0, 1, 6, 1)
            self.tetBoard.set_next_piece_label(self.ui.nextTetLabel)
            self.tetBoard.game_over.connect(self.gameover_tetris)
            self.tetBoard.score_changed.connect(self.ui.tetScoreLCD.display)
            self.tetBoard.level_changed.connect(self.ui.tetLvlLCD.display)
            self.tetBoard.lines_removed_changed.connect(self.ui.tetLinesLCD.display)
            self.ui.tetrisBoardWidget.resize(225, 370)
        self.ui.tetStateLabel.setText("Press 'Start'!")
        self.ui.stackedWidget.setCurrentWidget(self.ui.tetView)

    def gameover_tetris(self):
        self.tetBoard.destroy()
        self.ui.tetrisBoardWidget.setLayout(None)
        self.ui.tetStateLabel.setText("Game Over!")
        self.ui.tetLinesLCD.display(0)
        self.ui.tetLvlLCD.display(0)
        self.ui.tetScoreLCD.display(0)

    def start_tetris(self):
        self.tetBoard.start()
        self.ui.tetStateLabel.setText("Game started!")
        random.seed(None)
        print("Tetris: Start Game")

    def pause_tetris(self):
        self.tetBoard.pause()
        if self.tetBoard._is_paused:   
            self.ui.tetPauseBtn.setText("Resume")
            self.ui.tetStateLabel.setText("Game paused!")
            print("Tetris: Pause Game")
        else:
            self.ui.tetPauseBtn.setText("Pause")
            self.ui.tetStateLabel.setText("Game started!")
            print("Tetris: Resume Game")


    ######### TIC TAC TOE ############
    def switch_menu_view(self):
        if self.TTTGame.game_over == False:
            self.TTTGame.game_over = True
            self.gameover = True
            self.ui.turnLabel.setText("")
            self.ui.gameStateLabel.setText("")
            self.reset_gamefield()
            self.block_gamefield()
        if self.tetBoard._is_started == True:
            self.tetBoard.end_game()
            self.gameover_tetris()
        self.ui.stackedWidget.setCurrentWidget(self.ui.menuView)

    def ttt_game_reset(self):
        self.TTTGame.reset_game()
        self.ui.turnLabel.setText(f"Its >>> {self.TTTGame.turn.name} <<< turn!")
        self.ui.gameStateLabel.setText("Game started")
        self.reset_gamefield()
        self.gameover = False
        self.TTTGame.round += 1
        self.ui.tttRoundLCD.display(self.TTTGame.round)
        self.TTTGame.start_game()

    def play_game(self):
        if self.gameover:
            return
        self.TTTGame.start_game()
        self.ui.gameStateLabel.setText("Game started")
        self.ui.p1ScoreLcd.display(self.TTTGame.player1.score)
        self.ui.p2ScoreLcd.display(self.TTTGame.player2.score)
        self.ui.turnLabel.setText(f"Its >>> {self.TTTGame.turn.name} <<< turn!")
        self.unlock_gamefield()

    def reset_gamefield(self):
        self.unlock_gamefield()
        self.remove_winner_effect()
        self.ui.gridBtn_1.setText("?")
        self.ui.gridBtn_2.setText("?")
        self.ui.gridBtn_3.setText("?")
        self.ui.gridBtn_4.setText("?")
        self.ui.gridBtn_5.setText("?")
        self.ui.gridBtn_6.setText("?")
        self.ui.gridBtn_7.setText("?")
        self.ui.gridBtn_8.setText("?")
        self.ui.gridBtn_9.setText("?")
        self.ui.gridBtn_1.setMinimumSize(QSize(75, 75))
        self.ui.gridBtn_2.setMinimumSize(QSize(75, 75))
        self.ui.gridBtn_3.setMinimumSize(QSize(75, 75))
        self.ui.gridBtn_4.setMinimumSize(QSize(75, 75))
        self.ui.gridBtn_5.setMinimumSize(QSize(75, 75))
        self.ui.gridBtn_6.setMinimumSize(QSize(75, 75))
        self.ui.gridBtn_7.setMinimumSize(QSize(75, 75))
        self.ui.gridBtn_8.setMinimumSize(QSize(75, 75))
        self.ui.gridBtn_9.setMinimumSize(QSize(75, 75))
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

        self.TTTGame.player1 = player1
        self.TTTGame.player2 = player2
        self.TTTGame.round = 1
        self.ui.tttRoundLCD.display(self.TTTGame.round)

        self.ui.player1Label.setText(player1.name)
        self.ui.player2Label.setText(player2.name)

        print(self.TTTGame.player1.name, self.TTTGame.player2.name)
        self.ui.p1NameInput.setText("")
        self.ui.p2NameInput.setText("")
        self.reset_gamefield()
        self.block_gamefield()
        self.ui.turnLabel.setText("Please press Start!")
        self.ui.gameStateLabel.setText("Welcome!")
        self.gameover = False
        self.TTTGame.reset_game()
        self.ui.stackedWidget.setCurrentWidget(self.ui.gameView)

    def player_button_handler(self, button:QPushButton):
        button.setText(self.TTTGame.turn.symbol)
        animation = QPropertyAnimation(button, b"minimumSize", self.ui.stackedWidget)
        animation.finished.connect(button.setDisabled(True))
        animation.setDuration(300)
        animation.setStartValue(QSize(75,75))
        animation.setEndValue(QSize(85,85))
        animation.start()
        if self.TTTGame.turn.symbol == self.TTTGame.player1.symbol:
            button.setStyleSheet("border: 2px solid rgb(255, 0, 0); border-radius: 42px;font-size:58px; color: rgb(255, 0, 0);background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(13, 0, 0, 220), stop:0.994318 rgba(103, 0, 0, 220));")
        else:
            button.setStyleSheet("border: 2px solid rgb(0, 85, 255);border-radius: 42px;font-size:58px; color: rgb(0, 85, 255);background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(13, 0, 0, 220), stop:0.994318 rgba(0, 0, 255, 220));")

        self.TTTGame.move_player(button.objectName())

        if self.TTTGame.winner == None and self.TTTGame.game_over == True:        
            self.draw()
            return
        if self.TTTGame.game_over:
            self.player_wins()
            return

        self.ui.turnLabel.setText(f"Its >>> {self.TTTGame.turn.name} <<< turn!")
        if self.TTTGame.turn == self.TTTGame.player2 and self.TTTGame.player2.ai:
            self.block_gamefield()
            self.AITimer.start(1200)

    def ai_button_handler(self):
        btn = self.findChild(QPushButton, "gridBtn_"+str(self.TTTGame.ai_set_move()))
        btn.setText(self.TTTGame.player2.symbol)
        animation = QPropertyAnimation(btn, b"minimumSize", self.ui.centralwidget)
        animation.finished.connect(btn.setDisabled(True))
        animation.setDuration(180)
        animation.setStartValue(QSize(65,65))
        animation.setEndValue(QSize(85,85))
        animation.start()
        btn.setStyleSheet("border: 2px solid rgb(0, 85, 255);border-radius: 42px;font-size:58px; color: rgb(0, 85, 255);background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(13, 0, 0, 220), stop:0.994318 rgba(0, 0, 255, 220));")
        print("AI Clicked btn: "+ btn.objectName())
        if self.TTTGame.winner == None and self.TTTGame.game_over == True:        
            self.draw()
            return
        if self.TTTGame.game_over:
            self.player_wins()
            return
        self.unlock_gamefield()
        self.ui.turnLabel.setText(f"Its >>> {self.TTTGame.turn.name} <<< turn!")

    def draw(self):
        self.gameover = True
        self.ui.gameStateLabel.setText("Game Over!")
        self.ui.turnLabel.setText(f"Sorry, its a draw!")
        self.block_gamefield()

    def player_wins(self):
        self.gameover = True
        self.ui.gameStateLabel.setText("Game Over!")
        self.ui.turnLabel.setText(f"Winner is {self.TTTGame.winner.name}!")
        self.ui.p1ScoreLcd.display(int(self.TTTGame.player1.score))
        self.ui.p2ScoreLcd.display(int(self.TTTGame.player2.score))
        self.add_winner_effect()
    
    def add_winner_effect(self):
        self.unlock_gamefield()
        btn1:QPushButton = self.findChild(QPushButton, "gridBtn_"+str(self.TTTGame.win_buttons[0]))
        btn2:QPushButton = self.findChild(QPushButton, "gridBtn_"+str(self.TTTGame.win_buttons[1]))
        btn3:QPushButton = self.findChild(QPushButton, "gridBtn_"+str(self.TTTGame.win_buttons[2]))
        self.winner_btn = [btn1, btn2, btn3]

        for btn in self.winner_btn:
            shadow_1 = QGraphicsDropShadowEffect()
            shadow_1.setBlurRadius(105.0)
            if self.TTTGame.winner == self.TTTGame.player1:
                shadow_1.setColor(QColor(255, 0, 0, 220))
            else:
                shadow_1.setColor(QColor(0, 0, 255, 220))                
            shadow_1.setXOffset(0)
            shadow_1.setYOffset(0)
            shadow_1.setParent(btn)
            btn.setGraphicsEffect(shadow_1)
        self.block_gamefield()
    
    def remove_winner_effect(self):
        for btn in self.winner_btn:
            btn.setGraphicsEffect(None)
        self.winner_btn = []

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(BASE_DIR, 'appicon.ico')))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
