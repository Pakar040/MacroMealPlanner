# MacroMealPlanner
App that specifies how much to eat to reach macros

## Database Migrations
Django uses migrations to apply changes to the database schema. Follow these steps to make and apply migrations:

### 1. Make Migrations
Detect changes in models and create migration files:
```
python manage.py makemigrations
```

### 2. Apply Migrations
Apply the migrations to the database:
```
python manage.py migrate
```

## Running the Server
To run the development server and view the application:
```
python manage.py runserver
```
Access the application at http://127.0.0.1:8000/ in your web browser.

## Additional Commands
### Creating a Superuser
Create an admin user to access the Django admin interface:
```
python manage.py createsuperuser
```

### Updating Environmnet
Add to the `environment.yml` file for new dependancies

To update your environment match the depedancies:
```
conda env update -f environment.yml
```