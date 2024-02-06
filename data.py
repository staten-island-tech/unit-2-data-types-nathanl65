#Data Types 
#Nuymbers 1,2,3,
""" def add(x,y):
    print(x+y)
add(1,2)
#strings "a,b,c"
name = "Mark"
def greeting(person):
    print(person)
greeting(name)
#1 and "1" are not the same
add("1","2")
#undefined/nuLL


#booleans
tenure = False
def is_tenured(status):
    if(status == True):
        print("They have tenure")
    else:
        print("They are not tenured")

is_tenured(tenure)

x = 3
y = float(3)
print(x,y)

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
        print(i)

values = ["w","e","s","t"]
print(values[0])
print(values[3])"""

""" x = "6 4"
y= x.split()
z = y[1] """

""" numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

for oddnumber in numbers:
    if(oddnumber == "1", "3", "5", "7", "9"):
        print("Odd")

for evennumber in numbers:
    if(evennumber == "2", "4", "6", "8", "0"):
        print("Even") """

#Challenge 1

number = input("Give me a number between 1 and 10 ")
if number == "1":
    print("odd")
elif number == "3":
    print("odd")
elif number == "5":
    print("odd")
elif number == "7":
    print("odd")
elif number == "9":
    print("odd")
else:
    print("even")

#Challenge 2

service = input("How was the service? ")
if service == "bad":
    print("0% tip")
elif service == "okay":
    print("15% tip")
elif service == "good":
    print("20% tip")
elif service == "great":
    print("25% tip")
else:
    print("Please input 'bad', 'okay', 'good', or 'great'")

#Challenge 3

""" factors = input("Type a number between 1-10")
 """