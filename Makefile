moc:
	.\moc.cmd

run:
	.\run.cmd

build-app:
	pyinstaller --noconsole --icon=resources/logo.ico --name=Cheat app.py
