#import random
import random

#Make a boolean variable called KeepPlaying to track whether they want to 
#KeepPlaying and set it to true
KeepPlaying = True
#Make a game loop that continues while KeepPlaying is true
#print out a statement to welcone the user to the game 
while(KeepPlaying == true):
    print("Welcome to rock, paper, scissors. Best two out if three. Press "q" to quit")
    
    #Make variables called userScore and cpuScore to track scores, set to 0 
    userScore = 0
    cpuScore = 0
    #Make a round loop that continues while the userScore or spuScore is less
    #than 2
    while (userScore < cpuScore < 2):
        print("Choose (rock, paper or scissors)")
        if (userScore< spuScore < 2):
            break
        #use imput() to get a chouce from the user (rock, paper, scissors or q).
        #score choice in a variable. Use lower () to make the users choice
        #all lowercase
        choice = input ("please choose (Rock, paper, scissors):")
        x = input ("prompt"). lower ()
        
        #Make a list of choices, then use random choice to get a random 
        #choice for the cpu. Store the choice in a variable 
        choiceList = ["rock", "paper", "scissors"]
        cpuChoice = random.choice(choiceList)
        
        #make a if/elif/else statement to check the users input against 
        #the cpu choices
        
        
        
        if((user == "rock" and cpu == "rock") or (user == "paper" and cpu ==
        "paper") or (user == "scissors" and cpu == "scissors")):
            
            print("DRAW")
            print("User: " + str(userScore) + "CPU: " + str(cpuScore))
            
            if((user == "rocck" and cpu == "paper") or (user == "Scissors" and cpu == "Scissors")
            or (user == "rock" and cpu == "Scissors")):
            
            print("USER WO")
            print("USer: "+ str(userScore) + "CPU: " + str(cpuScore))
        
        #if the user won, add one to the users score, then print out the scores
        #print out the scoers
        #else  if it is a draw, print "DRAW", then print out the score 
        
        #else the user did not enter a accepted input, print "Not an option, try again."
        
        if(choice.lower() == 'q'):
            keepPlaying = False
        else:
            print("Not an option")
        #print out the thank you message
        print("Thanks for playing")
        #pint out who won:
        # if the userScore is 2, the the user won
        # if the cpuScore is 2, then the cpu won
        if(userScore == 2):
            print("YOU WIN")
        elif(cpuScore == 2):
            print("YOU LOSE")
        #print out the final scores
        print ("user: " + str(userScore) + "CPU: " + str(cpuScore))
            
            