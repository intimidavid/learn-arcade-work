import random

QUIT_COMMANDS = ["q", "quit", "Q", "q.", "QUIT"]
DRINK_COMMANDS = ["a", "drink", "A", "a.", "DRINK", "drink from canteen"]
MOD_SPEED_COMMANDS = ["b", "ahead moderate", "B", "b.", "moderate", "ahead moderate speed", "moderate speed"]
FULL_SPEED_COMMANDS = ["c", "ahead full", "C", "c.", "full", "ahead full speed", "full speed"]
REST_COMMANDS = ["d", "rest", "D", "d.", "REST", "stop and rest", "stop", "STOP AND REST"]
STATUS_COMMANDS = ["e", "status", "E", "e.", "STATUS", "status check", "check", "STATUS CHECK"]


def give_choices():
    # Escape the Wampa!

    print("""
    Welcome to Escape the Wampa!

    You have stolen a tauntaun and are making your way across Hoth to Echo Base.
    A wampa is chasing you! It wants its dinner back and to eat you, too.
    Survive the icy trek and outrun the wampa.""")

    miles_to_base = random.randrange(105, 201)
    miles_travelled = 0
    canteen_sips = 4
    energy = 10
    wampa_distance = random.randrange(15, 20)

    response = ""
    while response not in QUIT_COMMANDS:
        print("""
        A. Drink from your canteen.
        B. Ahead moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check.
        Q. Quit.
        """)

        response = input("Your choice? ")

        if response in DRINK_COMMANDS:
            if canteen_sips > 0:
                print("You drink from your canteen.")
                canteen_sips -= 1
                energy += random.randint(1, 3)
                wampa_distance -= 0.5
            else:
                print("You're out of water!")

        elif response in MOD_SPEED_COMMANDS:
            wampa_run = random.randrange(3, 8)
            moderate_speed = random.randrange(5, 10)
            miles_travelled += moderate_speed
            miles_to_base -= moderate_speed
            energy -= 1
            wampa_distance -= wampa_run
            wampa_distance += 1.5
            print(f"You travel {moderate_speed} miles.")

        elif response in FULL_SPEED_COMMANDS:
            wampa_run = random.randrange(4, 9)
            full_speed = random.randrange(12, 18)
            miles_travelled += full_speed
            miles_to_base -= full_speed
            energy -= 2
            wampa_distance -= wampa_run
            wampa_distance += 5
            print(f"You travel {full_speed} miles.")

        elif response in REST_COMMANDS:
            wampa_run = random.randrange(3, 8)
            wampa_distance -= wampa_run
            wampa_distance -= 2
            energy += random.randint(5, 7)

        elif response in STATUS_COMMANDS:
            print(f"Miles Travelled: {miles_travelled}")
            print(f"Drinks in canteen: {canteen_sips}")
            print(f"The wampa is {wampa_distance} miles behind you.")
            print(f"Miles to base: {miles_to_base}.")

        else:
            print("That didn't do anything. Use one of the available commands")

        if wampa_distance <= 0 < miles_to_base:
            print("The wampa got you! It savagely eats your tauntaun and strikes you down!")
            if miles_to_base < 10:
                print(f'You were only {miles_to_base} miles from base.')
            response = "q"

        if energy < 5 and wampa_distance > 0:
            print("You're thirsty.")

        if energy < 3 and wampa_distance > 0:
            print("You're tired.")

        if energy <= 0:
            print("You ran out of energy. You fall to the floor.")
            response = "q"

        if miles_to_base <= 0:
            print("Congratulations! You made it to Echo Base. Good job!")
            response = "q"


def main():
    done = False
    while not done:
        quit_game = input("Do you want to play Escape the Wampa? Type y or n. ")
        if quit_game == "n":
            done = True
        if not done:
            give_choices()
            print("Game Over.")


if __name__ == "__main__":
    main()
