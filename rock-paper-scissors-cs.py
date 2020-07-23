# Courtney Stowers
# July 22, 2020
# My first Python project after completing freeCodeCamp beginner course on Youtube: https://www.youtube.com/watch?v=rfscVS0vtbw

import random  # use random module for computer to randomly select rock, paper, or scissors

computer = ("rock", "paper", "scissors")  # random option list for computer's game selections


def rock_paper_scissors():
    player_select = input(
        "Enter rock, paper, or scissors to begin game: ")  # prompt for player to enter their selection
    selection = str(random.sample(computer, 1))[1:-1]  # computer's random selection, remove brackets
    computer_select = selection.replace("'", "")  # remove quotation marks from selection
    if player_select == "rock" and computer_select == "scissors":
        print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
            computer_select) + "\nYou win! Congratulations!")  # str.strip removes quotes from output
    elif player_select == "rock" and computer_select == "rock":
        print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
            computer_select) + "\nTie! Try again!")
    elif player_select == "paper" and computer_select == "rock":
        print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
            computer_select) + "\nYou win! Congratulations!")
    elif player_select == "paper" and computer_select == "paper":
        print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
            computer_select) + "\nTie! Try again!")
    elif player_select == "scissors" and computer_select == "paper":
        print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
            computer_select) + "\nYou win! Congratulations!")
    elif player_select == "scissors" and computer_select == "scissors":
        print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
            computer_select) + "\nTie! Try again!")
    else:
        print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
            computer_select) + "\nYou lose! Try again!")


# Play game:
rock_paper_scissors()
