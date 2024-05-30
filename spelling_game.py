def run_word_guessing_game():
    words_with_hints =  [
    ("apple", "A fruit often associated with Newton"),
    ("beach", "A sandy or pebbly shore by a body of water"),
    ("chess", "A strategic board game with kings and queens"),
    ("drill", "A tool or exercise often used in construction or fitness"),
    ("eagle", "A large bird of prey with a keen eye"),
    ("flame", "A visible, gaseous part of a fire"),
    ("grape", "A small, sweet fruit often used to make wine"),
    ("honey", "A sweet substance made by bees"),
    ("island", "A piece of land surrounded by water"),
    ("joker", "A card in a deck, or a person who loves to joke")
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
            user_guess = input("Your guess: ").strip()
            
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
