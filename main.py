import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Reading CSV file
df = pd.read_csv("students.csv")
print("Class Students Details")
print(df)
# Adding new column called Total
df["Total"]=df["Python"]+df["Maths"]+df["AI"]+df["DBMS"]
#Adding new column called Average
df["Average"]=df["Total"]/4
df["Average"]=df["Average"].round(2)
subjects = np.array(["Python","Maths","AI","DBMS"])
#Adding new column called Percentage
df["Percentage"] = (df["Total"]/400)*100
df["Percentage"] = df["Percentage"].round(2)
df["Status"] = df["Average"].apply(lambda x:"Pass" if x>=40 else "Fail")
print("After Updating Student Details")
print(df)
average = np.array([df["Python"].mean(),df["Maths"].mean(),df["AI"].mean(),df["DBMS"].mean()])
print("\n===========================================")
print("       STUDENT PERFORMANCE REPORT    ")
print("===========================================")
#Finding number of Students in the class
totalstudents = len(df)
print(f"{'Total Students':<20}:{totalstudents}")
# Total no.of Passed students
passed = (df["Status"]=="Pass").sum()
print(f"{'Passed Students':<20}:{passed}")
# Total no.of Failed students
failed = (df["Status"]=="Fail").sum()
print(f"{'Failed students':<20}:{failed}")
#Class average marks
clavg = df["Average"].mean()
print(f"{'Class Average':<20}:{clavg:.2f}")
# Printing Class Topper
print("\n😀 Class Topper")
index = df.loc[df["Total"].idxmax()]
name = index["Name"]
print(f"{'Name':<20}:{name}")
total = index["Total"]
print(f"{'Total':<20}:{total}")
topperavg = index["Average"]
print(f"{'Topper Average':<20}:{topperavg:.2f}")
# Finding Best Subject in the Class
print("📚 Best Subject")
avgsubject = {}
for subject in subjects:
    avgsubject[subject] = df[subject].mean()
bestsubject = max(avgsubject,key = avgsubject.get)
print(f"{'Subject':<20}:{bestsubject}")
print(f"{'Average':<20}:{avgsubject[bestsubject]:.2f}") 
# finding Lowest Scored Student name Total Marks
print("Lowest Marks Student ") 
lowest = df.loc[df["Total"].idxmin()]
print(f"{'Slow learner':<20}:{lowest["Name"]}")
print(f"{'Student Marks':<20}:{lowest["Total"]}")
# printing No.of students who are scored more than class average
moreclassAvg = (df["Average"]>clavg).sum()
print(f"{'More than class Avg':<20}:{moreclassAvg}")
#printing no.of students who scored more than 80 in python
highpython = (df["Python"]>=80).sum()
print(f"{'Above 80 in Python':<20}:{highpython}")
#printing Passed Students names,average,status
print("Passed Student Names")
passedstudents = df[df["Status"]=="Pass"]
print(passedstudents[["Name","Average","Status"]])
#printing failed Students names,Average,Status
failedstudents = df[df["Status"]=="Fail"]
print("Failed Students Names")
print(failedstudents[["Name","Average","Status"]])
# printing Subject wise Toppers
print("😀 Subject Toppers")
print("📚 Highest marks in Each Subject")
for subject in subjects:
    index = df[subject].idxmax()
    name = df.loc[index,"Name"]
    marks = df.loc[index,subject]
    print(subject,"->",name,"->",marks)
print("🥺 Lowest marks in Each Subject")    
for subject in subjects:
    index = df["Total"].idxmin()
    name = df.loc[index,"Name"]
    marks = df.loc[index,subject]
    print(subject,"->",name,"->",marks) 
# finding Maximum and minimum Marks in Each subject     
for subject in subjects:
    print("Maximum Marks in :",subject," ",df[subject].max())
    print("Minimum Marks in :",subject," ",df[subject].min()) 
