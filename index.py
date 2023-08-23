from colorama import Fore
user_input_list =[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
inputStr ='X'
def user_input(user_input_list_val,inputStr):
    try: 
        default_list =user_input_list_val   
        display_patern(default_list)
        if is_all_index_filled(default_list)==False:
            row =input(f'{Fore.BLUE}Please choose a ROW from 1,2,3 to insert {Fore.RED}{inputStr}!!{Fore.RESET}\n')
            if validate(row):
                col = input(f'{Fore.BLUE}Please choose a COLUMN from 1,2,3 to insert {Fore.RED}{inputStr}!!{Fore.RESET}\n')
                if validate(col):
                    if check_value_exist_in_index(default_list,int(row)-1,int(col)-1):
                        default_list[int(row)-1][int(col)-1]=inputStr
                        tempInput =inputStr
                        if tempInput=='X':
                            inputStr='O'
                        else:
                            inputStr='X' 
                        find_game_winner(default_list,inputStr)       
                    else:
                        display_error(f"{Fore.RED}Sorry!!. Already  added value in this box (row-{int(row)},column-{int(col)})!{Fore.RESET}",default_list,inputStr)    
                else:
                    display_error(f"{Fore.RED}invalid selection!{Fore.RESET}",default_list,inputStr)    
            else:
                display_error(f"{Fore.RED}invalid selection!{Fore.RESET}",default_list,inputStr)
        else:
            user_input(user_input_list,inputStr)

    except Exception as e:
        display_error(f"{Fore.RED}invalid selection!{Fore.RESET}",user_input_list,"X")

def display_patern(default_list):
    print(" | ".join(default_list[0]))
    print("--|---|--")
    print(" | ".join(default_list[1]))
    print("--|---|--")
    print(" | ".join(default_list[2]))

def is_all_index_filled(default_list):
    merge_list = default_list[0]+default_list[1]+default_list[2]
    return merge_list.count("X")+merge_list.count('O')==9

def validate(value):
    if not value.isdigit():
        return False
    x=range(0,3)
    return int(value)-1 in x

def check_value_exist_in_index(default_list,row,col):
    return default_list[row][col] == " "

def find_game_winner(default_list,inputStr="X"):
    winner=""
    dummyList=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    possibleWinEntries=["".join([default_list[0][0],default_list[0][1],default_list[0][2]]),
                        "".join([default_list[1][0],default_list[1][1],default_list[1][2]]),
                        "".join([default_list[2][0],default_list[2][1],default_list[2][2]]),
                        "".join([default_list[0][0],default_list[1][0],default_list[2][0]]),
                        "".join([default_list[0][1],default_list[1][1],default_list[2][1]]),
                        "".join([default_list[0][2],default_list[1][2],default_list[2][2]]),
                        "".join([default_list[0][0],default_list[1][1],default_list[2][2]]),
                        "".join([default_list[0][2],default_list[1][1],default_list[2][0]])
                        ]
    for item in possibleWinEntries:
        if item=="XXX":
            winner=item[0]
            break
        elif item=="OOO":
            winner=item[0]
            break
        else:
            pass
    
    if winner:
        display_patern(default_list)
        display_message(f'{Fore.GREEN}{winner} wins the game..Game Over!!{Fore.RESET}')
        display_message("Restarting game...!!")
        user_input(dummyList,"X")
        return
    elif is_all_index_filled(default_list) and not winner:
        display_patern(default_list)
        display_message(f'{Fore.YELLOW}Game Drawn!!{Fore.RESET}')
        display_message("Restarting game...!!")
        user_input(dummyList,"X")
        return   
    else:
        user_input(default_list,inputStr)
        return
     
def display_error(message,default_list,inputStr):
    print(message)
    user_input(default_list,inputStr)

def display_message(message):
    print(message)
user_input(user_input_list,inputStr)
    