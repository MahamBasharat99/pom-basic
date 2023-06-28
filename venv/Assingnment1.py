#Triangle Star
'''string=""
y=5
for x in range(1,y+1):
    for i in range(0,x):
        string = string + "*"
    print(x,string)
    string = ""

string1=""
y=5
for x in reversed(range(y+1)):
    for i in range(0,x):
        string1 = string1 + "*"
    print(x,string1)
    string1 = ""'''




#Factorial of a Number
'''sum=1
num = int(input("Enter Number for factorial"))
for x in range(1 , num+1):
      #print("go")
      if x == num:
          sum = sum * x
          print("Factorial of {} is {}".format(num,sum))
      else:
          sum = sum * x
          print(x)'''



#Factorial of a Number
sum1=1
num = int(input("Enter Number for factorial"))
for i in reversed(range(num+1)):
   if i > 0:
       sum1 = sum1 * i
       print(sum1,i)
   else:
       print("Factorial of {} is {}".format(num,sum1))

#Reverse String
name = 'INVOZONE'
reverseWord = ''
for v in reversed(range(len(name))):
    reverseWord = reverseWord + name[v]
    print(name[v])
print(reverseWord)

#print pyramid with *
star =""
for m in range(0,5):
    star=""
    print(m)
    for k in range(0,5-m):
        star = star + " "
    for n in range(m+1):
        star = star+ " *"
    print(star)

#print triangle with *

for o in range(0,5):
    data = ""
    for p in range(0,o+1):
        data=data + "*"
    print(data)










