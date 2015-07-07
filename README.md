# Musynk
A tiny desktop app that allows you to play music in sync on several computers in a network.

### Instructions for Windows users:
- Download and install Python 2.7 from [here](https://www.python.org/downloads/) if you don't already have it.
- Download and install PyAudio from [here](https://people.csail.mit.edu/hubert/pyaudio/).
- Double-click "Musynk Server.pyw" to launch the server which streams the music to the clients.
- Double-click "Musynk Client.pyw" to launch the client which plays the music it receives from the server.

### Instructions for Linux users:
- Run the dependency installer shell script by running `bash depinstaller.sh` from the terminal.
- Run `python Musynk\ Server.py` from the terminal to launch the server which streams the music to the clients.
- Run `python Musynk\ Client.py` from the terminal to launch the client which plays the music it receives from the server.