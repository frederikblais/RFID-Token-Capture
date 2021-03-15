# RFID-Token-Capture

## Context: 
The College wants to take care of their students and has installed an 
RFID token capture terminal in each classroom. Each time a student enters or 
leaves a classroom, the capture terminal registers a unique token from the 
student’s phone.

Each student’s phone has downloaded an application to 
communicate with the College capture terminal. Note that the maximum 
classroom capacity is 20 students for all the classrooms.

The terminal management application saves the data in a text file 
according to the following format:

> idrfid; date; intime; outtime

## Objective:
- [] Make the covid_capture terminal.py script which will randomly generate one data 
    file per classroom, you must generate 5 classrooms for one day.

- [] Make the covid_rapport.py which at the end of the day create a report. To do so, 
    you must ask the user if there are any students who have been diagnosed with 
    positive Covid-19, if there is none, the day is over! 

- [] On the other hand, if there is at least one student with a positive Covid-19 
    diagnosis, you should search all the students that was in the same classroom that 
    the positive Covid-19 student in a period of 15 minutes. 

- [] You must create a file that indicate the list of all the students who have been in 
    contact with the positive Covid-19 student.

You must use the different collections provided by Python to simplify your work