# user will define the inverval
# computer will try the guess the number in minimum steps
import random

# generate interval
def generateInterval():
    while True:
        i = input("What is your minmum?\n")
        try:
            i = int(i)
            break
        except:
            print("You should enter a number. (1,2,35,68...)")
            
    while True:       
        j = input("What is your maximum?\n")
        try:
            j = int(j)
            break
        except:
            print("You should enter a number. (1,2,35,68...)")
        
    return i,j

def computerGuess(i: int, j: int):  
    # generating random input for computer
    a = random.randint(i, j)
    counter = 1
    while True:
         cond = input(f"Is your number {a}? enter 'y' for yes 'n' for no.\n")
         if cond == 'y':
             print(f"I found it! It took me {counter} attempts!\n")
             break
         elif cond =='n':
             cond1 = input("Lower or higher? Enter 'h' for higher 'l' for lower.\n")
             if cond1 == 'h':
                 a = int(a)
                 i = a
                 a = int((int(j) - a) / 2 + a)
                
                 
             elif cond1 == 'l':
                 a = int(a)
                 j = a
                 a = int(a - (a - int(i)) / 2)           
             else:
                 print("You should enter y or no!\n")
         else:
             print("You should enter y or no!\n")
         counter += 1
def main():
    print("Welcome to the guessing game!\n")
    i ,j = generateInterval()
    computerGuess(i, j)

main()


