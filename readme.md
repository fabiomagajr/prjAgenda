# Contact Book

This is a simple contact book application built with Python and Django.

## Features

- Add, edit, and delete contacts
- Search for contacts
- View contact details

## Requirements

- Python 3.13.2
- Django 5.1.6

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/fabiomagajr/prjagenda.git
    cd contact-book
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000` to see the application.

## Usage

- To add a new contact, click on the "Add Contact" button and fill in the form.
- To edit or delete a contact, click on the contact's name and use the edit or delete buttons.
- Use the search bar to find contacts by name or other details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Django documentation: https://docs.djangoproject.com/
- Python documentation: https://docs.python.org/
