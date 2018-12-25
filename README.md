# Doctor-Finder

## Installation
1. Install virtualenv 
```bash
    pip3 install virtualenv
```
2. Get into to the folder doctor-tracker and run the command to activate the virtual env
```bash
    source bin/ativate
```
3. Install all the dependencies by executing the requirements.txt file
```bash
    pip3 install -r requirements.txt
```
4. Create a database according to the configurations mentioned in **Settings.py** and change the configuration according to the mysql on the system.

5. After creating the database, migrate all the tables by running the following commands.
```bash
    python3 manage.py makemigrations
    
    python3 manage.py migrate
```

6. Run the server
```bash
    python3 manage.py runserver
```