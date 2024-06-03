from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Restore PostgreSQL database from backup'

    def handle(self, *args, **kwargs):
        # PostgreSQLRestore instance initialization
        database_name = "quest_ans"  
        username = "postgres" 
        password = "1234" 
        input_file = "db_backups"  
        restore = PostgreSQLRestore(database_name, username, password, input_file)

        # Execute restore
        restore.restore()

class PostgreSQLRestore:
    def __init__(self, database, username, password, input_file):
        self.database = database
        self.username = username
        self.password = password
        self.input_file = input_file

    def restore(self):
        # Set the PGPASSWORD environment variable
        os.environ['PGPASSWORD'] = self.password

        # Construct the command string for restoring the database
        command = (
            f"pg_restore -U {self.username} -d {self.database} "
            f"-c {self.input_file}"
        )

        # Execute the command using os.system
        os.system(command)
