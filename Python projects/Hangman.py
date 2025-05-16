import random

words=[ 'ran' , 'python' , 'work' , 'ruby' , 'sandal']
chosen_word = random.choice(words)
word_display= ['_' for _ in chosen_word]
attempts = 8

print(" welcome to Hangman! ")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess=input("guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
               word_display[index] = guess
    else:
        print("the letter doesn't appear in the word sorry!!")
        attempts -= 1


if '_' not in word_display:
    print("you guessed the word")
    print(''.join(word_display))
    print("you survived")

else:
    print("you ran out of attempts. the word was: " + chosen_word) 
    print(" you lost")   