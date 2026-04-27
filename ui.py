def print_header():
    print("="*50)
    print("🎲      WELCOME TO DICE ROLL GAME      🎲")
    print("="*50)


def print_round(round_no):
    print("\n" + "-"*50)
    print(f"🎯 ROUND {round_no}")
    print("-"*50)


def print_footer():
    print("="*50)
    print("🏁      GAME OVER - THANK YOU FOR PLAYING      🏁")
    print("="*50)

dice_faces = {
    1: ["     ", "  ●  ", "     "],
    2: ["●    ", "     ", "    ●"],
    3: ["●    ", "  ●  ", "    ●"],
    4: ["●   ●", "     ", "●   ●"],
    5: ["●   ●", "  ●  ", "●   ●"],
    6: ["●   ●", "●   ●", "●   ●"]
}

def print_dice(num, label):
    print(f"{label} rolled: {num}")
    print("[-----------]")
    for row in dice_faces[num]:
        print(f"[  {row}  ]")
    print("[-----------]")

def print_dice(num, label):
    print(f"\n{label} rolled: {num}")
    print("+-------+")
    for row in dice_faces[num]:
        print(f"| {row} |")
    print("+-------+")