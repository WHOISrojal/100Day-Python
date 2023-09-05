import random 

Rock = "Rock"
Paper = "Paper"
Scissor = "Scissor"
image = [Rock,Paper,Scissor]
uchoice = int(input("Enter 0 for rock, 1 for paper, and 2 for scissor\n"))
print("You chose")
print(image[uchoice])

pcchoice = random.randint(0,2)
print("\nComputer chose")
print(image[pcchoice])

if uchoice >=3 or uchoice < 0:
    print("Invalid number. You lose")
elif uchoice == 0 and pcchoice == 2:
    print("\nYou win")
elif pcchoice == 0 and uchoice == 2:
    print("\nYou lose")
elif pcchoice > uchoice:
    print("\nYou lose")  
elif uchoice > pcchoice:
    print("\nYou win")
elif uchoice == pcchoice:
    print("\nDraw")

