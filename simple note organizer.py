notes = {} 

def display_menu():
    print("\n===== SIMPLE NOTES ORGANIZER =====")
    print("1. Create Note")
    print("2. Edit Note")
    print("3. Delete Note")
    print("4. Search Notes")
    print("5. View All Notes")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-6): ")

        if choice == '1':
            create_note()
        elif choice == '2':
            edit_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            search_notes()
        elif choice == '5':
            view_all_notes()
        elif choice == '6':
            print("thank you for your time!")
            break
        else:
            print("Invalid choice. Please try again.")
            
def create_note():
    title = input("Enter note title: ")
    if title in notes:
        print("Note with this title already exists.")
        return
    content = input("Enter note content: ")
    notes[title] = content
    print(f"Note '{title}' created successfully!")

def edit_note():
    print("\n--- All Notes ---")
    for title, content in notes.items():
        print(f"Title: {title}\nContent: {content}\n")
    for title, content in notes.items():
        print(f"Title: {title}\nContent: {content}\n")
    title = input("Enter note title to edit: ")
    if title not in notes:
        print("Note not found.")
        return
    
    print(f"Current content: {notes[title]}")
    new_content = input("Enter new content: ")
    notes[title] = new_content
    print(f"Note '{title}' updated successfully!")

def delete_note():
    print("\n--- All Notes ---")
    for title, content in notes.items():
        print(f"Title: {title}\nContent: {content}\n")
    title = input("Enter note title to delete: ")
    if title not in notes:
        print("Note not found.")
        return
    del notes[title]
    print(f"Note '{title}' deleted successfully!")

def search_notes():
    keyword = input("Enter keyword to search: ")
    found = False
    for title, content in notes.items():
        if keyword in title.lower() or keyword in content.lower():
            print(f"\nTitle: {title}\nContent: {content}\n")
            found = True
    if not found:
        print("No matching notes found.")


def view_all_notes():
    if not notes:
        print("No notes available.")
        return
    print("\n--- All Notes ---")
    for title, content in notes.items():
        print(f"Title: {title}\nContent: {content}\n")



if __name__ == "__main__":
    main()