import os
# Clear the screen.
os.system('clear')

line = '------------------------------------------'
title = '|               RAPPORT                  |'

# Header
print (line)
print (title)
print (line)

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