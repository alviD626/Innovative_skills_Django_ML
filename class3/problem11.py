word = input('Enter a word: ')
print(word)
letter = input("Enter the letter: ")
number = int(input("Enter the number: "))
word_index = word.index(letter)
if number != word_index:
    print("no")
else:
    print("yes")