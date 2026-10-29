# Email Management System 📧

## Overview
The **Email Management System** is a Python project that simulates basic email functionality. Users can send emails to other users, manage their inboxes, read messages, and delete emails.

Each email stores information about the sender, receiver, subject, body, timestamp, and read status.

## Features
- **Send Emails:** Send messages between users.
- **Inbox Management:** Store and organize received emails.
- **List Emails:** Display inbox messages with their sender, subject, timestamp, and read status.
- **Read Emails:** View the full content of an email and automatically mark it as read.
- **Delete Emails:** Remove emails from the inbox.
- **Timestamp Tracking:** Record the date and time when each email is created.
- **Input Validation:** Handle empty inboxes and invalid email numbers.

## Concepts Practiced
- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors and Instance Attributes
- Object Relationships and Composition
- Lists and Object Storage
- Methods and Encapsulation
- Python's `datetime` Module
- String Formatting
- Input Validation and Conditional Logic

## Project Structure
The project consists of three main classes:

| Class | Responsibility |
|---|---|
| `Email` | Stores email details, tracks read status, and displays full messages. |
| `User` | Represents a user who can send emails and manage their inbox. |
| `Inbox` | Stores received emails and supports listing, reading, and deleting messages. |

## How It Works
1. Users are created with their own inboxes.
2. A user sends an email by specifying the receiver, subject, and message body.
3. The email is added to the receiver's inbox.
4. Users can view their inbox and select an email to read.
5. Reading an email changes its status from **Unread** to **Read**.
6. Users can delete emails from their inboxes.

## Example
The main function creates two users, Tory and Ramy, and demonstrates sending emails between them.

```python
tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
```

## Technologies Used
- **Python**
- **datetime** — for recording email timestamps

## Learning Outcomes
This project demonstrates how object-oriented programming can model a simple communication system. It provides practice in designing classes, connecting objects, managing collections of objects, and implementing common email operations.

## Future Improvements
- Add a graphical user interface (GUI).
- Implement email search and filtering.
- Add inbox folders and spam management.
- Support email attachments.
- Add persistent storage using files or a database.
- Improve input handling and user interaction.

---

*Part of my Python practice projects, focused on strengthening programming fundamentals and object-oriented design.*
