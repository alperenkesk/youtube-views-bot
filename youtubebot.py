import webbrowser
from time import sleep
import os
import time


def mainMethod():	

	webbrowser.open('https://www.youtube.com/channel/UCCzpvX3ly5o2IUslqgMpLHg') #youtube video link
	sleep(38)   #time
	os.system('pkill -3 opera') 
	
	webbrowser.open('https://www.youtube.com/watch?v=A_3kKwoZ9ow')
	sleep(33)
	os.system('pkill -3 opera')


if __name__ == "__main__":
	while(True):
		mainMethod()
