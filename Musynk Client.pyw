import sys,os
import pyaudio
import wave
import thread
import socket
from Tkinter import *



root = Tk()

root.minsize(width=300,height=100)
root.maxsize(width=300,height=100)
root.wm_title("Musynk Client")

serverIPLabel=Label(root, text="Server IP:")
serverIPLabel.pack()
serverIPEntry = Entry(root)
serverIPEntry.pack()

def buttonPressedThread(ip):
	s = socket.socket()
	CHUNK = 1024
	s.connect((ip, 9999))
	musikz = s.recv(CHUNK)
	p = pyaudio.PyAudio()
	stream = p.open(format = p.get_format_from_width(2), channels = 2, rate = 44100, output = True)
	data = s.recv(CHUNK)

	while data != '':
		stream.write(data)
		data = s.recv(CHUNK)

	stream.stop_stream()
	stream.close()
	p.terminate()

def buttonPressed():
	thread.start_new_thread(buttonPressedThread, (serverIPEntry.get(), ))

B = Button(root, text ="Play", command = buttonPressed)
B.pack(side=BOTTOM)

if os.name == "nt":
	root.iconbitmap(os.path.dirname(os.path.abspath(__file__)) +'\\images\\favicon.ico')
else :
	root.iconbitmap(os.path.dirname(os.path.abspath(__file__)) +'/images/favicon.ico')

root.mainloop()
