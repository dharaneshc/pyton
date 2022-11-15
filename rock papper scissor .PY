import random
wins = 0
losses = 0
ties = 0
while True:
 print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
 while True:
    print('Enter your move: (r)ock (p)aper (s)cissors ')
    a = input()
    if a == 'r' or a == 'p' or a == 's':
        break

 randomNumber = random.randint(1, 3)
 if randomNumber == 1:
    computerMove = 'r'
    print('ROCK')
 elif randomNumber == 2:
    computerMove = 'p'
    print('PAPER')
 elif randomNumber == 3:
    computerMove = 's'
    print('SCISSORS')

 if a == computerMove:
    print('It is a tie!')
    ties = ties + 1
 elif a == 'r' and computerMove == 's':
    print('You win!')
    wins = wins + 1
 elif a == 'p' and computerMove == 'r':
    print('You win!')
    wins = wins + 1
 elif a == 's' and computerMove == 'p':
    print('You win!')
    wins = wins + 1
 elif a== 'r' and computerMove == 'p':
    print('You lose!')
    losses = losses + 1
 elif a == 'p' and computerMove == 's':
    print('You lose!')
    losses = losses + 1
 elif a == 's' and computerMove == 'r':
    print('You lose!')
    losses = losses + 1
