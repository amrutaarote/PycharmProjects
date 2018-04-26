def print_something(name, age):
    print(" My name is " + name + " and my age is " + str(age))


print_something("Amruta" ,27)


def print_something1(myname, myage):
    print("My name is",myname,"and my age is",myage)


print_something1("Amruta" ,27)


def print_something1(firstname = "Someone", lastname = "Dont know"):
    print("My name is",firstname,"and my surname is",lastname)


print_something1("Amruta", "Arote")


def print_people(*people):
    for person in people:
        print("This is person", person)


print_people("Amruta", "Ankita","Asha" ,"Yash")


def do_math(num1 ,num2):
    return num1 + num2


math1 = do_math(5, 10)
math2 = do_math(5, 25)

print("First sum is", math1,"and the second sum is ", math2)


check = "Water"

if check == False:
    print("It is false")
elif check == "Mobile":
    print("I want it")
elif check == "Water":
    print("It's Life....")
else:
    print("Yes it's True")

