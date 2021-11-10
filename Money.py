import csv

#import my files
import myDict
import strip
import change
import func

############################################################

#open the files for Appending and Reading
#write = open("Money.csv",'a')
read = open("ReadFromHere.txt",'r')
filename = "Money.csv"

# define variables that are needed
file = []
output = []

############################################################

#read the text file and create the file list
for x in read:
  z = x.split("\t")
  date = z[0]
  what = z[1]

  amt = func.convertToFloat(z[2])
  balance = func.convertToFloat(z[3])

  for x in strip.strip:
    what = what.replace(x,"")

  for x in change.change:
    if x in what:
      what = x

  file.append([date,what,amt,balance])
    
#end for

############################################################

#for debugging
#print(myDict.dictionary)

#create the output list
for x in file:
  
  if x[1] in myDict.dictionary:
    output.append([myDict.dictionary[x[1]],x[0],x[1],x[2]])
  else:
    output.append(["zOther",x[0],x[1],x[2]])
   
#end for

############################################################

y = "Amazon"
total=float(0)
income=float(0)
subtotal=float(0)

print("=================================================================================================================")

output.sort()
for x in output:
  
  if x[0] != "Income":
    total = round(x[3]+total,2)
  else:
    income = round(x[3]+income,2)

  if y == x[0]:
    print(x)
  else:
    print("=================================================================================================================")
    print(x)

  y = x[0]
    
#end for

print("\nTOTAL INCOME:\t",income)
print("TOTAL SPENT:\t",total)

############################################################

#for x in file:
#  print(x)

#close the files for Appending and Reading
read.close()



