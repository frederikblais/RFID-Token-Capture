# randomly generate one data file per classroom, you must generate 5 classrooms for one day.
import os
import os.path
import radar
import time
import random

import datetime as dt
from datetime import timedelta

import csv
from tempfile import NamedTemporaryFile

import re

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
            start_time = radar.random_time(start='2021-03-01T08:00:00', stop='2021-03-02T15:59:59')

            # End Time
            out_time = radar.random_time(start='2021-03-01T15:59:59', stop='2021-03-01T23:59:59')

            rfid_data = student_file.readline()
            raw_data = [rfid_data,str(date),str(start_time),str(out_time)]
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
        os.remove('infected.txt')
        resp = "Data file deleted"
        print(resp)
    except:
        print("Files not found.")

# CHECK FOR COVID EXPOSURES   
def covid_Alert():
    
    infected_List = [] # create a list of infected 
    
    with open('classroom1.txt', 'r+') as csvfile:
        temp_list = [] # Create temp copy of the csv file
        
        clientsReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        
        for row in clientsReader:
            temp_list.append(row)
            
        now = dt.datetime.now()
        infectedTime = now.replace(hour=8, minute=35, second=0, microsecond=0)
        contagionTime = now.replace(hour=8, minute=45, second=0, microsecond=0)
        
        print(str(infectedTime) + " The infected time")
        
        for line in temp_list:
 
                studentTime = line[2]
                studentHourString, studentMinuteString = studentTime.split(':', 1)
                studentHour = studentHourString.replace("0", "")
                
                studentHour = int(studentHourString[2:])
 
                studentMinute = int(studentMinuteString[0:2])
                
                
                today = now.replace(hour=int(studentHour), minute=studentMinute, second=0, microsecond=0)
                
                if infectedTime <= today <= contagionTime:
                    print("--CORONA VIRUS DETECTED-- Student: " + line[0])
                    infected =str(line[0])
                    infected_List.append(infected)
                    
                else:
                    print("--Student is safe-- Student: " + line[0])
    with open('infected.txt', 'w', newline='') as csvfile:
        
        csv_writer = csv.writer(csvfile, delimiter=' ', quotechar='|')
        for line in infected_List: # Attempting to write the updated infected to the txt file
            csv_writer.writerow(line)
 
        print('File Created!')

# Input Loop, break if "x" is selected
while True:

    print()

    print("[1] Generate data files for the day (5)")
    print("[2] Delete data files")
    print("[3] Generate covid rapport")
    print("[x] Exit")
    choice = input('>> ')
    print()

    if choice == "1":
        create_file()

    elif choice == "2":
        delete_file()

    elif choice == "3":
        covid_Alert()

    elif choice == "x":
        os.system('clear')
        break
    
    else:
        print("invalid choice")