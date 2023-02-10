## Distinctiveness and Complexity:
This project management website is unique in its approach to helping users manage their teams, projects, and tasks. It allows users to create teams and projects, and assign tasks to specific users within those projects. This level of customization and organization sets it apart from the previous projects done on the course.

In terms of complexity, this project required a deep understanding of object manipulation and the ability to style templates based on the values within those objects. This required a significant amount of effort and learning, as I had to explore new programming concepts and techniques to bring this project to life. The end result is a project management website that is both user-friendly and sophisticated in its functionality.

In order to bring this project to life, I had to delve into several advanced programming concepts. This included learning how to manipulate DOM styles based on the values within objects, creating object methods to simplify data returns, gaining a strong understanding of the Django framework, setting up asynchronous requests within templates, and manipulating databases to store and retrieve project data. Each of these elements required a significant amount of effort and learning, but the end result is a project management website that is both functional and minimalist. This project represents a significant step forward in my programming skills and demonstrates my ability to learn new technologies and programming concepts quickly and effectively.

In addition to the advanced programming concepts mentioned previously, I also had to learn how to work with SASS in order to bring this project to life. SASS was an essential component of the project as it allowed me to style the templates in a more organized and efficient manner. However, since Django is not a real-time application, I also had to learn how to properly compress the SASS into CSS before integrating it into the project. This added an extra layer of complexity to the project, but was necessary in order to ensure that the website would function smoothly and load efficiently for users. Overall, my experience with SASS and CSS compression has made me a more well-rounded programmer and has added valuable skills to my toolkit.

Overall, the combination of distinctiveness and complexity make this project management website a valuable tool for anyone looking to manage their projects and tasks in a more organized and efficient manner. The knowledge I gained from this project is significantly greater than what I learned from previous projects, making it a unique and valuable experience.  

*** 

## How to Run:
- Clone the repository to your local machine.
- Install the required packages using ``pip install -r requirements.txt``.
- Migrate the models to create the database tables using `python manage.py migrate`.
- Run the development server using `python manage.py runserver`.
- Open the application in your web browser at our local host address.
- Additional Information:
- This project is a part of the CS50 Web Programming with Python and JavaScript course, and the objective was to create a project management website. The application is built using Django and JavaScript and provides functionalities to create teams, projects, and tasks. The interface is designed to be user-friendly, making it easy to manage multiple projects with various teams and members. 

***

## Objective
This project is a web-based application designed to help users manage teams, projects, and tasks in a single platform. It satisfies the distinctiveness and complexity requirements as it provides a user-friendly interface to manage multiple projects with various teams and members, making it possible to assign tasks to individuals within those projects. This application is built using HTML, CSS, JavaScript, and Django, which makes it a challenging and complex project.

***

## Contents:
- templates folder contains all the HTML templates used in the project.
- static folder contains the CSS and JavaScript files.
- views.py contains the Django apps for the Teams, Projects, and Tasks.
- db.sqlite3 is the database file.
- manage.py is the management script for the project.
- requirements.txt contains the required packages for the project.


***



## Templates: 
### Projects Templates  
**index.html**
This template displays the main page of the projects section. It uses a for loop to iterate through the projects in the context data and displays the project name and objective for each project. It also includes a button to navigate to the create_project page.

**create_project.html**
This template is used to display the create project form. It includes form fields for the project name, objective, selected team, and selected users. The form is submitted to the create_project view, which processes the form data and creates the new project.

**get_team_users.html**
A template to retrieve the list of users that belong to a specific team when the team is selected in the "create project" form. It passes this value as a JSON to the template.

### Tasks Templates  
**tasks.html**
This template displays the tasks page. It uses a for loop to iterate through the tasks in the context data and displays the task name, objective, assigned user, and status for each task. It also includes a button to navigate to the create_task page.

**project_tasks.html**
This template displays the tasks for a specific project. It uses a for loop to iterate through the tasks in the context data and displays the task name, objective, assigned user, and status for each task.

**create_task.html**
This template is used to display the create task form. It includes form fields for the task name, objective, selected user, and project. The form is submitted to the create_task view, which processes the form data and creates the new task.

