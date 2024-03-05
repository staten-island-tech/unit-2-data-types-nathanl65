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





""" x = input("Give me a sentence: ")
words_list = x.split( )
print(f"Word count:{(len(words_list))}")
y = (len(words_list)) """


"""  #Challenge 1

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
    print("even") """


""" #Challenge 2

bill = float(input("Cost:"))
service = input("How was the service? ")
if service == "bad":
    print("0% tip")
    bill = bill
elif service == "okay":
    print("15% tip")
    bill = bill *1.15
elif service == "good":
    print("20% tip")
    bill = bill *1.2
elif service == "great":
    print("25% tip")
    bill = bill *1.25
print(bill) """


""" #Challenge 3

number = int(input("Enter a number:"))
def factor(x):
    for i in range(1, x + 1):
        if x % (i) == 0:
            print(i)
factor(number) """


#Challenge 4
def factors(x):
    factors_list = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors_list.append(i)
    return factors_list
number1 = int(input("Enter a number: "))
factors_number1 = factors(number1)
number2 = int(input("Enter another number: "))
factors_number2 = factors(number2)
gcf = 1
for num in factors_number1:
    if num in factors_number2 and gcf < num:
        gcf = num
print("The GCF is:", gcf)
