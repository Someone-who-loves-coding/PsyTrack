# PsycheTrack

Welcome to the PsycheTrack project. This Django-based application is set up to help you manage your development environment quickly and efficiently.

## Getting Started

To get the project running locally, follow these steps:

### Step 1: Activate the Virtual Environment

The virtual environment (`venv`) is already included in the repository. To activate it, use the following command depending on your operating system:

- **On Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

### Step 2: Change Directory

Navigate into the project directory `PsycheTrack`:

```bash
cd PsycheTrack
```

### Step 3: Run the Server

To start the development server, use the following command:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to view the application.

### Optional: Create a Superuser

To create an additional admin account, use the following command:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the new admin credentials.

## Project Structure

- **venv/**: Virtual environment containing all required dependencies.
- **PsycheTrack/**: The main project directory containing the Django app.

## Additional Notes

Ensure you have Python installed on your machine. If you encounter any issues with package dependencies, consider re-installing them via:

```bash
pip install -r requirements.txt
```

---

Enjoy using PsycheTrack!
```

This README provides a straightforward guide to setting up and running your project with clear instructions on virtual environment activation and Django server management.
