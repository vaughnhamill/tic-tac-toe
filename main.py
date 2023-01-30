import random

LOGO = """ 
        88                                                              
  ,d    ""              ,d                            ,d                
  88                    88                            88                
MM88MMM 88  ,adPPYba, MM88MMM ,adPPYYba,  ,adPPYba, MM88MMM ,adPPYba,  ,adPPYba, 
  88    88 a8"     ""   88    ""     `Y8 a8"     ""   88   a8"     "8a a8P_____88
  88    88 8b           88    ,adPPPPP88 8b           88   8b       d8 8PP""""""" 
  88,   88 "8a,   ,aa   88,   88,    ,88 "8a,   ,aa   88,  "8a,   ,a8" "8b,   ,aa  
  "Y888 88  `"Ybbd8"'   "Y888 `"8bbdP"Y8  `"Ybbd8"'   "Y888 `"YbbdP"'  `"Ybbd8"'                                                                                 
 """

print(LOGO)

user_shape = ""
bot_shape = ""
a1 = " "
a2 = " "
a3 = " "
b1 = " "
b2 = " "
b3 = " "
c1 = " "
c2 = " "
c3 = " "
spots = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
user_spots = []
bot_spots = []
winning_combos = [
    ["a1", "b1", "c1"],
    ["a2", "b2", "c2"],
    ["a3", "b3", "c3"],
    ["a1", "a2", "a3"],
    ["b1", "b2", "b3"],
    ["c1", "c2", "c3"],
    ["a1", "b2", "c3"],
    ["a3", "b2", "c1"]
]
turns = 9
initial_board = f"""
            1   2   3
        a     |   | 
           -----------
        b     |   | 
           -----------
        c     |   | 
    """

# Pick shape
shape = True
while shape:
    user_shape_pick = input("Pick your shape ('X' or 'O'): ").upper()
    if user_shape_pick == "X":
        user_shape = "X"
        bot_shape = "O"
        shape = False
    elif user_shape_pick == "O":
        user_shape = "O"
        bot_shape = "X"
        shape = False
    else:
        print("Please pick from the given shapes.")

# Game
print(initial_board)
game = True
while game:
    # User pick
    user_spot = input("Pick a spot (i.e. a1 or c2): ")
    if user_spot in spots:
        for spot in spots:
            if user_spot == spot:
                locals()[spot] = user_shape
                user_spots.append(spot)
                spots.remove(spot)
                turns -= 1

                # Bot pick
                if turns > 1:
                    bot_spot = random.choice(spots)
                    locals()[bot_spot] = bot_shape
                    bot_spots.append(bot_spot)
                    spots.remove(bot_spot)
                    turns -= 1
    else:
        print("Please pick another spot.")

    board = f"""
            1   2   3
        a   {a1} | {a2} | {a3}
           -----------
        b   {b1} | {b2} | {b3}
           -----------
        c   {c1} | {c2} | {c3}
        """

    print(board)

    # Checks for winner
    for win in winning_combos:
        if all(spots in user_spots for spots in win):
            print("Game over! You win!")
            exit()
    for win in winning_combos:
        if all(spots in bot_spots for spots in win):
            print("Game over! The bot won.")
            exit()
    for win in winning_combos:
        if turns == 0 and not all(spots in user_spots for spots in win) and not all(spots in bot_spots for spots in win):
            print("Game over! It's a draw.")
            exit()
