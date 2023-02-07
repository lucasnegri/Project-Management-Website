# Project Management Website

## Distinctiveness and Complexity:
This project is a web-based application designed to help users manage teams, projects, and tasks in a single platform. It satisfies the distinctiveness and complexity requirements as it provides a user-friendly interface to manage multiple projects with various teams and members, and assigns tasks to individuals within those projects. This application is built using HTML, CSS, JavaScript, and Django, which makes it a challenging and complex project.

## Contents:
- templates folder contains all the HTML templates used in the project.
- static folder contains the CSS and JavaScript files.
- views.py contains the Django apps for the Teams, Projects, and Tasks.
- db.sqlite3 is the database file.
- manage.py is the management script for the project.
- requirements.txt contains the required packages for the project.


## How to Run:
- Clone the repository to your local machine.
- Install the required packages using pip install -r requirements.txt.
- Migrate the models to create the database tables using python manage.py migrate.
- Run the development server using python manage.py runserver.
- Open the application in your web browser at http://localhost:8000/.
- Additional Information:
- This project is a part of the CS50 Web Programming with Python and JavaScript course, and the objective was to create a project management website. The application is built using Django and JavaScript and provides functionalities to create teams, projects, and tasks. The interface is designed to be user-friendly, making it easy to manage multiple projects with various teams and members.  



## Explaining All request urls  


### Projects URL's

#### index
Defines a function called "index" which is handling the request for loading the main page of the projects. It retrieves all the projects associated with the current user and stores them in the variable 'projects'. A message is also defined with the value "All projects".

The function then uses the 'render' method from the Django framework to render the 'network/index.html' template and pass the context data, which includes the projects and message, to the template. This way, the data can be used to display the projects on the main page of the website.

#### create_project
This code defines the view for processing the "create_project" request. When a GET request is made to the "create_project" path, the code generates a context dictionary containing a list of all registered users and the teams the current user belongs to. The context is then passed to the "network/create_project.html" template to render the page.

When a POST request is made to the "create_project" path, the code retrieves the project name, objective, selected team, and selected users from the request data. It then creates a new project with the given information and adds the selected users as members of the project. Finally, it redirects the user back to the index page.

#### get_team_users
This is a view in Django that handles a GET request and returns a JSON response. It is used to retrieve the list of users that belong to a specific team when the team is selected in the "create project" form.  


### Tasks URL's

#### tasks
View function named tasks that processes HTTP requests for the tasks page. When a GET request is received for this URL, the function retrieves all the tasks that are assigned to the currently logged-in user and are not yet completed. These tasks are stored in a queryset named user_tasks. The render function is then called, which returns an HTML template named "network/tasks.html". 

#### project_tasks
Defines a Django view function called project_tasks that takes in a request and a project_id as parameters. The function retrieves the project object with the specified project_id using the Project.objects.get method. Then, it filters all the Task objects associated with that project using the Task.objects.filter method and the project field. A message string is created to display the name of the project. Finally, the function returns the tasks to be displayed on a template file named network/tasks.html using the render method, along with the message, as context data.

#### create_task
The create_task function is a view in Django that creates a new task based on user input. If the request method is a GET, it retrieves the project_id and displays a template with the members of the project. If the request method is a POST, it creates a new task with the provided task name, objective, selected user, and project. The selected user is added to the task's assigned members, and the task's project is marked as not completed. The user is then redirected to the task list.

#### mark_task_as_completed
The mark_task_as_completed function is a view in Django that marks a task as completed by setting its is_completed field to True. It also checks if all tasks associated with the task's project are completed, and if so, it sets the project's is_completed field to True. The function finally redirects the user to the task list.  

     
### Teams URL's

#### teams
The teams function is a view in Django that loads the teams page. It retrieves the current user from the request object and uses the current_user.teams.all() method to retrieve all the teams that the user is a member of. The teams are then passed as a context to the render method to be displayed in the "network/teams.html" template.

#### teams_projects 
The team_projects function displays all the projects associated with a specific team. It takes the team's ID and retrieves the team and its projects. The projects and a message with the team's name are then displayed in the "network/index.html" template.

#### create_team
The create_team function creates a new team. If a GET request is made, it retrieves all registered users and displays them in a list. If a POST request is made, the function retrieves the team name, objective, color, and members from the request, creates a new team object with these properties, saves it to the database, and returns a page showing all teams including the newly created one.