#Make a variable called score to keep track of the correct answers. And set
#it to 0.
score=0
#Ask the user question one. And store the users answer.
print("1. What is the powerhouse of the cell")
question1 = input("Enter a letter. A) mitochondria B)nucleus C)rybosome")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if question1.upper == "A":
    score= score + 1
    print ("Correct")

else:
    print("Incorrect, the correct answer is A")
#Ask the user question two. And store the users answer.
print("2. How many hours are in a day")
question2 = input ("enter a letter. A) 16 B)20 C)24")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if question2.upper() == "c":
    score = score + 1
    print ("correct")
#Ask the user question three. And store the users answer.
print("In Y=MX+B what does m stand for")
question3 = input("enter a letter. A) Slope B) Output C) IDK")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if question3.upper() == "A":
    score=score + 1
    print("Correct")
    
    Else: 
    Print("Incorrect, the answer is A")
#Ask the user question four. And store the users answer.
print ("4. In english a person, place or thing is called")
question4 = input("Enter a letter. A) Verb B) Adjective C) Noun")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if question4.upper() == "C":
    score = score + 1
    print("Correct")

else:
    print("Incorrect, the correct answer is C")
#Calculate the percentage the user got. And store it in a variable called p
P = (score / 4)= 100
#Print out the users score: "You got a [score]/4. Or a [p]%."
print("you got a" + str(score) + "/4. or a" + str(p) + "%")