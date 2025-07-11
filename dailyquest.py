# dailyquest.py

import time

def dramatic_pause(seconds=1):
    time.sleep(seconds)

def print_header():
    print("\n=== 🌅 DAILYQUEST: The Awakening ===\n")

def start_game():
    print_header()
    print("You awaken. Again. Against your will.\n")
    print("What do you do?")
    print("1) Open your eyes")
    print("2) Hit snooze")
    print("3) Scroll phone mindlessly")
    print("4) Contemplate the void\n")

    choice = input("> ")

    if choice == "1":
        dramatic_pause()
        print("\n👁️ Your eyes burn like you've gazed upon a forbidden sun.")
        print("You regret this decision immediately.")
        bathroom_scene()
    elif choice == "2":
        dramatic_pause()
        print("\n🛏️ You sleep another 9 minutes. Victory is fleeting.")
        start_game()  # recursive loop of snoozing
    elif choice == "3":
        dramatic_pause()
        print("\n📱 You scroll. Memes. News. Doom. Repeat.")
        print("You’ve lost 17 minutes and a piece of your soul.")
        bathroom_scene()
    elif choice == "4":
        dramatic_pause()
        print("\n🌀 You stare at the ceiling.")
        print("The ceiling stares back.")
        bathroom_scene()
    else:
        print("\n⚠️ Invalid input. Sleep reclaims you.")
        print("The cycle begins anew.")
        start_game()

def bathroom_scene():
    print("\nYou stumble to the bathroom. The light is sears your eyes.")
    print("Choose your action:")
    print("1) Brush teeth")
    print("2) Stare into mirror")
    print("3) take shower")
    print("4) Return to bed (chaotic evil)\n")

    choice = input("> ")

    if choice == "1":
        print("\n🦷 Minty freshness acquired. You feel 0.04% more alive, the feeling dissipates.")
    elif choice == "2":
        print("\n👤 You stare into the mirror. It whispers:")
        print('"who are you?"')
    elif choice == "3":
        print("\nThe water heater is out, you take a cold shower.")
    elif choice == "4":
        print("\n🛌 You return to bed.")
        print("The cycle begins anew.")
        start_game()
    else:
        print("\n⚠️ Invalid input. The toothpaste judges you.")
        bathroom_scene()

    kitchen_scene()

def kitchen_scene():
    print("\n🏠 You enter the kitchen. Destiny awaits.")
    print("What do you do?")
    print("1) Brew coffee")
    print("2) Pour cereal with orange juice (accidentally?)")
    print("3) Open fridge and forget why")
    print("4) Just stand there\n")

    choice = input("> ")

    if choice == "1":
        print("\n☕ You brew. -5 min")
        print("You feel momentarily unstoppable, the feeling dissipates.")
        end_game()
    elif choice == "2":
        print("\n🥣 No...")
        print("so far, its not going well.")
        end_game()
    elif choice == "3":
        print("\n🧊 Cold air on your face. The light in the darkness shows you that you are out of milk.")
        print("You still don’t remember what you needed.")
        end_game()
    elif choice == "4":
        print("\n⏳ You stare at nothing. The kitchen stares back.")
        end_game()
    else:
        print("\n⚠️ Invalid input. You are now late for work.")
        kitchen_scene()

def end_game():
    print("\n🎉 You survived the morning.")
    print("Barely...")
    print("Thanks for playing DAILYQUEST™.")
    print("\n🏁 [ GAME OVER ]\n")

if __name__ == "__main__":
    start_game()
