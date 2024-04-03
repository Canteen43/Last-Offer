import random

print("Welcome to LAST OFFER!")

new_player = input("Are you a new player? (yes/no) ")
while new_player not in ['yes', 'no']:
    new_player = input("Wrong input! Are you a new player? (yes/no)")
if new_player == "yes":
    current_player = input("Enter your name: ")
    print(f"Hello, {current_player}!")
if new_player == "no":
    current_player = input("Enter your name: ")
    print(f"Hello, {current_player}!")
# still need mechanism to put players and scores in document
print("The game begins.")
print(f"Corleone: \"This 'incident' betters stays between us, {current_player}. "
      f"I will make you an offer you cannot refuse.\"")
last_offer = round(random.random() ** 20 * 1000000 + random.random() * 100)
actual_offer = 10
answer = ""
lost = False
# print(last_offer)
while answer != "yes" and lost == False:
    answer = input(f"Corleone: \"{actual_offer}$ is my last offer! Do you take it?\" (yes/no) ")
    if answer == "no":
        new_offer = actual_offer + round(random.random() * actual_offer)
        if new_offer <= last_offer:
            actual_offer = new_offer
        else:
            lost = True
if answer == "yes":
    print(f"Corleone: \"This money buys your silence\" \nCongrats, you made {actual_offer}$!")
if lost == True:
    print(f"Corleone: \"You've always been too greedy, {current_player}\"........BANG! "
          f"\nYou got shot and lost the game.")

input("\n\nHit enter to close the game\n")