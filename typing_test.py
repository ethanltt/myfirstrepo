import time

# List of 10 six-letter words
words = ["Marvel", "Bright", "Puzzle", "Cactus", "Fierce", "Silent", "Castle", "Dragon", "Talent", "Wizard"]

def typing_test(words):
    total_passed = 0

    for word in words:
        print(f"Type the word: {word}")
        
        start_time = time.time()
        user_input = input()
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        letters_per_second = len(word) / elapsed_time
        
        print(f"You typed the word '{word}' in {elapsed_time:.2f} seconds.")
        print(f"Your typing speed is {letters_per_second:.2f} letters per second.")
        
        if letters_per_second > 1:
            print("You passed this round!\n")
            total_passed += 1
        else:
            print("You did not pass this round.\n")

    if total_passed == len(words):
        print("Congratulations! You passed the typing speed test!")
    else:
        print(f"You passed {total_passed} out of {len(words)} rounds.")

# Run the typing test
typing_test(words)
