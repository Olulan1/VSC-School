'''
Portfolio Task - Grade Analyser

In order to decide student's overall classification, the university needs to take an overall mean average of their grades across all modules.
The classifications and boundaries are as follows:
>= 70 : 1
>=60 : 2:1
>=50 : 2:2
>=40 : 3
<40 : F

Each student's data is stored in a row in a csv file (4 sample files have been provided).
Students can have between 1 - 12 modules, for example:
203982,73,42,55,83,,,,,,,, # 4 modules
203742,55,97,57,37,76,68,,,,,, # 6 modules
You should ensure that you consider the number of modules when calculating your mean.

Your code needs to:
- ask for the filename of the student file
- read in the data, and for each student calculate their average grade and classification
- write out this calculated data in the format:
     student_id,average_grade,classification
     The average grade should be given to 2 decimal places
     this can be achieved by using the following in an fstring: {variable_name:.2f}
- write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

Your output files must be structured exactly as described - output files for all the test files have been provided so you can compare and ensure they are identical.

Note:
Your code will only be tested on valid files in the format shown in the 4 example files in this folder - you do not need to validate any data.
'''
import sys
file = input("Your filename: ")
filename = f"VSC-School/Task1.5/task2/{file}"
with open(filename, "r") as f1:
     next(f1)
     lines = f1.readlines()
data = []
students = {}
grades = []
sno = 0
for line in lines:
     data.append(line)
data = [line.split(",") for line in data]
for line in data:
     sno = sno+1
     del line[12]
     i = 1
     total = avg = 0
     first = False
     for i in range(1, 12):
          try:
               total+=int(line[i])
          except ValueError:
               if first == False:
                    print(f"No. of modules: {i-1}")
                    print(f"Total: {total}")
                    x = i-1
               first = True         
     print("X is:",x)
     first = False
     avg = float(total/x)
     print(avg)
     print(f"new student: {sno}")
     total = 0

