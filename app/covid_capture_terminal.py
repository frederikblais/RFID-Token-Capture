# randomly generate one data file per classroom, you must generate 5 classrooms for one day.
import os
import os.path
import datetime
import time

# Clear the screen.
os.system('clear')

line = '------------------------------------------'
title = '|            CAPTURE TERMINAL            |'

# Header
print (line)
print (title)
print (line)

# Set data directory
os.chdir("app")
os.chdir(".data")

# Create 5 txt files for the day
def create_file():
    file_count = 0

    while file_count < 5:
        cwd = os.getcwd()

        # Create file "classroom(number).txt"
        file_name = os.path.join(cwd, "classroom"+str(file_count + 1)+".txt")

        txt_file = open(file_name, "w")

        #
        student_file = open("students.txt","r")
        for _ in range(1,20+1):
            date = datetime.date.today()

            rfid_data = student_file.readline()
            formated_data = str(rfid_data)+str(date)+os.linesep
            fd = str.join(";", formated_data.splitlines())
            toFile = fd
            txt_file.writelines(toFile)

        txt_file.close()

        resp = "Data file " + str(file_count + 1) + " generated"
        print(resp)
        file_count += 1

# Delete all the files in .data
def delete_file():
    resp = "Data file deleted"
    print(resp)

# Input Loop, break if "x" is selected
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
        os.system('clear')
        break
    
    else:
        print("invalid choice")