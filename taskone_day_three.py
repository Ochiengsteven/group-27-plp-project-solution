# 1. Write a python program that simulates a door lock system such that:

# Password is set and stored in a variable,
# Commands to instruct the door are stored in variables.
# When a user enters the wrong password an error message is displayed and prompted to enter the password again.
# When a user enters “open” a “The door is now open” statement is displayed, when the “open” is entered more that once, a message is displayed saying, “the door is already open”
# When a user enters “close” a “The door is now locked” statement is displayed, when the “open” is entered more that once, a message is displayed saying, “the door is already locked”
# When a user enters “quit” the process is terminated and message is displayed.
# When a wrong message is entered or invalid key pressed a “Invalid input” message is displayed.
# When the door is locked or open, it prints out the last date/time the door was opened, eg “Door Last open  at 2022-07-05 08:46:20.535395”

from os.path import exists
import os ;import sys ;import subprocess #modules for clearing CMD and rebooting when setting up
import time  # importing time for delay
from datetime import datetime  # datetime module for timestamps

os.system("cls")  # clearing command line

last_time_closed = datetime.now() #first timestamp for door closed state
current_time = last_time_closed
first_opening = True #check for first opening of the door

password_tries = 3 #limited tries before exiting program

instruction_open = "open" #commands stored in variables
instruction_close = "close"
instruction_quit = "quit"

pass_key="" #empty password for initilising

def set_password(input_password): #function to set and change password to external file
    with open(file_name, 'w') as f:
        f.write(input_password)
        print("your password has been set \nRestarting")
        time.sleep(2)
        os.system("cls")


def time_difference(previous, current): #function for calcuating time duration since last action (open or close)
    # convert timestamps to datetime object
    #  previous = datetime.fromtimestamp(1652426243.907874)         #dummy data for testing function
    # #  print('Datetime Start:', previous)
    #  current = datetime.fromtimestamp(1657267451)
    #  print('Datetime End:', current)

    date_val = "("  #start of sting for return
    delta = current - previous # get delta time in seconds between two timestamps
    if delta.days > 0:  #check if delta days return a number indicating that theres more than 24hr difference between the previous and current timestamps
        date_val += str(delta.days)+" days " #appending number of days to date_val if available
    total_secs = delta.seconds 
    tmins = total_secs/60 #calculate possibility of time in minutes
    if tmins > 1:
        date_val += str(int(tmins))+" minutes "
        tsecs = total_secs % 60
        date_val += str(tsecs)+" seconds ago)"
    else:
        date_val += str(total_secs)+" seconds ago)" #if value isn't greater than 60 seconds return number of seconds
    return date_val


file_name = "init.txt" #file name to store password **insecure method

print("Hello and Welcome to Kifuli security lock system 🔐")

correct_password = False #check if password entered is correct for password tries
door_state = False  #initialise door state as closed when program starts

if exists(file_name): #check if file exists and reads password stored in it
    with open(file_name, "r") as rf:
        for line in rf:
            pass_key = line #read password from file

elif not exists(file_name):#if file does not exist, set your password to make the file
    set_password(input("set your new password\n"))
    os.system("cls")
    sys.stdout.flush()
    subprocess.call([sys.executable, os.path.realpath(__file__)] +sys.argv[1:]) #restart the program
    exit()#exit current program

username = input("enter your username\n") #ask for username 
password = input("enter your password(use N to set new password)\n") #password check input for user
os.system("cls")

while True:
    if not correct_password: #password checker loop
        if password != pass_key and password.upper() != "N": #if incorrect password
            if password_tries > 0: #counter for number of attempts
                print("Wrong password ❌. You have " + str(password_tries)+" tries left")
                password_tries -= 1
                password = input("enter the password again\n")
                os.system("cls")
            else:  #if no more tries are left break program and exit ***considered option to restart program
                print("Error ‼️ \nExceeded password attempts locking and exiting")
                time.sleep(1.8)
                os.system("cls")
                break
        elif password.upper() == "N": #if value entered is N start password change process
            password = input("enter your old password(use X to cancel)\n") #input for old password
            os.system("cls")
            if password == pass_key:
                set_password(input("set your new password\n")) #change password 
                os.system("cls")
                sys.stdout.flush()
                subprocess.call([sys.executable, os.path.realpath(__file__)] +sys.argv[1:]) #restart the program
                exit()#exit current program
                continue
            elif password.lower() == "x": #use value x to cancel password change process
                print("password remains unchanged ")
                time.sleep(1.2)
                continue
        elif password == pass_key: #if password input matches
            correct_password = True #change password flag to true
    else:#if passord flag is true
        print("Welcome", username)
        if door_state: #check if door is open (default is closed)
            duration = time_difference(last_time_opened, current_time) #check time difference  
            print("Door is OPEN Last open at ", last_time_opened, duration)
            last_time_opened = current_time #store current time as last time for reference
        else: #if door is closed
            duration = time_difference(last_time_closed, current_time)
            print("Door is LOCKED Last locked at ", last_time_closed, duration)
            last_time_closed = current_time
        print("use OPEN to open door ,use CLOSE to close door and use QUIT to exit")#instructions on available commands and their functionality
        input_text = input().lower()
        os.system("cls")
        if input_text == instruction_open: #command open door
            if not door_state: #if door is closed
                current_time = datetime.now()
                if first_opening: #check for first time opening
                    last_time_opened = current_time
                    first_opening = False
                door_state = True
            else:#if door is already open
                print("Error ❌, the door is already open")
                current_time = datetime.now()
        elif input_text == instruction_close: #command close door
            if not door_state:#if door is already closed
                print("Error ❌ , the door is already closed")
                current_time = datetime.now()
            else:#if door is open
                current_time = datetime.now()
                door_state = False
        elif input_text == instruction_quit: #command quit program
            print("Exiting")
            time.sleep(0.4)
            os.system("cls")
            break
        else:#invalid or unexpected input
            print("Invalid input")
        time.sleep(0.8)
        os.system("cls")
