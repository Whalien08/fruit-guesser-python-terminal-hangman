import random

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''


someWords = someWords.split() 
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: The word is a fruit.')
    
    # Print the initial blank spaces
    print(' '.join(['_'] * len(word)))

    guessed_letters = set() 
    chances = len(word) + 2

    try:
        while chances > 0:
            print(f"\nChances remaining: {chances}")
            guess = input('Enter a letter to guess: ').lower()

            if not guess.isalpha():   # check if letter is entered
                print('Enter only a letter!')
                continue
            elif len(guess) > 1:    # check if only a single letter is entered
                print('Enter only a single letter!')
                continue
            elif guess in guessed_letters:    # check if the letter was already gussed
                print('You already guessed that letter!')
                continue

            # Add the valid guess to our set of guessed letters
            guessed_letters.add(guess)

            # Check if the guess is wrong (Costs a chance)
            if guess not in word:
                print(f"Oof! '{guess}' is not in the word.")
                chances -= 1
            else:
                print("Good guess!")

            # Build the current state of the word to show the user
            for char in word:
                if char in guessed_letters:
                    print(char, end=' ')
                else:
                    print('_', end=' ')
            print() 

            if all(char in guessed_letters for char in word):
                print(f'\nCongratulations! You won! The word was: {word}')
                break

        # The else block attached to a while loop runs if the loop finishes without hitting a 'break'
        else:
            print('\nYou lost! The word was:', word)

    except KeyboardInterrupt:
        print('\nGame interrupted. Bye!')
        exit()


