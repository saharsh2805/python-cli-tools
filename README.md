# Python CLI Tools

A collection of command-line interface (CLI) tools built in Python as part of the "Python Dominance Dossier" training.

---

## 1. To-Do List Application (`todo.py`)

A fully functional, persistent CLI to-do list application that saves tasks to a `tasks.json` file.

### Features
* Add, view, remove, and mark tasks as complete.
* Data is saved and loaded automatically between sessions.

### How to Use
```bash
python todo.py

---
## 2. File Organizer (`file_organizer.py`)

A utility script that organizes files in a specified directory by moving them into subfolders based on their file extension.

### Features
* Handles multiple file types.
* Automatically creates destination folders if they don't exist.

### How to Use
```bash
python file_organizer.py

---

## 3. URL Shortener (`url_shortener.py`)

A simple API wrapper that uses the TinyURL service to shorten long web addresses.

### Features
* Accepts a long URL from the user.
* Intelligently adds `https://` if the protocol is missing.
* Returns a shortened URL from the TinyURL API.

### How to Use
```bash
python url_shortener.py