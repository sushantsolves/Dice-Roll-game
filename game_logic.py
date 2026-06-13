from utils import roll_dice


def play_round(user_choice):
    if not 1 <= user_choice <= 6:
        raise ValueError("Dice value must be between 1 and 6")
        
    comp_choice = roll_dice()
    return user_choice, comp_choice


def decide_winner(user, comp):
    if user > comp:
        return "user"
    elif comp > user:
        return "computer"
    else:
        return "draw"
