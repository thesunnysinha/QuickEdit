import subprocess
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Run Gunicorn with Uvicorn for Django application'

    def add_arguments(self, parser):
        parser.add_argument('--port', type=int, default=8000, help='Specify the port for Gunicorn to bind to')

    def handle(self, *args, **options):
        port = options['port']

        # Start Gunicorn with Uvicorn
        self.stdout.write(self.style.SUCCESS(f"Starting Gunicorn with Uvicorn on port {port}"))

        proxy_allow_ips = '*'

        gunicorn_command = [
            'gunicorn',
            '--bind', f'0.0.0.0:{port}',
            '--timeout', '240',
            '--workers', '3',
            '--proxy-allow-from', proxy_allow_ips,
            '--worker-class', 'uvicorn.workers.UvicornWorker',
            'QuickEdit.asgi:application',
            '--log-level=debug',
            '--log-file=-',
            '--access-logfile=-',
            '--error-logfile=-',
            '--capture-output',
        ]

        try:
            subprocess.run(gunicorn_command, check=True)
        except subprocess.CalledProcessError as e:
            self.stderr.write(self.style.ERROR(f"Error starting Gunicorn with Uvicorn: {e}"))

        self.stdout.write(self.style.SUCCESS(f"Started Gunicorn with Uvicorn on port {port}"))
