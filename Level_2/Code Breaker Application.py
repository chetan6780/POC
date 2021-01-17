from collections import Counter

#  Code Breaker Application
print("**"*50)

# Welcome message.
print("Welcome To Code Breaker Application.\n")

non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '.', '?', '!', ',', '"', "'", ':', ';',
               '(', ')', '%', '$', '&', '#', '\n', '\t', '[', ']', '{', '}', '/', '\\', '-', '_', '+', '*', '|', '^', '<', '>', ]

# for phrase 1 ,Take input
phrase_1 = """
To Sherlock Holmes she is always the woman. I have seldom heard him mention her under any
other name.
In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any
emotion akin to love for Irene Adler.
All emotions, and that one particularly, were abhorrent to his cold, precise but admirably
balanced mind.
He was, I take it, the most perfect reasoning and observing machine that the world has seen,
but as a lover he would have placed himself in a false position.
He never spoke of the softer passions, save with a gibe and a sneer.
They were admirable things for the observer excellent for drawing the veil from men's motives
and actions.
But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted
temperament was to introduce
a distracting factor which might throw a doubt upon all his mental results.
Grit in a sensitive instrument, or a crack in one of his own highpower lenses,
would not be more disturbing than a strong emotion in a nature such as his.
And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious
and questionable memory.
I had seen little of Holmes lately. My marriage had drifted us away from each other.
My own complete happiness, and the homecentred interests which rise up around the man who
first finds himself master of his own establishment,
were sufficient to absorb all my attention, while Holmes, who loathed every form of society with
his whole Bohemian soul,
remained in our lodgings in Baker Street, buried among his old books, and alternating from
week to week between cocaine and ambition,
the drowsiness of the drug, and the fierce energy of his own keen nature.
He was still, as ever, deeply attracted by the study of crime,
Page 89
and occupied his immense faculties and extraordinary powers of observation in following out
those clues,
and clearing up those mysteries which had been abandoned as hopeless by the official police.
From time to time I heard some vague account of his doings: of his summons to Odessa in the
case of the Trepoff murder,
of his clearing up of the singular tragedy of the Atkinson brothers at Trincomalee,
and finally of the mission which he had accomplished so delicately and successfully for the
reigning family of Holland.
Beyond these signs of his activity, however, which I merely shared with all the readers of the
daily press, I knew little of my former friend and companion.
"""
phrase_1 = phrase_1.lower()

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
phrase_2 = """
Quite so! You have not observed. And yet you have seen.
That is just my point. Now, I know that there are seventeen steps, because I have both seen
and observed.
By the way, since you are interested in these little problems,
and since you are good enough to chronicle one or two of my trifling experiences, you may be
interested in this.
He threw over a sheet of thick, pink tinted notepaper which had been lying open upon the table.
It came by the last post, said he. Read it aloud.
The note was undated, and without either signature or address.
There will call upon you tonight, at a quarter to eight o'clock,
it said, "a gentleman who desires to consult you upon a matter of the very deepest moment.
Your recent services to one of the royal houses of Europe have shown that you are one who
may safely be trusted
with matters which are of an importance which can hardly be exaggerated.
This account of you we have from all quarters received.
Be in your chamber then at that hour, and do not take it amiss if your visitor wear a mask.
This is indeed a mystery, I remarked. What do you imagine that it means?
I have no data yet. It is a capital mistake to theorise before one has data.
Insensibly one begins to twist facts to suit theories, instead of theories to suit facts.
But the note itself. What do you deduce from it?
I carefully examined the writing, and the paper upon which it was written.
The man who wrote it was presumably well to do, I remarked, endeavouring to imitate my
companion's processes.
Such paper could not be bought under half a crown a packet.
It is peculiarly strong and stiff.
"""
phrase_2 = phrase_2.lower()

for non_letter in non_letters:
    phrase_2 = phrase_2.replace(non_letter, '')
total_occurrences = len(phrase_2)
letter_count = Counter(phrase_2)

# STRING FORMATING AND NUMBER FORMATING - to print frequency
print("\n\nHere is the frequency analysis from key phrase 2\n")
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

# To select encode or decode
print("\n")
print("**"*50)
option = input(
    "\nWould you like to encode or decode a message: ").strip().lower()
phrase = input("What is the phrase: ").lower()
for non_letter in non_letters:
    phrase = phrase.replace(non_letter, '')

if option == "encode":
    encoded_phrase = []
    for letter in phrase:
        index = phrase_1_ordered_letters.index(
            letter)  # find index of letter in phrase
        # Rreturns the letter of same index from phrase 2 ordered leters
        letter = phrase_2_ordered_letters[index]
        encoded_phrase.append(letter)
    print("The encoded message is: ")
    for i in encoded_phrase:
        print(i, end="")

elif option == "decode":
    decoded_phrase = []
    for letter in phrase:
        index = phrase_2_ordered_letters.index(
            letter)  # find index of letter in phrase
        # Rreturns the letter of same index from phrase 2 ordered leters
        letter = phrase_1_ordered_letters[index]
        decoded_phrase.append(letter)
    print("The decoded message is: ")
    for i in decoded_phrase:
        print(i, end="")

else:
    print("Please enter valid option.(encode / decode)!!!")

# End of programm.
print("\n\nThank you for using the Code Breaker Application. Goodbye.\n")
print("**"*50)
