# Tissue Sample Collection Management Web App

This web application, powered by Django, serves as a tool to efficiently manage tissue sample collections. It enables users to handle, explore, and update sample information conveniently.

## Features

- **Collection Overview:** View a comprehensive list of collections with associated disease terms.
- **Detailed Collection Information:** Access specific collection details and associated sample data.
- **Sample Management:** Add new samples to existing collections effortlessly.
- **Create Collections:** Seamlessly create new collections within the system.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python (version x.x.x)
- Django (version x.x.x)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Hawaonline/SampleTracker.git
    cd SampleTracker
    ```

2. **Set Up Environment:**

    - Create and activate a virtual environment (optional but recommended):

        ```bash
        python -m venv env_name
        source env_name/bin/activate  # For Linux/Mac
        ```

    - Install project dependencies:

        ```bash
        pip install -r requirements.txt
        ```

3. **Database Setup:**

    Run migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

4. **Run the Application:**

    Start the development server:

    ```bash
    python manage.py runserver
    ```

    Access the application at `http://localhost:8000/` in your web browser.

## Contribution

Please read [CONTRIBUTING.md](link-to-contributing-guide) for details on our code of conduct, and the process for submitting pull requests.

## Acknowledgments

This project is brought to you by [Hawa Abdallah](https://github.com/Hawaonline). Special thanks to Hawa for her contributions and efforts in developing this application.
