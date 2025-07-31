
def first_book():

    book_name = input("What is the book name: ")

    try:

        with open("book.txt" , "r") as file:
            pass
    except FileNotFoundError:
        with open("book.txt" , "w" , newline="") as file:
            file.write('\n')
    return book_name

def add_book():
    log = first_book()
    books = [log]

    with open("book.txt" , "a" , newline="") as file:
        content = file.write(log)
    return log

def view_book():

    content = add_book()
    with open("book.txt" , "r") as file:
        content = file.read()
        print(content)



def main():
    while True:
        print("Welcome to your Book Logger 📖")
        print("1. Add a new book")
        print("2. View all saved books")
        print("3. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            add_book()
        elif choice == 2:
            view_book()
        elif choice == 3:
            print("Goodbye!!")
            break
        else:
            print("INVALID NUMBER!! TRY AGAIN")
main()
