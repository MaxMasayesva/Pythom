'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function.

EXAMPLE TASK:
'''
#EX) Define a function that has two parameters. Make the function add the two
#numbers together and return the result.
from Tools.demo.spreadsheet import colnum2name
from builtins import True
from email._header_value_parser import Parameter
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that has two int parameters. Make the function subtract 
#the first parameter minus the second one. Then, return the result. Now call 
#the function.
#Print what the function returns.
def subtraction(num1, num 2):
    answer = num1 - num2 
    return answer

a=2
b=1
subtraction(a,b)
print(subtraction(a,b))

#2) Define a function that has one parameter. Make the function divide the 
#parameter by 2, multiply it by 77, and then add 10,000. Return the result.
#Now call the function.
#Print what the function returns.

'''
This function divided on integer by 2 then multiplies it by 77 and then adds 100000
Then it returns and prints the answer
'''

def mathmaticalFunction(num1):
    answer = ((num1 / 2)* 77) + 10000
    print(answer)
    return answer


#3) Define a function that has two int parameters. Make the function check if 
#two numbers are equal. If they are equal, return true. If they are not equal, 
#return false. Now call the function.
#Print what the function returns.

'''
this function compares two numbers and determines if they are equal and they are equal it returns true.
then it returns and prints the answer
''' 
def areTwoNumsEqual (num1, num2):
    if(num1 == num2):
        return True
    else:
        return False
    c = 1
    d = 1
    areTwoNumsEqual(c,d)
    print(areTwoNumsEqual(c,d))


#4) Define a function that has two int parameters. Make the function
#check which parameter is bigger, and return the bigger parameter. 
#If they are the same, it should just return either parameter. Now call the 
#function.
#Print what the function returns.

'''
This function determines which paramter is larger, is larger, or if they are the same.
Then it returns the larger parameter.
'''

def whichIsLarger(par1, par2):
    if (par1>= par2):
        return par1
    else:
        return par2
a=6
b=8

whichIsLarger(a,b)
print(whichIsLarger(a,b))
#5) Define a function that has two string parameters. Make the function
#add the two strings together. And then return the combined string. Now call 
#the function.
#Print what the function returns.
def addingString(string1, string2):
    combString = string1 + string2
    return combString

a= "Two peas"
b= "In a pod"
addingString (a,b)
print(addingString(a,b))


#6) Define a function that has three int parameters. If the first number is 
#equal to the second OR the third number, return true. Else, return false. Now 
#call the function.
#Print what the function returns.
def compNums(num1, num2, num3):
    if(num1 == num2 == num3):
        return True
    else:
        returnFalse
 i = 8
 j = 4
 k = 8
 CompNums (i, j, k)
 print (compNums(i, j, k))

#7) Define a function that prints your name. It should have no parameters and 
#shouldn't return anything. Now call the function.
'''
The function run a loop, prinitng the positive integer, until the integer ends.
It does not return anything
'''
def zeroLoop(posInt):
    while (posInt > o):
        posInt = posInt - 1
        print (posInt)
        
        m = 12
        zeroLoop (m)


#8) Define a function that has one string parameter. The string should be a
#color. If that string is equal to your favorite color, it prints "That's my 
#favorite color!". If it is not, it prints "That is not my favorite color. 
#Try again.". It shouldn't return anything. Now call the function.



#9) Define a function that has one int parameter. The int should be 
#positive. If the number is not equal to zero, the function runs a loop that
#decrements the parameter by 1 and prints it each time. Now call the function.


