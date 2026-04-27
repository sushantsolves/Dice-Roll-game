def show_score(user_score, comp_score, draws):
    print("\n+----------------------------------+")
    print("|            SCOREBOARD            |")
    print("+----------------------------------+")
    print(f"| User Wins      : {user_score:<16}|")
    print(f"| Computer Wins  : {comp_score:<16}|")
    print(f"| Draws          : {draws:<16}|")
    print("+----------------------------------+")


def final_result(user_score, comp_score):
    print("\n🎉 FINAL RESULT 🎉")
    if user_score > comp_score:
        print("😎 You crushed the computer! Well played!")
    elif comp_score > user_score:
        print("😂 Computer wins! Better luck next time!")
    else:
        print("🤝 It's a draw! What a close match!")