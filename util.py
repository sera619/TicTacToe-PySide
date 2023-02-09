from dataclasses import dataclass


@dataclass
class ButtonStyles:
	MenuBtn = """QPushButton {
    color:#FFF;
    border: 1px solid orange;
    padding: 3px 8px;
	border-radius: 10px;
	font-weight: 700;
	font: 14pt "PhrasticMedium";
}

QPushButton::Hover{
	color: orange;
	font-weight: 700;
}

QPushButton::pressed{
	border: 1.4px solid orange;
	border-radius: 15px;
	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 0, 180), stop:0.994318 rgba(148, 49, 0, 180));
}"""
	GameBtnNormal = """QPushButton{
	border: 1px solid gray;
	border-radius: 37px;
	font-weight: bold;
	color:rgb(255, 85, 0);
	font: 32pt "Street Writer (noah)";
	background-color: qlineargradient(spread:pad, x1:0.5175, y1:0.517, x2:0.983, y2:0.965909, stop:0.0738636 rgba(0, 0, 0, 226), stop:0.664773 rgba(33, 33, 33, 222), stop:1 rgba(57, 57, 57, 222));
}
QPushButton::Hover{
	color:#FFF;
	font-size: 56px;
	border: 2px solid orange;
	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 0, 160), stop:0.994318 rgba(148, 49, 0, 160));
}
QPushButton::Disabled{
	background-color: rgba(67, 67, 67, 75);
	color:black;
}
QPushButton:Pressed{
	border-radius:37px;
}
"""
	TetrisLabel = """QLabel{
font: 18px "PhrasticMedium";
color: rgba(225, 150, 0, 255);
}"""

	LineEdit ="""QLineEdit{
	font: 16pt "PhrasticMedium";
	border-radius: 8px;
	border:1px solid orange;
	color: rgba(225, 150, 0, 230);
	padding:2px;
	text-align:center;


	background-color: qlineargradient(spread:pad, x1:0.5175, y1:0.517, x2:0.983, y2:0.965909, stop:0.0738636 rgba(0, 0, 0, 226), stop:0.664773 rgba(33, 33, 33, 222), stop:1 rgba(57, 57, 57, 222));
}"""

	ComboBox = """QComboBox{
font: 16pt "PhrasticMedium";
color: rgba(225, 150, 0, 230);
	border:1px solid orange;
	background-color: qlineargradient(spread:pad, x1:0.5175, y1:0.517, x2:0.983, y2:0.965909, stop:0.0738636 rgba(0, 0, 0, 226), stop:0.664773 rgba(33, 33, 33, 222), stop:1 rgba(57, 57, 57, 222));
	border-radius: 8px;
padding: 2px;
padding-right:2px;

}
"""
	LCDTetris = """QLCDNumber{
		color: rgb(225, 150, 0);
		border: 1px solid orange;
		border-radius: 15px;
		
	}"""