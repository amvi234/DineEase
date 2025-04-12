**Problem Statement:**
Often restaurants have the issue of maintaining thr transactions. To solve the common issue of Point of Sale(POS) System. I have developed a dashboard and restaurant items listed and added by admins. THe staff users will be responsible for the payment. Here with the integrated Razorpay Payment Gateway implementation, users can monitor and analyze each and every transactions easily.

**Screen Recording:**

[Screencast from 12-04-25 10:03:08 AM IST.webm](https://github.com/user-attachments/assets/d370fe85-68a8-4fbe-838c-d2f726eb8527)
[Screencast from 12-04-25 10:04:19 AM IST.webm](https://github.com/user-attachments/assets/3efbf534-e82e-4cce-9db0-ab5aac349369)

**Introduction:**
- This complete **backend-only web application** uses Django, Python, HTML, and CSS. Concepts of AJAX and Javascript are also included in the project.
- There are two types of users accessing the application for their purposes. 
- The web application is focused on managing the different recipes, focused mainly on the restaurant workers to simplify their work process. 

**Features:**
- There are two types of workers in the restaurant, one is the admin - who will manage the 
products and ingredients available for any particular recipe and update the list of currently available recipes in the dashboard.
- The other type of user is the Member, who can only access the Members Dashboard Page. On the Member's Dashboard Page, the users can take up the recipes, based on the order received, and by calculating the total amount, they can proceed to apply for payment. 
- The admin users are the only ones who can update and delete the list of recipes. They are the ones who can alter the available recipes list.
- There is a razorpay payment integration setup, which makes it easy for the admins to monitor and manage the Point of Sale system problem statement.

**Technologies Used:**
- HTML 
- CSS
- Python
- Django
- AJAX
- Javascript
- Bootstrap
- Dotenv
- Razorpay

**Requirements before setup of the project:**
1. A stable version of Python installed on your PC.
2. An interactive running terminal.

**To get this project running, follow the below steps:**
1. Clone the repository.
2. Move to the DineEase directory in your terminal. 
3. Run `pip install virtualenv` - a virtual environment will be created to start your installations. 
4. Now, run `pip install django`, `pip install razorpay` and `pip install dotenv` - this will install necessary packages for the development.
5. Run`sudo apt install pipenv` to start to shell command.
6. Now, move to the base directory and run `pipenv shell`.
7. Then, run `python manage.py runserver` to run your project.
8. In your browser, navigate to this URL - http://localhost:8000/
9. Now, you are all ready to work on this project.

**Future Enhancements:**
1. Implement a more comprehensive Recipe search functionality.
2. Add user's details at top left corner.

