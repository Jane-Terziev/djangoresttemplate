This is a django rest template project.

When changing the project name, you might need to do some changes:
1. Change the settings file path in manage.py, wsgi.py and asgi.py files with the new project name.
2. Change the database default settings to your db username and password.
3. Install all the packages in requirements.txt with <b>pip install -r requirements.txt<br>

For develop/staging/production servers, you might need to pass some environment variables. The settings file that is 
used on start depends on the ENVIRONMENT variable. This variable takes develop/staging/production values. If no value
is passed, the base.py is set as default settings file.

Environment variables that need to be passed:
1. ENVIRONMENT ("develop", "staging", "production"")
2. DATABASE_NAME
3. DATABASE_HOST
4. DATABASE_USER
5. DATABASE_PASSWORD
6. DATABASE_PORT
7. SMTP_EMAIL
8. SMTP_PASSWORD
9. SECRET_KEY