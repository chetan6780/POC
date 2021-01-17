from collections import Counter

#  Frequency Analysis Application
print("**"*50)

# Welcome message.
print("Welcome To Frequency Analysis Application.\n")
non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '.', '?', '!', ',', '"', "'", ':', ';',
               '(', ')', '%', '$', '&', '#', '\n', '\t', '[', ']', '{', '}', '/', '\\', '-', '_', '+', '*', '|', '^', '<', '>', ]

# for phrase 1 ,Take input
phrase_1 = input(
    "Enter a word or phrase to count the occurrence of each letter: ").strip().lower()
for non_letter in non_letters:
    phrase_1 = phrase_1.replace(non_letter, '')
total_occurrences = len(phrase_1)
letter_count = Counter(phrase_1)

# STRING FORMATING AND NUMBER FORMATING - to print frequency
print("Here is the frequency analysis from key phrase 1:\n")
print("{:10} {:>10} {:>12}".format("Letter", "Occurrence", "Percentage"))
for key, value in sorted(letter_count.items()):
    percentage = round((100*value/total_occurrences), 2)
    print("{:10} {:3.2f} {:15.2f}".format(key, value, percentage))

# print Letters ordered from highest occurrence to lowest
print("\nLetters ordered from highest occurrence to lowest:")
# Returns list of tuples of ordered letters from most occure to less
ordered_letter_count = letter_count.most_common()
phrase_1_ordered_letters = []
for i in ordered_letter_count:
    phrase_1_ordered_letters.append(i[0])
for letter in phrase_1_ordered_letters:
    print(letter, end="")

# for phrase 2 ,Take input
phrase_2 = input(
    "\n\nEnter a word or phrase to count the occurrence of each letter: ").lower().strip()
for non_letter in non_letters:
    phrase_2 = phrase_2.replace(non_letter, '')
total_occurrences = len(phrase_2)
letter_count = Counter(phrase_2)

# STRING FORMATING AND NUMBER FORMATING - to print frequency
print("Here is the frequency analysis from key phrase 2\n")
print("{:10} {:>10} {:>12}".format("Letter", "Occurrence", "Percentage"))
for key, value in sorted(letter_count.items()):
    percentage = round((100*value/total_occurrences), 2)
    print("{:10} {:3.2f} {:15.2f}".format(key, value, percentage))

# print Letters ordered from highest occurrence to lowest
print("\nLetters ordered from highest occurrence to lowest:")
# Returns list of tuples of ordered letters from most occure to less
ordered_letter_count = letter_count.most_common()
phrase_2_ordered_letters = []
for i in ordered_letter_count:
    phrase_2_ordered_letters.append(i[0])
for letter in phrase_2_ordered_letters:
    print(letter, end="")

# End of programm.
print("\n\nThank you for using the Frequency Analysis Application. Goodbye.\n")
print("**"*50)
