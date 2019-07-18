# print("Hello World")
# print("What's up?")

# #Datatypes
# #anything between quotes is a string
# print("There is no mistake here.")

# #integers/numbers
# print(7)
# print(7 + 9)
# print(7+9)

# print(4-8) #-4
# print(3*3) #9
# print(25/5) #5
# print(25/6) #4.something
# print(4**2) #16

# print(23%4) #3

# #functions and methods
# name = "John Jacob Jingleheimer Schmidt"
# print(name)

# print("Hello" + str(4))
# print(int("4"))
#Inputs!

# firstName = "Marek"
# lastName = input("What is your last name?\n").title()
# initials = firstName[0:1]+lastName[0:1]
# print("Welcome " + firstName + " " + lastName +"!")
# print("Your initials are: " + initials)
# age = int(input("What is your age?\n"))
# print("In 3 years you will be " + str(age+3) + " years old")
# print("You will be 65 in " + str(2019+65-age))
# if age>= 18:
#     print("You are old enough to vote")
# else:
#     print("You are not old enough to vote")
# if age>= 21:
#     print("You are old enough to drink")
# else:
#     print("You are not old enough to drink")

# try:
#     number = int(input("What's your favorite number?\n"))
#     if number%2==0:
#         print("Your number is even!\n")
#     elif number%2==1:
#         print("Your number is odd!\n")
# except ValueError:
#     print("Please enter your number as an integer")






#For Loops
# favAnimal = "Ostriches"
# print(favAnimal[4])
# print("The first letter is " + favAnimal[0])
# print("The second letter is " + favAnimal[1])
# print("The third letter is " + favAnimal[2])

# for i in range(0,len(favAnimal)):
#     ending = "th" 
#     if i == 0:
#         ending = "st"
#     elif i == 1:
#         ending = "nd"
#     elif i == 2:
#         ending = "rd"
    
#     print("The " + str(i+1)+ending+ " letter is " + favAnimal[i])
    
# numBottles = int(input("How many bottles?"))
# for i in range(0,numBottles):
#     stringBottles = str(numBottles-i)+ " bottles"
#     nextBottle = str(numBottles-i-1)+" bottles"
#     if numBottles-i==1:
#         stringBottles = "1 bottle"
#         nextBottle = "no more bottles"
#     elif numBottles-i==0:
#         stringBottles = "no more bottles"
#     print(stringBottles + " of beer on the wall, " + stringBottles +  " of beer\n Take one down and pass it around, " + nextBottle + " of beer on the wall\n")

# print("No more bottles of beer on the wall, no more bottles of beer.\n Go to the store and buy some more, " + str(numBottles) + " bottles of beer on the wall")        

        
def encode(message):
    encodedMessage = ""
    for character in message:
        if(character == " "):
            encodedMessage+=" "
        else:
            encodedMessage+=chr(ord(character)+3)
    return encodedMessage

print(encode(input("Enter your message: \n")))