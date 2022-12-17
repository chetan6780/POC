import random

#  Welcome to the Thesaurus App!
print("**"*50)

# Welcome message.
print("Welcome To Welcome to the Thesaurus App!\n")

# Defining a list
thesaurus = {"hot": ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
             "cold": ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
             "happy": ['content', 'cheery', 'merry', 'jovial', 'jocular'],
             "sad": ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']
             }

# Display words
print("""Choose a word from the thesaurus and I will give you a synonym.
Here are the words in the thesaurus:""")
for key in thesaurus.keys():
    print("\t-", key)

# synonym for given word
word = input("\nWhat word would you like a synonym for: ").strip().lower()
if word in thesaurus.keys():
    a = random.randint(0, 4)
    print(f"A synonym for {word} is {thesaurus[word][a]}.")
else:
    print("I'm sorry, that word is not currently in the thesaurus.")

# print whole thesaurus
whole_thesaurus = input(
    "\nWould you like to see the whole thesaurus (yes/no): ").strip().lower()
if whole_thesaurus == "yes":
    for key, values in thesaurus.items():
        k = key.title()
        print(f"\n{k} synonyms are: ")
        for v in values:
            print(f"\t-{v}")
else:
    print("\nThank you for using the Welcome to the Thesaurus App! Goodbye.\n")

# End of programm.
print("**"*50)
