# Task Manager
Task Manager is a web application built with Django that allows you to manage projects, teams, employees, tasks, positions, and task types. It provides a user-friendly interface for organizing and tracking tasks within an organization or team.

## Characteristic

```
- Create, Update, Detail and Delete Projects;
- Categorize tasks based on task types;
- Add any Teams to any Projects;
- Create, Update, Detail and Delete Tasks;
- Information about users and him positions;
- Track the status of tasks and projects;
```
## Local deployment instruction
To deploy the Task Manager project locally, please follow the steps below:

1. Clone the repository to your local machine: git clone https://github.com/Bohdan11Dii/task-manager.git
2. Navigate to the project directory: cd task-manager
3. Create a virtual environment: python -m venv env
4. Activate the virtual environment:
    - For Windows:  .\env\Scripts\activate
    - For macOS and Linux: source env/bin/activate
5. Install the project dependencies: pip install -r requirements.txt
6. Apply database migrations: python manage.py migrate
7. Run the development server: python manage.py runserver
8. Open your web browser and access the Task Manager application at http://localhost:8000/.

#### You can use test user made during migration:

* Username Bohdan
* Password 27%!ImV1z43&

#### Environment Variables
In the root directory, you need to create .env file and set your secret key to it
```
SECRET_KEY: Your Django secret key
```