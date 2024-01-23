__author__  = "Simon_Wristel"
__version__ = "1.0.0"
__email__   = "Simon.wristel@elev.ga.ntig.se"


import os #för att kunna sudda
from colors import bcolors #för att kunna ha olika färger
os.system("cls")
print(bcolors.GREEN+"""
       _________________________________________________________
      |                                                         |
      |_-_-_-_-_-_-_Skriv en lista me dina kompisar_-_-_-_-_-_-_|
      |_________________________________________________________|""") 
my_list=[] #här skapas en lista

def add_list(addition): #en funktion som används för att lägga till ett namn i listan
    my_list.append(addition)

def remove_list(remove): #en funtkion som används för att ta bort ett namn från listan
    my_list.pop(remove)

def edit_list(edit, newname): #en funktion som används för att redigera namn i listan
    my_list[edit]=newname


while True:
    input_1=(input(bcolors.CYAN+"\nSkirv in ett namn eller en position för att förändra något i listan: "))
    if input_1.isdigit(): # menar att om man bara skriver siffror så funkar det men annars så stängs programmet av
        select=int(input_1)
        if select > 0 and select<=len(my_list):
            action = input("vill du ta bort(T) eller redigera(R) eller avsluta(Q)")
            pos = action.upper() # ska kunna skriva både stora och små bokstäver
            if pos == "T":
                remove_list(select-1)
            elif pos == "R":
                new_name=input(f"Skriv in det nya namnet för {my_list[select-1]}: ")
                edit_list(select-1, new_name)
            elif pos == "Q":
                quit
        os.system("cls")
        x=0
        print(bcolors.BOLD+"--DIN LISTA--") #detta är rubriken i listan
        for i in my_list:
            x+=1
            print(f"{x}) { i}")

        print(bcolors.BLUE+"du har", len(my_list), "namn i din lista") #printar ut nummret och namnet i listan i blå färg
    else:
        (add_list(input_1)) #lägger in namnet i listan (sparar den)
            


        os.system("cls") #suddar allt du skriver ut
        x=0
        print(bcolors.BOLD+"-_-_-|_LISTAN_|-_-_-") #detta är namnet på listan som alltid kommer vara längst upp
        for i in my_list: # en for loop
            x+=1
            print(f"{x}) { i}")
        print(bcolors.BLUE+"du har", len(my_list), "namn i din lista") #printar ut nummret och namnet i listan i blå färg

