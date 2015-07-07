import socket
import wave
import sys
import pyaudio
import thread
import time
from Tkinter import *

root = Tk()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 9999))

CHUNK = 16

clientlist = []

def play(data, w, clientsocket):
	while data != '':
		data = w.readframes(CHUNK)
		for client in clientlist:
			try:
				client.send(data)
			except:
				pass

def buttonPressedThread(numclients, songpath):
	serversocket.listen(numclients)
	
	try:
		wf = wave.open(songpath, 'rb')
	except:
		return
		
	data = wf.readframes(CHUNK)
	
	successLabel=Label(root, text="Launched successfully.")
	successLabel.pack()

	for i in range(numclients):
		clientsocket, addr = serversocket.accept()
		s = str(i+1)+" connected."
		print s
		clientlist.append(clientsocket)
	print 'Playing...'
	
	thread.start_new_thread(play, (data, wf, clientsocket, ))
	
def buttonPressed():
	numclients = numclientsEntry.get()
	songpath = songnameEntry.get()
	
	thread.start_new_thread(buttonPressedThread, (int(numclients), songpath ))
	
root.minsize(width=300,height=220)
root.maxsize(width=300,height=220)
root.wm_title("Musynk Server")

var = StringVar()
IPlabel = Label(root, textvariable=var, wraplength = 250)
ipstring = "Server IP: " + socket.gethostbyname(socket.getfqdn())
if ipstring[11:17] == "127.0.":
	ipstring = "Unable to fetch IP. Find it using ipconfig or ifconfig from CMD or terminal."
var.set(ipstring)
IPlabel.pack()

var2 = StringVar()
instructionLabel = Label(root, textvariable=var2, wraplength = 250)
var2.set("Enter this IP address on the Musynk app on the client machine.")
instructionLabel.pack()

numclientsLabel=Label(root, text="Number of clients:")
numclientsLabel.pack()
numclientsEntry = Entry(root)
numclientsEntry.pack()

songnameLabel=Label(root, text="Path to .wav file: (e.g. /usr/local/music/Bartender.wav)", wraplength = 250)
songnameLabel.pack()
songnameEntry = Entry(root)
songnameEntry.pack()

B = Button(root, text ="Launch", command = buttonPressed)
B.pack(side=BOTTOM)

root.iconbitmap('images/favicon.ico')
root.mainloop()