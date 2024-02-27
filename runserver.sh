
#!/bin/bash
# Get the directory where the script is located
script_directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Navigate to the script's directory
cd "$script_directory"

read -p "Do you want to switch your branch to latest 'main'? (y/n): " branch_answer

if [ "$branch_answer" == "y" ]; then
    git stash

    git checkout main

    git pull origin main

else
    echo "'branch switch' skipped."
fi

# Navigate to the backend directory
cd "$script_directory/backend"

python manage.py deletemigrations

python manage.py makemigrations grayscaling QuickEditApp imageEnhancement edgeDetection skewCorrection textExtractor fileConverter linkShortener

python manage.py setupapplication

# Start Django development server on the assigned port

read -p "Do you want to run 'gunicorn'? (y/n): " gunicorn_answer

if [ "$gunicorn_answer" == "y" ]; then

    python manage.py rungunicorn

else
    python manage.py runserver 0.0.0.0:8000
fi
