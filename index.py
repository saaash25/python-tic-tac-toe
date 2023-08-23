from colorama import Fore
import re
import time
import os

user_input_list =['{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}']
inputStr ='X'

def user_input(user_input_list_val,inputStr):
    try: 
        default_list =user_input_list_val   
        display_patern(default_list)
        if is_all_index_filled(default_list)==False:
            position =input(f'{Fore.BLUE}Enter a position from 1-9 to insert {Fore.RED}{inputStr}!!{Fore.RESET}\n')
            if validate(position):
                if check_value_exist_in_index(default_list,int(position)-1):
                    default_list[int(position)-1]=f' {inputStr} '
                    tempInput =inputStr
                    if tempInput=='X':
                        inputStr='O'
                    else:
                        inputStr='X' 
                    find_game_winner(default_list,inputStr)       
                else:
                    display_error(f"{Fore.RED}Sorry!!. Already  added value in this box (position-{int(position)})!{Fore.RESET}",default_list,inputStr)    
            else:
                display_error(f"{Fore.RED}invalid selection!{Fore.RESET}",default_list,inputStr)
        else:
            user_input(user_input_list,inputStr)

    except Exception as e:
        print(e)
        display_error(f"{Fore.RED}something went wrong!!{Fore.RESET}",user_input_list,"X")
        do_start_game()

def display_patern(default_list):
    print("   |   | ")
    print("|".join(default_list[0:3]))
    print("   |   | ")
    print("---|---|---")
    print("|".join(default_list[3:6]))
    print("   |   | ")
    print("---|---|---")
    print("   |   | ")
    print("|".join(default_list[6::]))
    print("   |   | ")

def is_all_index_filled(default_list):
    return default_list.count(" X ")+default_list.count(' O ')==9

def validate(value):
    if not value.isdigit():
        return False
    x=range(0,9)
    return int(value)-1 in x

def check_value_exist_in_index(default_list,position):
    x = re.search(r"{[1-9]}",default_list[position])
    return x != None

def find_game_winner(default_list,inputStr="X"):
    winner=""
    possibleWinEntries=[default_list[0].strip()+default_list[1].strip()+default_list[2].strip(),
                        default_list[3].strip()+default_list[4].strip()+default_list[5].strip(),
                        default_list[6].strip()+default_list[7].strip()+default_list[8].strip(),
                        default_list[0].strip()+default_list[3].strip()+default_list[6].strip(),
                        default_list[1].strip()+default_list[4].strip()+default_list[7].strip(),
                        default_list[2].strip()+default_list[5].strip()+default_list[8].strip(),
                        default_list[0].strip()+default_list[4].strip()+default_list[8].strip(),
                        default_list[2].strip()+default_list[4].strip()+default_list[6].strip()
                        ]
    for item in possibleWinEntries:
        if item=="XXX" or item=="OOO":
            winner=item[0]
            break
        else:
            pass
    
    if winner:
        display_patern(default_list)
        display_message(f'{Fore.GREEN}{winner} wins the game..Game Over!!{Fore.RESET}')
        do_start_game()
        return
    elif is_all_index_filled(default_list) and not winner:
        display_patern(default_list)
        display_message(f'{Fore.YELLOW}Game Drawn!!{Fore.RESET}')
        do_start_game()
        return   
    else:
        user_input(default_list,inputStr)
        return
     
def display_error(message,default_list,inputStr):
    print(message)
    user_input(default_list,inputStr)

def display_message(message):
    print(message)

def display_initial_messages(initial_list,initialValue):
    os.system('clear')
    print("Starting game...!!")
    while True:
        time.sleep(1)
        print("-----------------------------")
        print("1. 'X' for player 1 and 'O' for player 2")
        print("2. There will be boxes 1-9. each user choose 1 from this to insert their value")
        print("3. Cant't insert values if already a value is there in a box")
        print("------------------------------")
        user_input(initial_list,initialValue)

def do_start_game():
    start="WRONG"
    while start.lower()!="y" or start.lower()!="n":
        start=input("Want to play again?\nEnter Y for Yes OR N for No\n")
        if start.lower()=="y":
            display_initial_messages(['{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}'],'X')
        elif start.lower()=="n":
            exit()
        else:
            print(f'{Fore.RED}Accept only Y or N{Fore.RESET}')    

display_initial_messages(user_input_list,inputStr)

     