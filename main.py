import msvcrt
import os
from colorama import Fore as F, init

init(autoreset=True)

def menu():
    how_to_use_text = f"""{F.CYAN}
Welcome to the Sensitivity Adjustment Tool!
-----------------------------------------

This tool allows you to adjust your sensitivity by calculating a lower and higher sensitivity based on your input.

How to Use:
1. Enter your current sensitivity when prompted.
2. Choose an option:
- [1] Low: Calculates a sensitivity that is half of your original.
- [2] High: Calculates a sensitivity that is 150% of your original.
- [0] Exit: Quits the tool.
3. Repeat steps 1 and 2 until you find a sensitivity that suits you.

Note: Make sure to enter a valid numerical value for your sensitivity.

Enjoy gaming with your optimized sensitivity!
"""
    print(how_to_use_text)
    print(f"{F.YELLOW}Press any key to continue...")
    msvcrt.getch()
    os.system('cls')
    main()

def main():
    text = f"""{F.CYAN}
██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗████████╗███████╗███████╗███╗   ██╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔════╝████╗  ██║██╔════╝
██████╔╝█████╗  ██████╔╝█████╗  █████╗  ██║        ██║   ███████╗█████╗  ██╔██╗ ██║███████╗
██╔═══╝ ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ██║        ██║   ╚════██║██╔══╝  ██║╚██╗██║╚════██║
██║     ███████╗██║  ██║██║     ███████╗╚██████╗   ██║   ███████║███████╗██║ ╚████║███████║
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝

                {F.GREEN}-by Saay
          """
    print(text)
    
    try:
        sens = float(input("Enter your sens >>>> "))
        calc(sens)
    except:
        print(f"{F.RED}\nInvalid input, exiting...")
        exit()

def calc(sens):
    print(f"""
          
          [1] Low: {calculate_low(sens)}
          [2] High: {calculate_high(sens)}
          [0] Exit
          
          """)
    choice = int(input("Choose an option >>> "))
    if choice == 1:
        sens = calculate_low(sens)
        calc(sens)
    elif choice == 2:
        sens = calculate_high(sens)
        calc(sens)
    elif choice == 0:
        print(f"{F.RED}Exiting...")
        exit()
    else:
        print(f"{F.RED}Invalid input, exiting...")
        exit()

def calculate_high(sens):
    return round(sens*1.5, 3)

def calculate_low(sens):
    return round(sens/2, 3)

if __name__ == "__main__":
    menu()
