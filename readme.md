# Web Note

**Web Note** is a web application that allows users to create, edit, delete, and manage personal notes. This project uses Django class-based views for structured and scalable CRUD functionality and Bootstrap for a responsive and intuitive user interface.

## Features

- **CRUD Functionality**: Add, edit, update, and delete notes effortlessly.
- **Class-Based Views**: Efficient and modular code structure through Django’s class-based views.
- **Organized Notes View**: An organized list of notes for easy access and management.
- **Responsive Design**: Compatible with various devices for on-the-go access.

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: CSS, HTML
- **Database**: SQLite

## Getting Started

### Prerequisites
- Python 3.10
- Django

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HimaKalyanKodati/web_note.git
   cd web_note

2. Install required packages:
   ```bash
   pip install -r requirements.txt

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

4. Start the server:
   ```bash
   python manage.py runserver

5. Access the app in your browser at http://127.0.0.1:8000/.

### Usage
- **Homepage**: View all notes in a structured list.
- **Add Note**: Create a new note by selecting "Add"
- **Edit Note**: Click on "Edit" on any note to modify its content.
- **Delete Note**: Click on "Delete" on any note to delete its content.

### License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
