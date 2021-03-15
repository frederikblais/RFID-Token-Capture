# randomly generate one data file per classroom, you must generate 5 classrooms for one day.
import os

# Clear the screen.
os.system('clear')

line = '------------------------------------------'
title = '|            CAPTURE TERMINAL            |'

# Header
print (line)
print (title)
print (line)

def create_file():
    str = "Data file generated"
    print(str)

def delete_file():
    str = "Data file deleted"
    print(str)

while True:

    print()

    print("[1] Generate data files for the day (5)")
    print("[2] Delete data files")
    print("[x] Exit")
    choice = input('>> ')
    print()

    if choice == "1":
        create_file()

    elif choice == "2":
        delete_file()

    elif choice == "x":
        break
    
    else:
        print("invalid choice")