### Teams Templates  
**teams.html**
This template displays the teams page. It uses a for loop to iterate through the teams in the context data and displays the team name, objective, and color for each team. It also includes a button to navigate to the create_team page.

**teams_projects.html**
This template displays all the projects associated with a specific team. It uses a for loop to iterate through the projects in the context data and displays the project name and objective for each project.

**create_team.html**
This template is used to display the create team form. It includes form fields for the team name, objective, color, and members. The form is submitted to the create_team view, which processes the form data and creates the new team.

**manage_Team.html**
This template is used to display a view of a specific team for the user. It shows all the information about that team and a list. If the current user is the creator of the team, it should let that administrator to add/remove users from the team.

***



## URL's Paths

### Projects URL's

#### index
Defines a function called "index" which is handling the request for loading the main page of the projects. It retrieves all the projects associated with the current user and stores them in the variable 'projects'. A message is also defined with the value "All projects".

The function then uses the 'render' method from the Django framework to render the projects(index) template and pass the context data, which includes the projects and message, to the template. This way, the data can be used to display the projects on the main page of the website.

#### create_project
This code defines the view for processing the "create_project" request. When a GET request is made to the "create_project" path, the code generates a context dictionary containing a list of all registered users and the teams the current user belongs to. The context is then passed to the "create_project" template to render the page.

When a POST request is made to the "create_project" path, the code retrieves the project name, objective, selected team, and selected users from the request data. It then creates a new project with the given information and adds the selected users as members of the project. Finally, it redirects the user back to the index page.

#### get_team_users
Used to retrieve the list of users that belong to a specific team when the team is selected in the "create project" form, then, it passes this value as a JSON to the template.  


### Tasks URL's

#### tasks
View function named tasks that processes requests for the tasks page. When a GET request is received for this URL, the function retrieves all the tasks that are assigned to the currently logged-in user and are not yet completed. These tasks are stored in a queryset named user_tasks. The render function is then called, which returns an HTML template named "tasks". 

#### project_tasks
Defines a Django view function called project_tasks that takes in a request and a project_id as parameters. The function retrieves the project object with the specified project_id, then, it filters all the Task objects associated with that project using the filter method and the project field. A message string is created to display the name of the project. Finally, the function returns the tasks to be displayed on a template file named "tasks" using the render method, along with the message, as context data.

#### create_task
The create_task function is a view in Django that creates a new task based on user input. If the request method is a GET, it retrieves the project_id and displays a template with the members of the project. If the request method is a POST, it creates a new task with the provided task name, objective, selected user, and project. The selected user is added to the task's assigned members, and the task's project is marked as not completed. The user is then redirected to the task list.

#### mark_task_as_completed
The function is a view in Django that marks a task as completed by setting its is_completed field to True. It also checks if all tasks associated with the task's project are completed, and if so, it sets the project's is_completed field to True. The function finally redirects the user to the task list.  

     
### Teams URL's

#### teams
The teams function is a view in Django that loads the teams page. It retrieves the current user from the request object and retrieve all the teams that the user is a member of. The teams are then passed as a context to the render method to be displayed in the teams template.

#### teams_projects 
This function displays all the projects associated with a specific team. It takes the team's ID and retrieves the team and its projects. The projects and a message with the team's name are then displayed in the index template.

#### create_team
The create_team function creates a new team. If a GET request is made, it retrieves all registered users and displays them in a list. If a POST request is made, the function retrieves the team name, objective, color, and members from the request, creates a new team object with these properties, saves it to the database, and returns a page showing all teams including the newly created one.


#### manage_team
This code defines a path that handles the "manage_team" request. When this path is hit, the following actions are performed:
It fetches the team object using the id passed in the URL.
It retrieves a list of all users using the User model.
It returns a rendered HTML template "network/manage_team.html", passing the team and all_users data.

#### add_member
The add_member function adds a user to a specific team. It retrieves the specified user and team by their IDs, then adds the user to the team's member list. Finally, it returns a JSON response containing an updated list of all users.

#### remove_member 
The remove_member function removes a user from a specific team. It retrieves the specified user and team by their IDs, then removes the user from the team's member list. Finally, it returns a JSON response containing an updated list of all users.