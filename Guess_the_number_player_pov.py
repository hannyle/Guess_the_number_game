import random, math
from math import log, ceil
def player_game():
    play = 'yes'
    while play=='yes':
    
        print ("Please enter 2 values for range: \n")
        first_num, second_num=map(int,input().split(','))
        if second_num<first_num:
            print('First number should be less than second number')
        else:
            random_num=random.randrange(first_num, second_num)
            total_tries=ceil(log(second_num,2))
            
            print('I have picked a number between ' + str(first_num) + ' and ' + str(second_num) + " , what's your guess? \n" + "You have " + str(total_tries) + " left.")

            guess = int(input())
            tries=1
            
            while(tries<=total_tries):
                if guess==random_num:
                    print('Bingo!')
                    break       

                elif guess<random_num:
                    print('This number is lower than the number I have in mind! Next try? \n'+ 'You have ' + str(total_tries-tries) +' tries left.')
                      
                    
                    

                elif guess>random_num:
                    print('This number is higher than the number I have in mind! Next try? \n'+ 'You have ' + str(total_tries-tries) +' tries left.')
                      

                 

                guess=int(input())
                tries+=1
                    
            if(tries>total_tries):
                    
                print('You lose!\n')
            print('Play again? yes/no')
            play=input()
        
            
                

        
    





