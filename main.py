import random
import pandas as pd
import os

def ask_question (question, answers=["yes", "no"]):
    answer = input(f"{question} {answers} ")
    while answer not in answers:
        answer = input("Wrong Input!\n" + f"{question} {answers} ")
    return answer
def enter_statement (statement):
    input(statement)
    pass

if os.path.exists('last_offer_history.csv'):
    df = pd.read_csv('last_offer_history.csv')
else:
    df = pd.DataFrame(columns=['name', 'games_total', 'games_lost', 'bribe_max', 'bribe_total', 'code'])

enter_statement("Welcome to LAST OFFER! (Hit enter to advance) ")
new_player = ask_question("Are you a new player?")
if new_player == "yes":
    current_player = input("Enter your name: ")
    while df['name'].isin([current_player]).any():
        current_player = input("That name is taken. Use another: ")
    code = input("Set your secret code for future games: (might go online) ")
    new_row = {'name': current_player, 'games_total': 0, 'games_lost': 0,
               'bribe_max': 0, 'bribe_total': 0, 'code': code}
    df.loc[len(df)] = new_row
if new_player == "no":
    current_player = input("Enter your name: ")
    while ~df['name'].isin([current_player]).any():
        current_player = input("That player does not exist. Use another: ")
    code = input("Enter your secret code: ")
    while code != df.loc[df['name'] == current_player, 'code'].item():
        code = input("Wrong code. Enter your code again: ")

enter_statement(f"Hello, {current_player}!")
def play_game():
    enter_statement("The game begins.")
    enter_statement(f"Corleone: \"This 'incident' betters stays between us, {current_player}.\"")
    enter_statement(f"Corleone: \"I will make you an offer you cannot refuse.\"")
    last_offer = round(random.random() ** 20 * 1000000 + random.random() * 100)
    current_offer = 10
    answer = "no"
    lost = False
    # print(last_offer)
    while answer == "no" and lost == False:
        answer = ask_question(f"Corleone: \"{current_offer}$ is my last offer! Do you take it?\"")
        if answer == "no":
            new_offer = current_offer + round(random.random() * current_offer)
            if new_offer <= last_offer:
                current_offer = new_offer
            else:
                lost = True
    df.loc[df['name'] == current_player, 'games_total'] += 1
    if answer == "yes":
        df.loc[df['name'] == current_player, 'bribe_total'] += current_offer
        if current_offer > df.loc[df['name'] == current_player, 'bribe_max'].item():
            df.loc[df['name'] == current_player, 'bribe_max'] = current_offer
        enter_statement(f"Corleone: \"This money buys your silence\"")
        enter_statement(f"Corleone: \"I better not see you around here no more.\"")
        enter_statement(f"Congrats, you made {current_offer}$!")
    if lost == True:
        df.loc[df['name'] == current_player, 'games_lost'] += 1
        enter_statement(f"Corleone: \"You've always been too greedy...\"")
        enter_statement(f"...")
        enter_statement(f"BANG!")
        enter_statement(f"The godfather shot you and you lost the game.")
    df.to_csv('last_offer_history.csv', index=False)

    # Displaying score table
    enter_statement(f"...")
    enter_statement(f"Enter to see score table. ")
    df_show = df.copy()
    df_show["Mobster"] = df["name"]
    df_show["Lost Games"] = (df["games_lost"] / df["games_total"]).apply(lambda x: f"{x:.0%}")
    df_show["Highest Bribe"] = df["bribe_max"].apply(lambda x: f"{x:,.0f}$")
    df_show["Bribe-Per-Game"] = df["bribe_total"] / df["games_total"]
    df_show.drop(columns=['name', 'games_total', 'games_lost', 'bribe_max', 'bribe_total', 'code'], inplace=True)
    df_show.sort_values(by="Bribe-Per-Game", ascending=False, inplace=True)
    print(df_show.head(10).to_string(index=False))
    print("")

wants_play = ask_question("Do you want to play a game? ")
while wants_play == "yes":
    play_game()
    wants_play = ask_question("Do you want to play another round? ")
enter_statement("\nEnter to exit. ")
"""
"""
