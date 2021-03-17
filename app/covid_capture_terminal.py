# randomly generate one data file per classroom, you must generate 5 classrooms for one day.
import os
import os.path
import radar
import time
import random

import datetime as dt
from datetime import timedelta

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
            date = dt.date.today()
            
            # Start time
            start_time = radar.random_time(start='2021-03-01T08:00:00', stop='2021-03-02T20:59:59')

            # End Time
            #rand_minute = random.randint(0, 60)
            #end_time = start_time.hour , (start_time+timedelta(minutes = rand_minute))

            rfid_data = student_file.readline()
            raw_data = [rfid_data,str(date),str(start_time)] #,str(end_time)
            formated_data = [x[:-1] for x in raw_data]
            txt_file.write(str(formated_data)+'\n')

        txt_file.close()

        resp = "Data file " + str(file_count + 1) + " generated"
        print(resp)
        file_count += 1

# Delete all the files in .data exept student.txt
def delete_file():
    try:
        os.remove('classroom1.txt')
        os.remove('classroom2.txt')
        os.remove('classroom3.txt')
        os.remove('classroom4.txt')
        os.remove('classroom5.txt')
        resp = "Data file deleted"
        print(resp)
    except:
        print("Files not found.")

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