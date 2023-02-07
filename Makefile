clean:
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist
	if exist "./__pycache__" rd /s /q .\__pycache__
	if exist "./src/__pycache__" rd /s /q .\src\__pycache__

build:

	pyinstaller main.spec

run:
	pyside6-uic .\src\Ui_main.ui > .\src\ui_Ui_main.py
	pyside6-rcc .\src\res.qrc > res_rc.py
	python .\main.py