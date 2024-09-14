# Blog Interface in Python

## Project Overview
This Python-based blog interface allows multiple users to register, log in, and manage their own blog posts. The project includes user authentication with password encryption and features such as creating, editing, deleting, and displaying blog posts. The user data and blog posts are securely stored in a SQLite database.

## Features
- **User Authentication**: Users can create accounts and log in with encrypted passwords.
- **Create Blog Post**: Authenticated users can write new blog posts.
- **Display Blog Posts**: Users can view a list of their own blog posts.
- **Edit Blog Post**: Users can modify the content of an existing blog post.
- **Delete Blog Post**: Users can delete a blog post.
- **Persistent Data Storage**: All user and blog data is stored in a SQLite database.

## Technologies Used
- **Python**: Core programming language.
- **SQLite**: A lightweight database for data storage.
- **bcrypt**: For secure password hashing and validation.
- **sqlite3**: Python module for interacting with SQLite.

## Installation and Setup

### Prerequisites
- Python 3.x
- SQLite (installed with Python's standard library)
  
### Libraries
This project uses `bcrypt` and `sqlite3`. You can install `bcrypt` via `pip`:

```bash
  pip install bcrypt
```
## Database Schema

### `users` Table:

| Column          | Data Type | Description                        |
| --------------- | --------- | ---------------------------------- |
| `username`      | TEXT      | Primary key, stores the username.  |
| `hashed_password` | BLOB      | Stores the encrypted user password. |

### `blogs` Table:

| Column     | Data Type | Description                        |
| ---------- | --------- | ---------------------------------- |
| `id`       | INTEGER   | Primary key, unique blog post ID.  |
| `username` | TEXT      | Foreign key, references `users.username`. |
| `content`  | TEXT      | The content of the blog post.      |


## Future Enhancements
Implementing password recovery via email.
Adding the ability to comment on blog posts.
Expanding the UI to a web interface using Flask or Django.
Adding timestamps to blog posts.
Integrating with a cloud database for scalability.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Credits
Created by AJAY KRISHNA D
