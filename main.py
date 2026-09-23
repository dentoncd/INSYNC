import random, time

GOAL = 10
p1_score = 0
p2_score = 0

l = []
r = 0

topics = [
    ["Sweet", "Savory"],
    ["Hot", "Cold"],
    ["Sweet", "Sour"],
    ["Stale", "Fresh"],
    ["Sweet", "Salty"],
    ["Quiet", "Loud"],
    ["Slow", "Fast"],
    ["Beginner", "Expert"],
    ["Casual", "Formal"],
    ["Simple", "Complex"],
    ["Practical", "Impractical"],
    ["Cozy", "Adventurous"],
    ["Healthy", "Unhealthy"],
    ["Safe", "Dangerous"],
    ["Antique", "Modern"],
    ["Low Effort", "High Effort"],
    ["Funny", "Serious"],
    ["Relaxing", "Stressful"],
    ["Overrated", "Underrated"],
    ["Cheap", "Expensive"],
    ["Good Place for Body Hair", "Bad Place for Body Hair"],
    ["Feels Good", "Feels Bad"],
    ["Good Country", "Bad Country"],
    ["Good Ice Cream Flavor", "Bad Ice Cream Flavor"],
    ["Cool Accessory", "Lame Accessory"],
    ["Cool to a 2nd Grader", "Lame to a 2nd Grader"],
    ["Snack", "Meal"],
    ["Ugly Word", "Beautiful Word"],
    ["Young Man Name", "Old Man Name"],
    ["Young Woman Name", "Old Woman Name"],
    ["Green Flag", "Red Flag"],
    ["Bad Time to Scream", "Good Time to Scream"],
    ["Common Hobby", "Uncommon Hobby"],
    ["Small Person Sport", "Large Person Sport"],
    ["Bad First Date", "Good First Date"],
    ["Optional", "Mandatory"],
    ["Normal Greeting", "Weird Greeting"],
    ["Unpopular", "Popular"],
    ["Hard to Do", "Easy to Do"],
    ["Would Sit On", "Wouldn't Sit On"],
    ["Primitive", "Electronic"],
    ["Liquid", "Solid"],
    ["Winter Activity", "Summer Activity"],
    ["Winter Attire", "Summer Attire"],
    ["Fragile", "Indestructible"],
    ["Soft", "Sharp"],
    ["Good Year", "Bad Year"],
    ["Good Movie", "Bad Movie"]
]

while p1_score < GOAL or p2_score < GOAL:
    # Reset
    l = []

    # Player 1 turn
    topic = random.choice(topics)
    print(f"Current topic: {topic[0]} <----> {topic[1]}")
    a_input = input("Player 1, please choose your category ('/' to select, ',' to shuffle): \n")
    while a_input != '/':

        if a_input == ',':
            topic = random.choice(topics)
            print(f"\rCurrent Topic: {topic[0]} <----> {topic[1]}", end="")
            a_input = input()

        elif a_input == '/':
            break

        else:
            a_input = input("Not a valid input, try again: ")
            continue

    # Wheel spinning
    print("\033c", end="")
    print(f"Selected topic: {topic[0]} <----> {topic[1]}")
    for i in range(0, 50):
        l.append(random.randint(1, 20))

    for i in range(0, len(l)):
        r = l[i]
        print(f"\rSpinning the Wheel: {r}/20 ", end="")
        time.sleep(0.05)

    print("\n")

    # Enter hint
    hint = input("Please enter a hint word/phrase: ")
    print("\033c", end="")
    b_input = int(input(f"\nPlayer 2, the topic is {topic[0]} <----> {topic[1]} | Hint: {hint} | Please enter a number (1-20): "))

    # Score check
    if (b_input) == r:
        print(f"Player 2 guessed: {b_input}. The number was: {r}")
        p1_score += 3
    elif b_input == (r + 1) or b_input == (r - 1):
        print(f"Player 2 guessed: {b_input}. The number was: {r}")
        p1_score += 2
    elif b_input == (r + 2) or b_input == (r - 2):
        print(f"Player 2 guessed: {b_input}. The number was: {r}")
        p1_score += 1
    else:
        print(f"Player 2 guessed: {b_input}. The number was: {r}")
    time.sleep(1)

    print("\n======Scores======")
    print(f"Player 1: {p1_score} | Player 2: {p2_score}\n")

    if p1_score >= GOAL:
        print("Player 1 wins!"); exit(1)
    if p2_score >= GOAL:
        print("Player 2 wins!"); exit(1)

    # Player 2 turn
    l = []
    topic = random.choice(topics)
    print(f"Current topic: {topic[0]} <----> {topic[1]}")
    b_input = input("Player 2, please choose your category ('/' to select, ',' to shuffle): \n")
    while b_input != '/':

        if b_input == ',':
            topic = random.choice(topics)
            print(f"\rCurrent Topic: {topic[0]} <----> {topic[1]}", end="")
            b_input = input()

        elif b_input == '/':
            break

        else:
            b_input = input("Not a valid input, try again: ")

    # Wheel spinning
    print("\033c", end="")
    print(f"Selected topic: {topic[0]} <----> {topic[1]}")
    for i in range(0, 50):
        l.append(random.randint(1, 20))

    for i in range(0, len(l)):
        r = l[i]
        print(f"\rSpinning the Wheel: {r}/20 ", end="")
        time.sleep(0.05)

    print("\n")
    hint = input("Please enter a hint word/phrase: ")
    print("\033c", end="")
    a_input = int(input(
        f"\nPlayer 1, the topic is {topic[0]} <----> {topic[1]} | Hint: {hint} | Please enter a number (1-20): "))

    # Score check
    if a_input == r:
        print(f"Player 1 guessed: {a_input}. The number was: {r}")
        p2_score += 3
    elif a_input == (r + 1) or a_input == (r - 1):
        print(f"Player 1 guessed: {a_input}. The number was: {r}")
        p2_score += 2
    elif a_input == (r + 2) or a_input == (r - 2):
        print(f"Player 1 guessed: {a_input}. The number was: {r}")
        p2_score += 1
    else:
        print(f"Player 1 guessed: {a_input}. The number was: {r}")
    time.sleep(1)

    print("\n======Scores======")
    print(f"Player 1: {p1_score} | Player 2: {p2_score}\n")

    if p1_score >= GOAL:
        print("Player 1 wins!")
        exit(1)
    if p2_score >= GOAL:
        print("Player 2 wins!")
        exit(1)