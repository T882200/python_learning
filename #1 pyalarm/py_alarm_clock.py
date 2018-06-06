#-------------------------------------------------------------------------------
# Name:        py_alarm_clock.py
# Purpose: A simple Python program to make the computer act
# like an alarm clock. Start it running from the command line
# with a command line argument specifying the duration in minutes
# after which to sound the alarm. It will sleep for that long,
# and then beep a few times. Use a duration of 0 to test the
# alarm immediiately, e.g. for checking that the volume is okay.
#
# Author:      t8822_000
#
# Created:     14/02/2018
# Copyright:   (c) t8822_000 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Alarm clock using Python Tkinter module

#import Tkinter for GUI
from tkinter import *
from tkinter import ttk

#imports for time counting
import time
import os


#for pop-up message box
from tkinter import messagebox


#Main Window
#def main():
root = Tk()
root.title("Alarm clock")

#Alarm time request button
def SubmitButton():

  AlarmTime = entry1.get()

  #call for Message1 function
  Message1()
  #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))  #delayed in execution

  CurrentTime = time.strftime("%H:%M")

  #message for aproove the time request
  print("the alarm time is: {}".format(AlarmTime))
  #label2.config(text="")

  #loop for time counting when the thread is in sleep mode
  while AlarmTime != CurrentTime:
    #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))
    CurrentTime = time.strftime("%H:%M")
    time.sleep(1)

  #check if time for alarm came
  if AlarmTime == CurrentTime:
     print("now Alarm Musing Playing")
     #open music file
     os.system("start alarm-music.mp3")


     #TODO: add option to choose specific favorit song
     #TODO: add option to the user to play most trending video in YouTube or most viewed video in the YouTube etc.
     #TODO: add option to paste a link for youtube video to open and play


     #text label when the music plays
     label2.config(text = "Alarm music playing.....")

     #recive the user message input
     messagebox.showinfo(title= 'Alarm Message', message= "{}".format(entry2.get()))




#message for time counting when the thread is in sleep mode
def Message1():
    AlarmTimeLable= entry1.get()
    label2.config(text="the Alarm time is Counting...")
    #label2.config(text= "the Alarm will ring at {}".format(AlarmTimeLable))

    #the message box tkinter command
    messagebox.showinfo(title = 'Alarm clock', message = 'Alarm will Ring at {}'.format(AlarmTimeLable))



#The TkInter GUI frame
frame1 = ttk.Frame(root)
frame1.pack()
frame1.config(height = 100, width = 100)

label1= ttk.Label(frame1,text = "Enter the Alarm time :")
label1.pack()


entry1 = ttk.Entry(frame1, width = 30)
entry1.pack()
entry1.insert(3,"example - 13:15")

labelAlarmMessage= ttk.Label(frame1, text="Alarm Message:")
labelAlarmMessage.pack()

entry2= ttk.Entry(frame1, width=30)
entry2.pack()

button1= ttk.Button(frame1, text= "submit", command=SubmitButton)
button1.pack()
#this Label2 will show the Last Alarm Time
label2= ttk.Label(frame1)
label2.pack()


#label2.config(text="hello")

#run TkInter GUI
root.mainloop()