# finding topper in a Particular Subject      
mathstopper = df.loc[df["Maths"].idxmax()]
print(mathstopper["Name"])
print(mathstopper["Maths"]) 
#printing lowest Average in the class
print("Lowest Average in the Class")
lowestavg = df.loc[df["Average"].idxmin()]
lname = lowestavg["Name"]
lavg = lowestavg["Average"]
print(f"{'Name':<20}:{lname}")
print(f"{'Average':<20}:{lavg}")
print("Students who are Passed and above 80 Average")
passavg = df[(df["Status"]=="Pass")&(df["Average"]>80)]
print(passavg[["Name","Status","Average"]])
avbove80inpython = df[df["Python"]>=80]
print(avbove80inpython[["Name","Python"]])
print("No.of Students who are scored above 80 in AI")   
print((df["AI"]>=80).sum())  
print("Average Above 80 students names")
avg80 = df[df["Average"]>=85] 
print(avg80[["Name","Average"]])
print("Total :",(df["Average"]>=85).sum())
print("This is the complete Information About Class! ")
print("===============================================")
#********Data Visualization Using Matplotlib Library*******
#Bar graph for Name VS Total
plt.bar(df["Name"],df["Total"],color = ["#6251b5","#962d83","#2d9196","#289e65","#8a9e28","#9e7e28","#9e4b28","#a82d22"])
plt.title("Student VS Marks")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.xticks(rotation = 45)
plt.show()
# Printing Pie chart(Pass VS Fail)
label = ["Pass","Fail"]
values = [passed,failed]
plt.pie(values,labels = label,colors = ["#f542f2","#d12a78"],autopct = "%1.1f%%",explode = [0,0.1],shadow = True,startangle = 90)
plt.title("Pass And Fail Percentage")
plt.show()
# Printing Bar graph for Subjects VS Average
plt.bar(subjects,average,color = ["#d1cc2a","#bd4c1c","#1cbdbd","#851cbd"])
plt.title("Subject VS Average")
plt.xlabel("Subject")
plt.ylabel("Average")
plt.xticks(rotation = 45)
plt.show()
#printing pie chart based on the condition
explode = [0.1 if total == df["Total"].max() else 0 for total in df["Total"]]
plt.pie(df["Average"],labels = df["Name"],autopct = "%1.1f%%",explode = explode,shadow = True,startangle = 90)
plt.title("Average Marks for Each student")
plt.show()
#Bar chart for Name VS Average
sort_avg = df.sort_values("Average",ascending=False)
plt.bar(sort_avg["Name"],sort_avg["Average"])
plt.title("Average VS Student")
plt.xlabel("Student Name")
plt.ylabel("Average")
plt.xticks(rotation = 45)
plt.show()
# Python VS Marks
"""plt.bar(df["Name"],df["Python"],color = ["#9fb322","#f542f2","#d12a78","#bd4c1c","#1cbdbd","#851cbd","#b04213","#8f17e6"])
plt.title("Python Marks")
plt.xlabel("Student Name")
plt.ylabel("Python Marks")
plt.xticks(rotation = 45)
plt.show()
# Mathematics VS marks
plt.bar(df["Name"],df["Maths"])
plt.xlabel("Student Name")
plt.ylabel("Maths Marks")
plt.title("Mathematics VS Marks")
plt.xticks(rotation = 45)
plt.show()
# AI VS Marks
plt.bar(df["Name"],df["AI"])
plt.title("AI VS Marks")
plt.xlabel("Student Name")
plt.ylabel("AI Marks")
plt.xticks(rotation = 45)
plt.show()
#Bar chart for DBMS VS Marks
plt.bar(df["Name"],df["DBMS"])
plt.title("DBMS VS Marks")
plt.xlabel("Student Name");
plt.ylabel("DBMS Marks")
plt.xticks(rotation = 45)
plt.show()"""
students = df["Name"]
x = np.arange(len(students))
width = 0.2
plt.bar(x-0.3,df["Python"],width,label = "Python")
plt.bar(x-0.1,df["Maths"],width,label = "Maths")
plt.bar(x+0.1,df["AI"],width,label = "Ai")
plt.bar(x+0.3,df["DBMS"],width,label = "DBMS")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students performance in All subjects")
plt.xticks(x,students,rotation = 45)
plt.legend()
plt.tight_layout()
plt.show()