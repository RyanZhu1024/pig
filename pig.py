"""Ruiqi Jiang
31778261
I worked alone without help"""

import random


def print_instructions():
    """print the rules of the game"""
    print("Instructions: Pig is a very simple game. Two players take turns; on each turn, a player rolls a six-sided die (\"die\" is the singular of \"dice\") as many times as she wishes, or until she rolls a 6. Each number she rolls, except a 6, is added to her score this turn; but if she rolls a 6, her score for this turn is zero, and her turn ends. At the end of each turn, the score for that turn is added to the player's total score. The first player to reach or exceed 50 wins.")


def each_roll():
    """define the movement and score for each roll"""
    current_roll=roll()
    print(current_roll)
    current_roll_score = 0
    if current_roll == 6:
        current_roll_score = 0
    else:
        current_roll_score = current_roll

    return current_roll_score

def computer_move(computer_score, human_score):
    """define computer's move"""
    computer_current_move_score = 0
    while True:
        computer_roll = each_roll()
        if computer_roll == 0:
            computer_current_move_score = 0
            break
        else:
            computer_current_move_score += computer_roll
            if (human_score - computer_score - computer_current_move_score) >0:
                continue
            else:
                break
    print("Computer score for this move: ", computer_current_move_score)
    computer_score += computer_current_move_score
    return computer_score

def human_move(computer_score, human_score):
    """define human's move"""

    human_current_move_score = 0
    while True:
        human_roll = each_roll()
        if human_roll == 0:
            human_current_move_score = 0
            break
        else:
            human_current_move_score += human_roll
            user_respond = ask_yes_or_no("Roll again? ")
            if user_respond == True:
                continue
            else:
                break

    human_score += human_current_move_score
    return human_score


def is_game_over(computer_score, human_score):
    """compare computer and human score, to end the game or not"""

    if (computer_score >= 50) or (human_score >= 50):
        if computer_score != human_score:
            return True
        else:
            return False
    else:
        return False

def roll():
    """roll die, one time"""
    return random.randint(1,6)

def ask_yes_or_no(prompt):
    """ask the user if to roll again till to get a valid answer"""
    user_answer = input(prompt)
    while (user_answer == '') or (user_answer[0] not in ('n', 'N', 'y', 'Y')):
        user_answer = input(prompt)
    if user_answer[0] in ('y','Y'):
        return True
    else:
        return False


def show_current_status(computer_score, human_score):

    print("User's current score is: ", human_score)
    print("Computer's current score is: ", computer_score)
    difference = human_score - computer_score

    if difference > 0:
        print("You are ahead {}".format(difference))
    elif difference < 0:
        print("You are behind {}".format(abs(difference)))
    else:
        print("There is a tie.")

def show_final_results(computer_score, human_score):

    difference = human_score - computer_score
    if difference > 0:
        print("You win, by {}".format(difference))
    else:
        print("You lose, by {}".format(difference))

def main():
    computer_score = 0
    human_score = 0
    print_instructions()
    while True:
        computer_score = computer_move(computer_score,human_score)
        show_current_status(computer_score,human_score)
        human_score = human_move(computer_score,human_score)
        show_current_status(computer_score,human_score)
        if is_game_over(computer_score,human_score) == False:
            continue
        else:
            show_final_results(computer_score, human_score)
            if ask_yes_or_no("Play again? ") == True:
                main()
            else:
                break



if __name__ == '__main__':
    main()
