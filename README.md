**Introduction:**
- This complete **backend-only web application** uses Django, Python, HTML, and CSS. Concepts of AJAX and Javascript are also included in the project.
- There are two types of users accessing the application for their purposes. 
- The web application is focused on managing the different receipes, focused mainly on the restaurant workers to simplify their work process. 

**Features:**
- There are two types of workers in the restaurant, one is the admin - who will manage the 
products and ingredients available for any particular receipe and update the list of currently available receipes in the dashboard.
- The other type of user is the Member, who can only access the Members Dashboard Page. On the Member's Dashboard Page, the users can take up the receipes, based on the order received, and by calculating the total amount, they can proceed to apply for payment. 
- The admin users are the only ones who can update and delete the list of receipes. They are the ones who can alter the available receipes list.

**Technologies Used:**
- HTML 
- CSS
- Python
- Django
- AJAX
- Javascript
- Bootstrap

**Screenshots:**

<img width="948" alt="register" src="https://github.com/amvi234/manifest-reciepes/assets/67577861/b62294e7-26d5-4559-a7bb-e8482fc9efbc">
<img width="959" alt="login" src="https://github.com/amvi234/manifest-reciepes/assets/67577861/0bd2f1cb-0eba-49b5-963e-233c5cef9dee">
<img width="947" alt="admin" src="https://github.com/amvi234/manifest-reciepes/assets/67577861/14a20566-c339-4c27-aa56-1e3328905129">
<img width="959" alt="receipes" src="https://github.com/amvi234/manifest-reciepes/assets/67577861/e821a447-0a41-4bbe-aec7-51f591245e9d">
<img width="942" alt="member" src="https://github.com/amvi234/manifest-reciepes/assets/67577861/421aebe7-5cb8-4538-9ed2-41f00be1ca15">
<img width="943" alt="total" src="https://github.com/amvi234/manifest-reciepes/assets/67577861/d79ae47d-a6fb-4472-ace0-a49aa7c360e0">
<img width="943" alt="payment" src="https://github.com/amvi234/manifest-reciepes/assets/67577861/5af18375-284a-4f42-8b9e-2f8e4edd3b60">
<img width="959" alt="upiid" src="https://github.com/amvi234/manifest-reciepes/assets/67577861/f19446f6-4710-4292-92fc-7efb494f9541">

**Requirements before setup of the project:**
1. A stable version of Python installed on your PC.
2. An interactive running terminal.

**To get this project running, follow the below steps:**
1. Clone the repository.
2. Move to the manifest-receipes directory in your terminal.
3. Run `pip install virtualenv` - a virtual environment will be created to start your installations. 
4. Now, run `pip install django` - this will install Django for the development.
5. Now, move to the base directory and run `pipenv shell`.
6. Then, run `python manage.py runserver` to run your project.
7. In your browser, navigate to this URL - http://localhost:8000/
8. Now, you are all ready to work on this project.

**Future Enhancements:**
1. Enable a full-functioning Payment Gateway.
2. Allow handling of admin and member user workflow much cleaner.
3. Interactive Receipe images for better visualization.
4. Implement a more comprehensive Receipe search functionality.
