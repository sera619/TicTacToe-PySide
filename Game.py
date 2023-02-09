from dataclasses import dataclass
import random

@dataclass
class Player:
    name: str
    symbol: str
    score: int = 0
    ai: bool = False

class TTTGame:
    player1: Player
    player2: Player
    game_over: bool = True
    turn: Player
    round: int
    winner: str = None
    playround: int = 1
    gamefield: dict = {
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "", 
        "9": ""
    }
    win_buttons: list = []
        
    def start_game(self):
        if self.player1 and self.player2:
            print("Start Game")
            self.game_over = False
            self.turn = self.player1
    
    def reset_game(self):
        self.gamefield = {
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "", 
        "9": ""}
        self.playround = 1
        self.turn = self.player1
        self.winner = None
        self.win_buttons = []

    def move_player(self, btn_name:str):
        print(btn_name[-1])
        if self.playround == 9:
            self.game_over = True
            return
        self.playround += 1
        self.gamefield[btn_name[-1]] = self.turn.symbol
        if self.check_win() == True:
            self.game_over = True
            self.winner = self.turn
            self.winner.score += 1
            print(f"Game Over, Winner is {self.winner.name}")
            return
        self.switch_turn()

    def switch_turn(self):
        if self.turn == self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1
        print(f"its {self.turn.name} turn!")

    def check_win(self) -> bool:
        b = self.gamefield
        #horizontal
        if b["1"] == b["2"] == b["3"] != "":
            self.win_buttons = ["1", "2", "3"]
            return True
        elif b["4"] == b["5"] == b["6"] != "":
            self.win_buttons = ["4", "5", "6"]
            return True
        elif b["7"] == b["8"] == b["9"] != "":
            self.win_buttons = ["7", "8", "9"]
            return True
        # vertical
        elif b["1"] == b["4"] == b["7"] != "":
            self.win_buttons = ["1", "4", "7"]
            return True
        elif b["2"] == b["5"] == b["8"] != "":
            self.win_buttons = ["2", "5", "8"]
            return True
        elif b["3"] == b["6"] == b["9"] != "":
            self.win_buttons = ["3", "6", "9"]
            return True
        # diagonal
        elif b["1"] == b["5"] == b["9"] != "":
            self.win_buttons = ["1", "5", "9"]
            return True
        elif b["3"] == b["5"] == b["7"] != "":
            self.win_buttons = ["3", "5", "7"]
            return True
        else:
            print("No Winner")
            return False

    def ai_set_move(self) -> str:
        moveable = []
        for k in self.gamefield.keys():
            if self.gamefield[k] == "":
                moveable.append(k)
        i = random.randint(1,len(moveable))
        self.move_player("gridBtn_"+str(moveable[i-1]))
        return str(moveable[i-1])
        


