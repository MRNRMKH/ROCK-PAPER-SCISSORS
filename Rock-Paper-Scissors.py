import random

print ('\/'*5)
print ("ROCK,")
print ("PAPER,")
print ("SCISSORS,")
print ('\/'*5)

user_score=0
computer_score=0

while True:
    
    while True:
       
        user_choice=input("\nChoice among (rock[r],paper[p],scissors[s]) : ")

        possible_choice = ['r' , 'p' , 's']
        computer_choice = random.choice(possible_choice)
        possible_meaning = {'r':'ROCK','p':'PAPER','s':'SCISSORS'}
        
        
        if user_choice in possible_choice:
            print('Valid')
            break
            
        else:
            print('INvalid input pls just enter (r,p,s)')

        
    print('\/\/\/\/'*5)
    print(f"user choice is _{ possible_meaning[user_choice] }_ and computer choice is _{possible_meaning[computer_choice]}_")
    print('\/\/\/\/'*5)
    
    if (user_choice == computer_choice):
        print('Tie')

    elif (user_choice == 'r' and computer_choice == 's') or (user_choice =='p' and computer_choice =='r' ) or (user_choice =='s' and computer_choice =='p'):
        print('user Win!!')
        user_score+=1

    else:
        print('computer win!!')
        computer_score+=1

    play_again = input("play again(y/n)")
    if play_again.lower()!='y':
        break
print('$$$'*20)
print(f'user Point = {user_score} ____ {computer_score} = computer Point')