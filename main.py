from ui import print_header, print_round, print_footer, print_dice
from game_logic import play_round, decide_winner
from scoreboard import show_score, final_result

print_header()

rounds = int(input("Enter number of rounds: "))

user_score = 0
comp_score = 0
draws = 0

for i in range(1, rounds+1):
    print_round(i)

    while True:
        try:
            user_choice = int(input("Pick a number (1-6): "))
            if 1 <= user_choice <= 6:
                break
            else:
                print("Enter a number between 1 and 6!")
        except:
            print("Invalid input!")

    user, comp = play_round(user_choice)

    print_dice(user, "You")
    print_dice(comp, "Computer")

    result = decide_winner(user, comp)

    if result == "user":
        print("🔥 You win this round!")
        user_score += 1
    elif result == "computer":
        print("💻 Computer wins this round!")
        comp_score += 1
    else:
        print("😐 It's a draw!")
        draws += 1

show_score(user_score, comp_score, draws)
final_result(user_score, comp_score)
print_footer()
