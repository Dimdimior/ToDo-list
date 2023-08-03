# ToDo-list

This app lets you create and manage your tasks

## How to run the app

1. Clone the repository
    ```git clone https://github.com/Dimdimior/ToDo-list.git```

2. Go to the project directory:
   ```cd todo```

3. Create a virtual environment:
   ```python -m venv env```

4. Activate the virtual environment:
   - For Windows:
   ``` .\env\Scripts\activate```
   - For macOS and Linux:
   ```source env/bin/activate```
5. Install the project dependencies:
   ```pip install -r requirements.txt```

6. Apply database migrations:
   ```python manage.py migrate```

7. Run the server:
   ```python manage.py runserver```

8. Open your web browser and access the Task Manager application at http://localhost:8000/.
   You can use test user made during migration:

   - Username ```admin```
   - Password ```test```

## Environment Variables

The following environment variables should be set in the `.env` file:

- `DJANGO_SECRET_KEY`: Your Django secret key

**Note:** Before starting the project, make a copy of the `.env_sample` file and rename it to `.env`. Replace the sample values with your actual environment variable values.