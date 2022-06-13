
import random    

print("Welcome to the word guessing game!")
print()


random_words = ["duvet", "bed", "pillow"] #list of words the random function will pick from
secret_word = random.choice(random_words) #picks a word from the list in the random words

print("Your hint is:",len(secret_word)*"_") # get length of secret word
guess = input("What is your guess? ") # input guess word
count = 1 


while guess != secret_word: # while loop run till guess word match with secret word
    print("Your hint is:",end=" ")  #gives hint to the user, with "_" for each letter in the random word that was chosen
    
    for i in range(0, len(guess)): # this will loop over guess word
        if i < len(secret_word) and guess[i] == secret_word[i]: # if character matches on correct spot
           print(guess[i].upper(),end=" ")   #prints the right letter in caps at the spot where it is correct
        elif secret_word.find(guess[i]) != -1: # if character is present in secret word but not on the exact spot
           print(guess[i],end=" ")
        else:   #if no match is found
           print("_",end=" ")
    count += 1    #preferred this than count = count + 1
    print()
    guess = input("what is your guess? ")  # input guess word
print("Congratulations! You guessed it!")
print(f"It took you {count} guesses.")   #counts the number of guesses it took the user.