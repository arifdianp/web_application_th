# Risk Management Database
### Objective: Design and implement a simple proof-of-concept web application that serves two types of users:<br>
•	**Project Manager (PM)**: The project manager is in charge of conducting a risk assessment of their application project. He or she uses the web application to access the database of risk scenarios. If they find a risk scenario that can apply to their project, they add it to their risk table. They can also state whether the risk scenario has been mitigated.<br>

•	**Risk Consultant (RC)**: The risk consultant has a global overview of all the risk tables created by the project manager(s). He or she uses the web application to view the risk tables created by the project managers and collaboratively work with the project managers to update the risk tables.<br>


### Features:<br>
•	**User sign-in**: A PM or RC should be able to login and see different views of the application based on their role.<br>

•	**View risk scenario database**: Both the PM and RC should be able to view the risk scenario database.<br>

•	**Search risk scenario database**: The RC should be able to search the risk scenarios in the database by name and keywords (in the risk scenario description or mitigation strategy).<br>

•	**Edit mitigation progress**: The PM should be able to edit the risk scenario in the risk table to indicate how much the risk has been mitigated. A risk can be either (1) not mitigated, (2) partially mitigated, or (3) fully mitigated.<br>

•	**Create risk table**: The PM should be able to create a risk table by adding/deleting a risk scenario from the risk scenario database.<br>

•	**Update risk tables**: The PM and RC should be able to share the same view of the risk table created by the PM and be able to update that table. The updates should be visible to each user as a notification.<br>

### Documentations on how to run:<br>

1. Install Latest Version of Python  
   > Python==3.10.0

2. Installing the virtual environment
   > pip3 install pipenv

3. Installing latest version of django
   > pipenv install django

4. Run the virtual environment
   > pipenv shell

5. migration and running the django app
  > python manage.py makemigrations <br>
  > python manage.py migrate <br>
  > python manage.py runserver <br>

### Testing using Selenium
1. pip install selenium
2. install webdriver chrome selenium (check chrome version for compatibility)
    setx PATH "%PATH%;C:\Users\ADP\web_application_th\"
