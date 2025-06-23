**Chapter and Coffee**

    Chapter and Coffee is a Python-based console application that simulates a cozy bookstore café experience. 
    It allows users to browse a menu of books and beverages, place orders, and view their basket with a detailed cost breakdown. 
    Designed with simplicity and functionality in mind, this project demonstrates file handling, user input, and basic access control using Python methods.

**Features**
**Interactive Menu Display**
    View available books, drinks, and cafe items, all loaded dynamically from text files.

**Order Management**
    Users can select items from the menu and add them to their basket. The application calculates and displays the total cost.

**Today's Specials**
    A curated list of daily specials is included in all relevant displays and ordering actions.

**Secure Staff Access**
    Staff members can modify the menu (add or remove items) using a password-protected method. The password is securely stored in a text file and verified during access.

**File-Based Data Handling**
    All menu items and credentials are stored in plain text files, making the system easy to update and maintain.

**How it works**
--The program reads from text files to display the menu, books, drinks, and specials.
--Users interact with the system through a series of prompts and selections.
--Orders are collected and summarized in a list basket.
--Staff can log in with a password to edit the menu files directly from the program interface.

**File Structure**

chapter_and_coffee

── books.txt           # List of available books
── drinks.txt          # List of available drinks
── menu.txt            # General cafe menu
── specials.txt        # Today's specials
── password.txt        # Staff password (for editing access)
── chapter_and_coffee.py  # Main Python script

**Staff Access**
To modify menu files:

--Enter the staff mode.
--Provide the correct password (stored in password.txt).
--Use the interface to add or remove items from the menu.
