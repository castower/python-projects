# Courtney Stowers
# July 23, 2020
# Rock, Paper, Scissors with loop and case insensitivity
# My second Python project after completing freeCodeCamp
# beginner course on Youtube: https://www.youtube.com/watch?v=rfscVS0vtbw

import random  # use random module for computer to randomly select rock, paper, or scissors

computer = ("rock", "paper", "scissors")  # random option list for computer's game selections

print( "\nWelcome to rock, paper, scissors!\n"
       "\nRules: "
       "\nRock beats Scissors "
       "\nScissors beats Paper"
       "\nPaper beats Rock"
       "\nTry to outsmart the computer with a winning selection!\n"
       "\nGood luck!")


def rock_paper_scissors():
    player_select = input(
        "\nEnter rock, paper, or scissors to begin game: ")  # prompt for player to enter their selection
    selection = str(random.sample(computer, 1))[1:-1]  # computer's random selection, remove brackets
    computer_select = selection.replace("'", "")  # remove quotation marks from selection
    play_again = "yes"
    while play_again == "yes":
        if player_select.lower() != "rock" and player_select.lower() != "paper" and player_select.lower() != "scissors":
            print("Wrong input! Please enter rock, paper, or scissors and try again!")
        elif player_select.lower() == "rock" and computer_select == "scissors":
            print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
                computer_select) + "\nYou win! Congratulations!")  # str.strip removes quotes from output
        elif player_select.lower() == "rock" and computer_select == "rock":
            print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
                computer_select) + "\nTie! Try again!")
        elif player_select.lower() == "paper" and computer_select == "rock":
            print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
                computer_select) + "\nYou win! Congratulations!")
        elif player_select.lower() == "paper" and computer_select == "paper":
            print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
                computer_select) + "\nTie! Try again!")
        elif player_select.lower() == "scissors" and computer_select == "paper":
            print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
                computer_select) + "\nYou win! Congratulations!")
        elif player_select.lower() == "scissors" and computer_select == "scissors":
            print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
                computer_select) + "\nTie! Try again!")
        else:
            print("Player selection: " + str(player_select) + "\nComputer selection: " + str.strip(
                computer_select) + "\nYou lose! Try again!")
        play_again = input("\nDo you want to try again? Enter yes or no: ")
        if play_again.lower() == "yes":
            rock_paper_scissors()
            break
        elif play_again.lower() == "no":
            print("Aw, okay :( Hope you play again soon!")
            break
        elif play_again.lower() != "yes" and play_again.lower() != "no":
            print("Wrong input! Please enter yes or no.")
            play_again = input("\nDo you want to try again? Enter yes or no: ")
            if play_again.lower() == "yes":
                rock_paper_scissors()
                break
            elif play_again.lower() == "no":
                print("Aw, okay :( Hope you play again soon!")
                break
            else:
                print("Wrong input! Try again later. Goodbye!")
                break
        else:
            break


# Play game:
rock_paper_scissors()
