import os,random


os.system('cls')

print(".:.:.>>>    Welcome To Guess The Word Game   <<<.:.:.\n*\*\*\    You Have ONLY 3 Chance To Win The Game    /*/*/*\n")
words_list = ['hi','hello','sun','car','moon','water']

loop_counter = 3

        

def user_input_validation (user_input):
    ''' This Method Checks IF user Input Be Not Invalid '''
    user_input = user_guess
    if user_input.isalpha() and user_input in words_list:
        return True
    else:
        return False


def ai_random_choice():
    ''' This Method Generate Random Choice Betwean Words List '''
    ai_choice = random.choice(words_list)
    return ai_choice


def answer_checker (user_choice,ai_choice):
    ''' This Method Comparison User Guess With Currect Answer '''
    global loop_counter

    if user_input_validation(user_guess) == True:
        print(15*' =')
        if user_choice == ai_choice:
            print("yes")
            return True

        else:
            print('NO')
            print(f'You have {loop_counter-1} more chances')
            print(15*' =')
            loop_counter -=1

    else:
        print(15*' =')
        print("    Please Enter Valid Choice !!!    ")
        print(f'You have {loop_counter} more chances yet')
        print(15*' =')
        

ai_choice =  ai_random_choice()

while loop_counter > 0 :
    user_guess = input(f'Enter your guess from under list elements\n{words_list}\nYour Choice is:').lower()
    if answer_checker(user_guess,ai_choice) == True:
        break
    
print(f'Currect choice was {ai_choice}')

