import random, time, os
retry = "y"
def roll_dice(dice_num, dice_l, dice):
    for d in range(0, dice_num):
        if dice_l[d] != 1:
            if dice_l[d] == 2 and dice_rolls != 0:
                print("locked")
            else:
                dice[d] = random.randint(1,6)
    return dice
def of_a_kind(num, m, id, score_set, score_points):
    k = 0
    if score_set[id] != 1:
        score_points[id] = 0
        for pdice in range(0, dice_num):
            counter = 0
            for pdice_t in range(0, dice_num):
                if dice[pdice] == dice[pdice_t]:
                    counter = counter + 1
            if counter == num:
                k = dice[pdice]
        if k != 0:
            score_points[id] = m * k
    return score_points
def bonus(id, a, b, r):
    if score_points[id] != 50:
        counter = 0
        score_set[id] = 2
        for b in range(a, b):
            if score_set[b] == 1 and score_points[b] != 0:
                counter = counter + 1
        if counter == r:
            score_points[id] = 50
    return score_points

while retry != "n":     
    dice_num = 5     
    max_rolls = 3   #I've decided not to make them customisable (the top variable).
    score_num = 13
    score_points = [0] * score_num
    score_name = [0] * score_num
    score_set = [0] * score_num
    score_total = 0
    counter = 0
    set_c = 0
    q = ""
    quitter = 0
    dice_rolls = 0
    dice = [0] * dice_num
    dice_l = [0] * dice_num
    dice_l_n = 0
    table_choose = 0
    score_choose = 0

    menu = [0] * 3
    os.system('cls') #only works with windows
    print("Welcome to:")
    print("************************************")
    print("*__   __    _     _                *")
    print("*\ \ / /_ _| |__ | |_ _______  ___ *")
    print("* \ V / _` | '_ \| __|_  / _ \/ _ \*")
    print("*  | | (_| | | | | |_ / /  __/  __/*")
    print("*  |_|\__,_|_| |_|\__/___\___|\___|*")
    print("************************************")
    input("Press enter to play ") 

    while menu[0] != "":
        os.system('cls')
        print("Menu:")
        print("-Game Mechanics-")
        print("1 - Change non-unlockable dice amount -")
        print(f"    Currently set at {dice_l_n} dice")
        print("2 - Change max dice roll amount -")
        print(f"    Currently set at {max_rolls} rolls")
        print("A game guide is found elsewhere (documentation).")
        print("3 - There's nothing here.")
        menu[0] = input("Enter a number to an action or press enter to proceed: ")

        if menu[0] == "1": #Change non-unlockable
            while menu[1] == 0:
                menu[1] = 0
                os.system('cls')
                print("Change non-unlockable dice amounts")
                print("A game mechanic where if a roll has, for example:")
                print()
                print("dice roll: [1,2,3,4,5]")
                print("dice lock: [0,0,2,0,0]")
                print("                ^ This number,")
                print()
                print("That means that it will be locked throughout the available rolls.")
                print("You won't be able to change it.")
                print("Purposed for the daring people (who want bragging rights).")
                print("Recommended to stay below 3 unlockable dice.")
                print("How much dice do you want with this mechanic each round? (Maximum of 3)")
                #If I let people go wild with higher amounts, it will remove strategy from the game, and will function more like a one-roll-only thing.
                try:
                    dice_l_n = int(input(""))
                    if dice_l_n <= 3 and dice_l_n >= 0:
                        dice_l_n
                        menu[1] = 1
                    else:
                        input("Too high (or low)! Press enter to try again.")
                except:
                    input("Didn't... work. Press enter to try again.")
        
        if menu[0] == "2": #Change max rolls
            while menu[2] == 0:
                menu[2] = 0
                os.system('cls')
                print("This game mechanic changes how many dice rolls are allowed")
                print("before being forced to choose a score.")
                print("Does not add a bonus, just shifts difficulty and importance of chance.")
                print("By default, it is set at 3.")
                try:
                    max_rolls = int(input("How many maximum rolls do you want? "))
                    if max_rolls < 1:
                        input("Too low! Press enter to try again: ")
                    else:
                        menu[2] = 1
                except:
                    input("Didn't... work. Press enter to try again: ")
        
        if menu[0] == "3": #Nothing........ ;)
            os.system('cls')
            print("Hello there!")
            print("...")
            print("Wait, why are you here? I said not to! Didn't I? ...")
            print("Anyways, if you make the dice lock selection not work for 3 times,")
            print("you can self-destruct the code!")
            print("Don't tell anyone else...")
            input("Press enter to step away from the 'dark alley': ")
    #-------The game (after 131 lines of menu code!):--------
    while set_c < score_num:
        if dice_l_n != 0:
            counter = 0
            while counter < dice_l_n:
                dice_l_n_v = random.randint(0,dice_num - 1)
                if dice_l[dice_l_n_v] != 2:
                    dice_l[dice_l_n_v] = 2
                    counter = counter + 1
        while table_choose != "0" and dice_rolls < max_rolls - 1:
            table_choose = 0
            dice = roll_dice(dice_num, dice_l, dice)
            dice_rolls = dice_rolls + 1
            quitter = 0
            d = 0
            while table_choose != "" and table_choose != "0":
                os.system('cls')
                print(f"Roll number {dice_rolls} out of {max_rolls}")
                print("dice num:   1  2  3  4  5")
                print(f"dice roll: {dice}")
                print(f"dice lock: {dice_l}")
                table_choose = input("Enter number of dice to lock / enter '0' to move to score table / leave blank to reroll: ")
                if table_choose == "0":
                    dice_rolls = max_rolls
                elif table_choose != "":
                    try:
                        if dice_l[int(table_choose) - 1] == 2:
                            input("That's permanently locked. Press enter to try again.")
                        else:
                            dice_l[int(table_choose) - 1] = abs(dice_l[int(table_choose) - 1] - 1)
                    except:
                        input("That... Didn't work. Press enter to choose again: ")
                        quitter = quitter + 1
                        if quitter == 3:
                            q = input("It's been your third time though! If you want, press r to self-destruct: ")
                            print() #Space between the game and the error.
                            if q == "r":
                                if buhbye == 0:
                                    buhbye = true #Self-destruct mechanism - Should spawn an error. Liiiiiittle easter egg.
    
        d = 0
        if table_choose != "0":
              dice = roll_dice(dice_num, dice_l, dice)
        os.system("cls")
        #This is the part where assets can be added. -------------------------------------------------------

        #Ones to sixes, IDs = 1 to 6
        for pdice in range(1, 7):
            counter = 0
            if score_set[pdice - 1] != 1:                                                         
                for pdice_t in range(0, dice_num):
                    if dice[pdice_t] == pdice:
                        counter = counter + 1
                score_points[pdice - 1] = counter * pdice
        score_name[0:5] = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]
        
        #Of a kind.
        of_a_kind(3, 5, 6, score_set, score_points)
        of_a_kind(4, 10, 7, score_set, score_points)
        score_name[6:7] = ["Three of a kind", "Four of a kind"]

        #Straight (consecutive numbers), ID = 9
        straight_c = [0] * 6
        if score_set[8] != 1:
            score_points[8] = 0
            for pdice in dice:
                straight_c[pdice - 1] = straight_c[pdice - 1] + 1
            if straight_c == [1,1,1,1,1,0]:
                score_points[8] = 40
            if straight_c == [0,1,1,1,1,1]:
                score_points[8] = 60
        score_name[8] = "Straight"

        #Full house (three of a number, two of another), ID = 10
        fh = [0] * 2
        if score_set[9] != 1:
            score_points[9] = 0
            for pdice in range(0, dice_num):
                counter = 0
                for pdice_t in range(0, dice_num):
                    if dice[pdice] == dice[pdice_t]:
                        counter = counter + 1
                if counter == 3:
                    fh[0] = dice[pdice]
                if counter == 2:
                    fh[1] = dice[pdice]
            if fh[0] != 0 and fh[1] != 0:
                score_points[9] = fh[0] * 8 + fh[1] * 4
        score_name[9] = "Full house"

        #Yahtzee (All one number), ID = 11
        if score_set[10] != 1:
            counter = 0
            for pdice_t in range(0, dice_num):
                if dice[0] == dice[pdice_t]:
                    counter = counter + 1
            if counter == 5:
                score_points[10] = 15 * dice[0]
        score_name[10] = "Yahtzee"

        #The bonuses.
        bonus(11, 0, 6, 6)
        bonus(12, 6, 12, 5)
        score_name[11:12] = ["Dice bonus!", "Extra bonus!"]

        #This is code again. -------------------------------------------------------------------------------
        score_total = 0
        for total in range(0, score_num):
            if score_set[total] != 0:
                score_total = score_total + score_points[total]

        print("Final dice roll:")
        print("dice num:   1  2  3  4  5")
        print(f"dice roll: {dice}")
        print( "ID | Points | Set | Name")
        for s in range(0, score_num):
            print(f"{str(s + 1).zfill(2)} | {str(score_points[s]).zfill(6)} |  {score_set[s]}  | {score_name[s]}")
        print(f"Total points: {score_total}") 

        skill_issue = 1
        while skill_issue == 1:
            try:
                score_choose = int(input("Enter ID of the score you want to set (leading zeros don't matter): "))
                if score_set[score_choose - 1] == 0:
                    score_set[score_choose - 1] = 1
                    skill_issue = 0
                elif score_set[score_choose - 1] == 2:
                    print("That's a bonus.")
                else:
                    print("Already taken.")
            except:
                input("Didn't.... work. Press enter to try again. ")

        set_t = 0
        set_c = 0
        for set_t in range(0, score_num):
            if score_set[set_t] != 0:
                set_c = set_c + 1
        dice_l = [0] * dice_num
        os.system("cls")
        dice_rolls = 0
        table_choose = 0
    bonus(11, 0, 6, 6) #Check bounses again.
    bonus(12, 6, 12, 5)
    print("Drum roll...")
    time.sleep(2)
    os.system("cls")
    score_total = 0
    for total in range(0, score_num):
            score_total = score_total + score_points[total]
    s = 0
    print( "ID | Points | Name")
    for s in range(0, score_num):
            print(f"{str(s + 1).zfill(2)} | {str(score_points[s]).zfill(6)} | {score_name[s]}")
    print(f"TOTAL SCORE: {score_total}")
    if dice_l_n != 0:
        print("+ Bragging rights!")
    time.sleep(1)
    retry = input("Would you like to retry? ('n' to quit): ")
print("Thank you for playing! ")      
time.sleep(1)  
