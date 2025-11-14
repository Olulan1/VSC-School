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
filename = file # this is hard to make the autograder recognise
with open(filename, "r") as f1:
     next(f1)
     lines = f1.readlines()
data = []
IDS = []
grades = []
avgs = []
students = {}
sno = 0
for line in lines:
     data.append(line)
data = [line.split(",") for line in data]
for line in data:
     while ("" in line):
          line.remove("")
     while ("\n" in line):
          line.remove("\n")
     print(line)
     IDS.append(line[0])
     linelen = len(line)
     ll = linelen-1
     line[ll] = line[ll].strip()


for line in data:
     sno = sno+1
     print(f"student: {sno}")
     i = 1
     total = avg = x = 0
     print(line)
     for i in range (1, len(line)):
          total+=int(line[i])
          x+=1

     print("X is:",x)
     print(total)
     avg = float(total/x)
     t = round(avg)
     if t >= 70: temp = "1"
     elif 69 >= t >= 60: temp = "2:1"
     elif 59 >= t >= 50: temp = "2:2"
     elif 49 >= t >= 40: temp = "3"
     elif t < 40: temp = "F"
     grades.append(temp)
     avgs.append(avg)
     total = 0
filename = filename.strip(".csv")
filename = f"{filename}_out.csv"

for i in range (0, len(IDS)):
     students.update({IDS[i]:grades[i]})
     s = str(IDS[i])+","+str(format(avgs[i],'.2f'))+","+str(grades[i])+"\n"
     if i == 0:
          with open(filename, "w") as f2:
               f2.write(s)
     else:
          with open(filename, "a") as f3:
               f3.writelines(s)
