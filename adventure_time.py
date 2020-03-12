import time
import random


# Slowing down prints
def print_pause(text):
    print(text)
    time.sleep(2)


# Check if input is within allowed answers
def option_checker(option, allowed_answers):
    while True:
        option = input()
        if option in allowed_answers:
            return option
            break
        else:
            print_pause("Sorry, that's not an option")


# Check the time
def clock_check(time):
    if time > 9:
        print_pause("You look at your watch")
        print_pause(f"It's already {time}:00")
        lost()
    if time < 8:
        print_pause("You look at your watch")
        print_pause(f"Good job, it's {time}:00. You're still on track!")


# Restart the game
def play_again():
    print_pause("Do you want to play again?")
    allowed_answers = ["Yes", "No"]
    replay = option_checker("option", allowed_answers)
    if replay == "Yes":
        play_game()
    if replay == "No":
        print_pause("Sorry to hear you decided to quit this amazing game.")
        print_pause("This is your life. It's not an option to quit.")
        play_game()


# Lose Game
def lost():
    print_pause("You didn't manage to come to work on time, "
                "wake up earlier next time")
    play_again()


# Waking Up
def introduction():
    print_pause("You wake up with a dizzy feeling in your head")
    print_pause("You can't seem to remember where and who you are")
    name = input("Who are you? \n")
    print_pause(f"Right, you suddenly recall that your name is {name}")
    print_pause("You realize that you're actually in your own bed")
    return name


# Alarm
def first_choice(name, time):
    print_pause(f"The alarm rings. The clock shows {time}:00. What do you do, "
                "{name}?")
    allowed_answers = ["Get up", "Snooze", "Stop alarm"]
    print_pause(f" 1. {allowed_answers[0]} \n 2. {allowed_answers[1]} \n "
                "3. {allowed_answers[2]} \n")
    alarm = option_checker("option", allowed_answers)
    if alarm == "Get up":
        print_pause("You're getting up and walking to the kitchen.")

    if alarm == "Snooze":
        time += 1
        print_pause(f"You're sleeping for another hour, the clock "
                    "shows {time}:00")
        first_choice(name, time)
    if alarm == "Stop alarm":
        time += 5
        print_pause(f"When you finally wake up 5h have passed")

    clock_check(time)
    return time


# Coffee
def coffee(name, time):
    print_pause("Do you want to make yourself a coffee?")
    allowed_answers = ["Yes", "No"]
    print_pause(f" 1. {allowed_answers[0]} \n 2. {allowed_answers[1]} \n")
    coffee_choice = option_checker("option", allowed_answers)
    if coffee_choice == "Yes":
        print_pause("You put the beans into the coffee grinder")
        print_pause("You insert the beans into the portafilter")
        print_pause("Delicious coffee comes out of the machine")
        print_pause("This took so long. Who bought this crazy coffee machine?")
        time += 2
    else:
        print_pause("Excellent choice! You can have coffee later")
    clock_check(time)
    return time


# Way to Train Station
def train(name, time):
    print_pause(f"Do you want to walk or run to the train station,{name}?")
    allowed_answers = ["Run", "Walk"]
    print_pause(f" 1. {allowed_answers[0]} \n 2. {allowed_answers[1]} \n")
    run = input()
    if run == "Run":
        print_pause("Excellent choice, Speedy Gonzales!")
    if run == "Walk":
        print_pause("You're walking at snail speed, this is "
                    "taking an hour of your time")
        time += 1
    print_pause(f"You arrive at the train station, {name}")
    arrival_time = random.randint(1, 4)
    print_pause(f"The train comes in {str(arrival_time)} h")
    time = time + arrival_time
    clock_check(time)
    print_pause("You arrive downtown and leave the train")
    return time


# Walk to office
def paths_to_work(name, time):
    print_pause("Do want to take the shortcut through the park "
                "or stay on the street?")
    allowed_answers = ["Park", "Street"]
    print_pause(f" 1. {allowed_answers[0]} \n 2. {allowed_answers[1]} \n")
    path = input()
    if path == "Park":
        random_pidgeon = random.randint(0, 2)
        if random_pidgeon != 1:
            print_pause("A random pidgeon appears and attacks you."
                        " You run away and make a long detour to the office")
            time += 2
        else:
            print_pause("You have a nice stroll through the park and "
                        "reach the office")
    if path == "Street":
        time += 1
        print_pause("It takes a bit longer but you reach the "
                    "office after an hour")
    return time


# Reaching work
def at_work(name, time):
    print_pause(F"The office clock shows {time}")
    if time > 10:
        lost()
    else:
        print_pause(f"You made it to the office on time {name}! "
                    "Good worker bee!")
        print_pause("See you tomorrow!")
        return "victory"


# Play
def play_game():
    time = 4
    name = introduction()
    time = first_choice(name, time)
    time = coffee(name, time)
    time = train(name, time)
    time = paths_to_work(name, time)
    time = at_work(name, time)
    if time == "victory":
        print("Thanks for playing the amazing adventure of life. "
              "Good luck tomorrow.")
        quit()


play_game()
