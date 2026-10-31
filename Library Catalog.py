def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    with open("books.txt", "a") as f:
        f.write(title + "," + author + "\n")

    print("Book added successfully!")


def search_book():
    name = input("Enter title or author to search: ")

    with open("books.txt", "r") as f:
        for line in f:
            if name.lower() in line.lower():
                print(line.strip())


def report():
    with open("books.txt", "r") as f:
        books = f.readlines()

    print("Total number of books:", len(books))

    author = input("Enter author name: ")
    count = 0

    for book in books:
        title, book_author = book.strip().split(",")
        if author.lower() == book_author.lower():
            count += 1

    print("Books by", author, ":", count)


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        report()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
