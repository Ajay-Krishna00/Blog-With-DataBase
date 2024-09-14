#  Aim:
#  To Implement a Blog interface in Python, having the following compulsory features:
#   - Creating a Blog Post
#   - Deleting a Blog Post
#   - Modifying an existing Blog Post
#  This includes User Authentication, which means multiple users can register or log in and
#  each user can create their own blog . 
#   - Passwords must be encrypted and stored, so that users can login again.

import bcrypt
import sqlite3
import sys

conn = sqlite3.connect('blog.db') #Connect to SQLite database(will create the database if it doesn't exist)
c = conn.cursor()

# Create Users table
c.execute('''CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY, 
            hashed_password BLOB NOT NULL)''')

# Create Blogs table
c.execute('''CREATE TABLE IF NOT EXISTS blogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            content TEXT NOT NULL,
            FOREIGN KEY(username) REFERENCES users(username))''')

# Commit the changes
conn.commit()

def login():
    currentUsername = input("Enter The Username: ")
    currentPassword = input("Enter The Password: ").encode('utf-8')

    c.execute("SELECT hashed_password FROM users WHERE username = ?", (currentUsername,))
    result = c.fetchone()

    if result and bcrypt.checkpw(currentPassword, result[0]):
        accessGranted(currentUsername)
    else:
        print("Wrong Credentials!\n")

def createAccount():
    username = input("Enter The Username: ")
    password = input("Enter The Password: ").encode('utf-8')
    hashedP = bcrypt.hashpw(password, bcrypt.gensalt())

    # Insert new user into the database
    try:
        c.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, hashedP))
        conn.commit()
        print("Account created successfully. Please login.\n")
        login()
    except sqlite3.IntegrityError:
        print("Username already exists! Please try another.\n")

def displayBlog(currentUsername):
    print("Your Blogs are: ")
    c.execute("SELECT id, content FROM blogs WHERE username = ?", (currentUsername,))
    blogs = c.fetchall()
    
    if blogs:
        for blog in blogs:
            print(f"{blog[0]}. {blog[1]}")
    else:
        print("You have written no Blogs!\n")

def writeBlog(currentUsername):
    print("Write the contents of the blog\n")
    content = input()

    c.execute("INSERT INTO blogs (username, content) VALUES (?, ?)", (currentUsername, content))
    conn.commit()
    print("Blog added successfully!\n")

def editBlog(currentUsername):
    print("Enter the blog number you want to edit:")
    blog_id = int(input())

    c.execute("SELECT id FROM blogs WHERE id = ? AND username = ?", (blog_id, currentUsername))
    if c.fetchone():
        print("Enter the new content of the blog:")
        new_content = input()
        c.execute("UPDATE blogs SET content = ? WHERE id = ?", (new_content, blog_id))
        conn.commit()
        print("Blog edited successfully!\n")
    else:
        print("Invalid Blog Number\n")

def deleteBlog(currentUsername):
    print("Enter the blog number you want to delete:")
    blog_id = int(input())

    c.execute("DELETE FROM blogs WHERE id = ? AND username = ?", (blog_id, currentUsername))
    if c.rowcount > 0:
        conn.commit()
        print("Blog deleted successfully!\n")
    else:
        print("Invalid Blog Number\n")

def accessGranted(currentUsername):
    print(f"\nWelcome {currentUsername}, What do you want to do today?\n")
    while True:
        inp = int(input("Enter 1 to display blog\n\t 2 to write blog\n\t 3 to Edit blog\n\t 4 to Delete blog\n\t 5 to exit\n"))
        match inp:
            case 1: displayBlog(currentUsername)
            case 2: writeBlog(currentUsername)
            case 3: editBlog(currentUsername)
            case 4: deleteBlog(currentUsername)
            case 5:
                print("Thank you for using the Ajay's Blog service!")
                print("Goodbye!")
                return
            case _: print("Invalid choice")

print("Welcome!")
inp = int(input("Enter 1 for Login and 2 for Creating Account: "))
try:
    if inp == 1:
        login()
    elif inp == 2:
        createAccount()
    else:
        print("Enter 1 or 2")
except ValueError:
    print("Invalid Input")
    sys.exit()
