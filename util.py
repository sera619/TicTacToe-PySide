from dataclasses import dataclass


@dataclass
class ButtonStyles:
    MenuBtn = """QPushButton {
    color:#FFF;
    border: 1px solid orange;
    padding: 3px 8px;
	border-radius: 10px;
	font-weight: 700;

}

QPushButton::Hover{
	color: orange;
	font-weight: 700;
}

QPushButton::pressed{
	border: 1.4px solid orange;
	border-radius: 15px;
	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 0, 160), stop:0.994318 rgba(148, 49, 0, 160));
}"""
    GameBtnNormal = """QPushButton{
	border: 1px solid gray;
	border-radius: 37%;
	font-weight: bold;
	color: #FFF;
		
	font: 32pt "Street Writer (noah)";
	background-color: qlineargradient(spread:pad, x1:0.5175, y1:0.517, x2:0.983, y2:0.965909, stop:0.0738636 rgba(0, 0, 0, 226), stop:0.664773 rgba(33, 33, 33, 222), stop:1 rgba(57, 57, 57, 222));
}
QPushButton::Hover{
	color: rgb(3, 196, 255);
	font-size: 48px;
}

QPushButton::Disabled{
	
	background-color: rgba(67, 67, 67, 75);
	color:black;
	
}

"""