import random

def generaterandomnumber():
    randomnumber = random.randint(1, 3)
    return randomnumber

def getcomputerchoice(randomnumber):
    if randomnumber == 1:
        computerchoice = 'rock'
    elif randomnumber == 2:
        computerchoice = 'paper'
    elif randomnumber == 3:
        computerchoice = 'scissor'

    return computerchoice


def getuserchoice():
    userchoice = raw_input('Please enter your option [ rock , paper , scissor ] : ')
    return userchoice


def determinewinner(computerchoice, userchoice):
    rockmessage = 'The rock smashes the scissor'
    scissormessage = 'Scissor cuts paper'
    papermessage = 'paper wraps rock'
    tie = 'no winner'

    if computerchoice == 'rock' and userchoice == 'scissor':
        winner = 'computer'
        print(rockmessage)
    elif computerchoice == 'scissor' and userchoice == 'rock':
        winner = 'You'
        print(rockmessage)

    if computerchoice == 'scissor' and userchoice == 'paper':
        winner = 'computer'
        print(scissormessage)
    elif computerchoice == 'paper' and userchoice == 'scissor':
        winner = 'You'
        print(scissormessage)

    if computerchoice == 'paper' and userchoice == 'rock':
        winner = 'computer'
        print(papermessage)
    elif computerchoice == 'rock' and userchoice == 'paper':
        winner = 'You'
        print(papermessage)

    if computerchoice == 'rock' and userchoice == 'rock':
        winner = 'tie'
        print(tie)
    if computerchoice == 'paper' and userchoice == 'paper':
        winner = 'tie'
        print(tie)
    if computerchoice == 'scissor' and userchoice == 'scissor':
        winner = 'tie'
        print(tie)

    return winner



def main():
    randomnumber = generaterandomnumber()
    computerchoice = getcomputerchoice( randomnumber )
    userchoice = getuserchoice()
    print('The computer chose', computerchoice)
    winner = determinewinner(computerchoice, userchoice)


    if winner != 'no winner':
        print('result ->', winner, '-- WON')
        winner = main()
    while winner == 'no winner':
        print('Both chose same')
        winner = main()
main()

