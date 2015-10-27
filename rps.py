"""This is a simple rock paper scissors game that you can play with the computer.
It will begin by asking the user if they would like to play rock, paper scissors. 
The user will say yes, and then a variable containing the users choice will be populated
and a variable containing the computers randomized choice will be populated."""
import random

def rps():
	
	print "Hello! Would you like to play a game of Rock/Paper/Scissors?"
	print "Please type y to play or n to quit."
	
	userChoice = raw_input()
	
	if userChoice == 'y':
		print "Yay we will play a game!"
		playGame()
	elif userChoice == 'n':
		print "I\'m sorry you don\'t want to play."
		exit()
	else:
		print "You need to type y or n. This game will now exit."
		exit()

def playGame():
	print "Do you choose rock, paper or scissors?"
	print "Type r for rock; p for paper or s for scissors. To quit type q."
	
	userChoice = raw_input()
	rNumber = random.randint(1,3)
	if rNumber == 1:
		computerChoice = 'r'
	elif rNumber == 2:
		computerChoice = 'p'
	elif rNumber == 3:
		computerChoice = 's'
	else:
		print "Random gen error."
		exit()
	
	if userChoice == computerChoice:
		print "This game is a tie!"
	elif userChoice == 'r' and computerChoice == 's':
		print "Rock beats scissors!"
		print "You win!"
	elif userChoice == 'r' and computerChoice == 'p':
		print "Rock beats paper!"
		print "You win!"
	elif userChoice == 's' and computerChoice == 'p':
		print "Scissors beat paper!"
		print "You win!"
	elif userChoice == 's' and computerChoice == 'r':
		print "Scissors lose to rock!"
		print "The computer wins!"
	elif userChoice == 'p' and computerChoice == 's':
		print "Paper loses to scissors!"
		print "The computer wins!"
	elif userChoice == 'p' and computerChoice == 'r':
		print "Paper beats rock!"
		print "You win!"
	elif userChoice == 'q':
		print "Thanks for playing!"
		exit()
	else:
		print "Please type r, p, s or q."
		exit()
		
	print "Do you want to play again?"
	
	playAgain = raw_input()
	
	if playAgain == 'y':
		playGame()
	else:
		exit()
	
	

rps()
