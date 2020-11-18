build: main.py
	sudo apt-get install python-tk python3-tk tk-dev
	sudo apt install sqlite3
	pip3 install matplotlib-venn
	pip3 install pyinstaller

rustize:
	curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
