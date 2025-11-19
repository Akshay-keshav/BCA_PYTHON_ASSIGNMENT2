print("===========================================================")
print("              WELCOME TO LIBRARY BOOK MANAGER              ")
print("===========================================================\n")

books = {}
borrowed = {}

def add_book():
    print("\n--- Add New Book ---")
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    copies = int(input("Enter Number of Copies: "))

    books[book_id] = {"title": title, "author": author, "copies": copies}
    print(f"\nBook '{title}' added successfully!\n")

def view_books():
    if not books:
        print("\nNo books available in the library.\n")
        return

    print("\n------------------- Library Books -------------------")
    print(f"{'Book ID':<10}{'Title':<25}{'Author':<20}{'Copies':<10}")
    print("-----------------------------------------------------")
    for bid, info in books.items():
        print(f"{bid:<10}{info['title']:<25}{info['author']:<20}{info['copies']:<10}")
    print("-----------------------------------------------------\n")


def search_book():
    print("\n--- Search Book ---")
    print("1. Search by Book ID")
    print("2. Search by Title")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        bid = input("Enter Book ID: ")
        if bid in books:
            book = books[bid]
            print(f"\nBook Found:\nID: {bid}\nTitle: {book['title']}\nAuthor: {book['author']}\nCopies: {book['copies']}\n")
        else:
            print("\nBook not found.\n")

    elif choice == "2":
        title_part = input("Enter part of the title: ").lower()
        found = False
        for bid, book in books.items():
            if title_part in book["title"].lower():
                print(f"\nBook Found:\nID: {bid}\nTitle: {book['title']}\nAuthor: {book['author']}\nCopies: {book['copies']}\n")
                found = True
        if not found:
            print("\nNo books match that title.\n")
    else:
        print("\nInvalid choice.\n")

def borrow_book():
    print("\n--- Borrow Book ---")
    student = input("Enter Student Name: ")
    book_id = input("Enter Book ID to borrow: ")

    if book_id in books:
        if books[book_id]["copies"] > 0:
            books[book_id]["copies"] -= 1
            borrowed[student] = book_id
            print(f"\nBook '{books[book_id]['title']}' borrowed successfully by {student}.\n")
        else:
            print("\nSorry, no copies available for this book.\n")
    else:
        print("\nBook ID not found.\n")

def return_book():
    print("\n--- Return Book ---")
    student = input("Enter Student Name: ")
    book_id = input("Enter Book ID to return: ")

    if student in borrowed and borrowed[student] == book_id:
        books[book_id]["copies"] += 1
        del borrowed[student]
        print(f"\nBook '{books[book_id]['title']}' returned successfully by {student}.\n")
    else:
        print("\nNo such borrowing record found.\n")

    if borrowed:
        borrowed_list = [f"{stu} -> {bk}" for stu, bk in borrowed.items()]
        print("\nCurrently borrowed books:")
        for item in borrowed_list:
            print(item)
    else:
        print("\nNo books currently borrowed.\n")

def menu():
    while True:
        print("\n=========== Library Menu ===========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("\nThank you for using Library Book Manager!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

def save_records():
    with open("library_records.txt", "w") as file:
        file.write("Library Books:\n")
        for bid, info in books.items():
            file.write(f"{bid}: {info['title']} by {info['author']} ({info['copies']} copies)\n")

        file.write("\nBorrowed Books:\n")
        for student, book_id in borrowed.items():
            file.write(f"{student} -> {book_id}\n")
    print("\nRecords successfully saved to 'library_records.txt'!\n")

menu()

save_choice = input("Do you want to save the records to a file? (yes/no): ").strip().lower()
if save_choice == "yes":
    save_records()
else:
    print("\nRecords not saved. Exiting program.\n")