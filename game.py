#
#
# color=input("Enter a color: ")
# plural_noun=input("Enter a Plural Noun: ")
# celebrity=input("Enter a celebrity: ")
# print("Roses are "+color)
# print(plural_noun+" are blue")
# print("I love "+celebrity)
#

#Guessing Game

secret_word = "book"
guess = ""
guess_count =0
guess_limit=3
out_of_guesses= False


while guess != secret_word and not out_of_guesses:
    if guess_count< guess_limit:
        guess = input("Enter Guess: ")
        guess_count +=1
    else:
        out_of_guesses=True

if out_of_guesses:
    print("Out of Guesses, You loose.")
else:
    print("You win!")