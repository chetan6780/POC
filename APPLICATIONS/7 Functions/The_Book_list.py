FILENAME = "Books.txt"
FILENAME2 = "Readed_books.txt"


def write_books(books):
    with open(FILENAME, "w") as file:
        for book in books:
            file.write(book+"\n")


def read_books():
    books = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            books.append(line)
    return books


def list_books(books):
    for i in range(len(books)):
        book = books[i]
        print(str(i+1)+". "+book)
    print()


def add_book(books):
    book = input("book: ").capitalize()
    if book in books:
        print(f"{book} is already in your list.\n")
    else:
        books.append(book)
        print(book+" is added successfully !\n")
        write_books(books)
        print("Please press 'Enter' to continue.\n")
        input()


def completed_book(books):
    index = input("Number: ")
    try:
        index = int(index)
        try:
            book = books.pop(index-1)
            with open(FILENAME2, "a") as file:
                file.write(book+"\n")
            write_books(books)
            print(f"""Congratulations!!! you have completed '{book}' Book's summary!\n""")
            print("Please press 'Enter' to continue.\n")
            input()

        except:
            print("Please Enter correct Index Number!\n")
            completed_book(books)
    except:
        print("Enter a Number only!!!\n")
        completed_book(books)


def display_menu():
    print("********* COMMAND MENU **********\n")
    print("COMMANDS - DESCRIPTION")
    print("----------------------------------")
    print("List     - List all books.")
    print("Add      - Add a book.")
    print("Complete - Completed a book.")
    print("Exit     - Exit the program.")
    print("----------------------------------\n")


def main():
    print("*************************** Welcome To The book List Program ***************************\n")
    books = read_books()
    while True:
        display_menu()
        cmd = input("COMMAND: ").strip().lower()
        if cmd == "list":
            list_books(books)
        elif cmd == "add":
            add_book(books)
        elif cmd == "complete":
            completed_book(books)
        elif cmd == "exit":
            print("Thank you for using The Book List program! Bye!!!\n")
            break
        else:
            print("Not a valid command.Please try again.\n")
            print("Please press 'Enter' to continue.\n")
            input()


if __name__ == '__main__':
    main()
