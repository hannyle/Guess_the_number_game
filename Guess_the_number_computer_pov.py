def computer_game():
    
    min_num, max_num=map(int,input('What range is your number in? \n').split(','))
    
    if max_num<min_num:
        print('First number should be less than second number')
        
    else:
        print("Please asnwer 'yes', 'higher', 'lower'")
        max_num = max_num - 1
        while min_num<=max_num:
            guess=(min_num+max_num)//2
            answer=input('Is your number ' + str(guess) + '?')
            if answer=='yes':
                print('Bingo!')
                break
            elif answer=='lower':
                max_num=guess - 1
            elif answer=='higher':
                min_num=guess+1
            
        

    
    

    
