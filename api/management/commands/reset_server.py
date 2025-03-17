from django.core.management.base import BaseCommand
import os
import sys


class Command(BaseCommand):
    help = 'Resets the database and starts the server'

    def handle(self, *args, **kwargs):
        self.stdout.write("Resetting database...")

        # Delete migrations
        os.system(
            "find . -path '*/migrations/*.py' -not -name '__init__.py' -delete")
        os.system("find . -path '*/migrations/*.pyc' -delete")

        # Reset database and apply migrations using the correct Python executable
        python_exec = sys.executable
        os.system(f"{python_exec} manage.py flush --no-input")
        os.system(f"{python_exec} manage.py makemigrations")
        os.system(f"{python_exec} manage.py migrate")

        self.stdout.write(self.style.SUCCESS(
            "Database reset complete. Starting server..."))
        os.system(f"{python_exec} manage.py runserver")
