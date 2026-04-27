from utils import roll_dice


def play_round(user_choice):
    comp_choice = roll_dice()
    return user_choice, comp_choice


def decide_winner(user, comp):
    if user > comp:
        return "user"
    elif comp > user:
        return "computer"
    else:
        return "draw"