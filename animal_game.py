import random

# List of animals and their clues
animals = {
    "elephant": ["I am the largest land animal.", "I have a long trunk.", "I have big ears."],
    "giraffe": ["I have a very long neck.", "I eat leaves from tall trees.", "I am the tallest land animal."],
    "penguin": ["I can't fly, but I am a bird.", "I live in cold places.", "I waddle when I walk."],
    "lion": ["I am known as the king of the jungle.", "I have a majestic mane.", "I roar loudly."],
    "kangaroo": ["I carry my babies in a pouch.", "I can jump very high.", "I live in Australia."],
}

# Welcome message
print("Welcome to the Guess the Animal game!")
print("Try to guess the animal based on the clues provided.")
print("Keep guessing until you get it right!\n")

# Main game loop
while True:
    # Select a random animal
    animal, clues = random.choice(list(animals.items()))

    clue_index = 0

    # Animal guessing loop
    while True:
        print(f"Clue {clue_index + 1}: {clues[clue_index]}")
        guess = input("Your guess: ").strip().lower()

        if guess == animal:
            print("Congratulations! You guessed the correct animal!\n")
            break
        else:
            print("That's not correct.\n")
            clue_index = (clue_index + 1) % len(clues)

    # Ask the player if they want to play again
    play_again = input("Do you want to guess another animal? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
