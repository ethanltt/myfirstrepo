def run_word_guessing_game():
    words_with_hints = [
        ("Bakery", "A place where bread and cakes are made."),
        ("Gloves", "Worn on hands to keep them warm or clean."),
        ("Jungle", "A dense forest in a tropical area."),
        ("Stream", "A small, narrow river."),
        ("Throne", "A ceremonial chair for a sovereign or deity."),
        ("Silver", "A precious shiny grayish-white metal."),
        ("Frozen", "Turned into ice or another solid state."),
        ("Spring", "The season after winter and before summer."),
        ("Bottle", "A container, typically made of glass or plastic and with a narrow neck, used for storing drinks."),
        ("Gadget", "A small mechanical or electronic device or tool.")
    ]

    score = 0

    print("Welcome to the Word Guessing Game!")
    print("You will be given a word with the first, third, and last letters, and a hint. Guess the full word.\n")

    for word, hint in words_with_hints:
        # Display the word with first, third, and last letters only
        if len(word) >= 3:  # Ensure the word is long enough
            masked_word = word[0] + "_" + word[2] + "_" * (len(word) - 4) + word[-1]
        else:
            masked_word = word  # For words shorter than expected, show as is
        
        print(f"Word: {masked_word}")
        print(f"Hint: {hint}")
        
        # Initialize correct guess flag
        correct_guess = False
        
        while not correct_guess:
            # Get user input
            user_guess = input("Your guess: ").capitalize().strip()
            
            # Check if the guess is correct
            if user_guess == word:
                print("Correct!\n")
                score += 1
                correct_guess = True
            else:
                print("Wrong! Try again.")

    print(f"Game Over! Your final score is {score}/{len(words_with_hints)}.")

# Run the game
run_word_guessing_game()
