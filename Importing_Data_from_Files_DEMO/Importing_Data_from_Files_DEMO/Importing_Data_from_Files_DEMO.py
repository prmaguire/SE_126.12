#WEEK 3 Day 1: Importing Data from a File


#CSV: Comma separated value
#RECORDS: rows of the file, different types of data grouped around "something" (something = person, room, location, machine, etc data that  belongs to the same "thing")
#FIELDS: columns of the file, lists/sets of data that are all the same type (ie names, ages, salaries, etc)

import csv #import csv library so we can read the file

total_records = 0 #you should ALWAYS have a total records var and value (holds the true total number of records (Rows) in the file)

total_salary = 0 #this holds the total salaries of all employees (this is a sum total var)

#FIELD HEADER HINTS:
name = "NAME"
age = "AGE"
sal= "SALARY"

print("{0:5} \t\t  {1:5} \t {2:8}".format(name, age, sal))

#right click text/csv file in folder view --> "properties" to find the file location NOTE: it will NOT include the file name and extension, you MUST ADD THIS
#these file locations are cAsE sEnSiTiVe and space/special char sensitive so DOULBE and TRIPLE CHECK THEM
#flip all '\' to '/'

with open("C:/Users/008008122/Desktop/SE_126.12/example.csv") as csvfile:
    
    #notice the ':' and minimize option on line 25 --> everything must be indented now (until we are ready to be finished with the file)    

    file = csv.reader(csvfile) #now the file we have connected to the program is known as 'file'

    #below is a FOR LOOP
    #for loops are loops -- repeated sequence of code
    #they continue not based on a condition but on a RANGE

    for rec in file:
        
        #notice the ':' and minimize button --> this is a control flow statement and all lines of code that are "within" the for loop must be indented
        #RANGE: for every record in the file, do the following

        #TRICK OF THE TRADE
        name = rec[0]
        age = rec[1]
        salary = float(rec[2])
        #^^^DO FOR LAB 3A^^^    
    
        total_records += 1
        #print("TOTAL RECORDS = ", total_records)

        #print the 'rec' to see it in list view (how the comp sees it)
        #print(rec)

        #print each piece of data (one per field) as individual values (no longer in full list form)
        print("{0:5} \t\t {1:5} \t\t ${2:8.2f}".format(name, age, salary))
        #ALL DATA COMING INTO A PYTHON PROGRAM IS TREATED AS A STRING UNLESS OTHERWISE CAST AS A NUMERIC TYPE (this is why rec[2] is floated)

        total_salary += salary

print("\n\n\nFinished Processing")
print("---------------------------\n")
print("TOTAL RECORDS: ", total_records)
print("ANNUAL PAYROLL: ${:.2F}".format(total_salary))
print("\n---------------------------\n")
        

    