from django.core.management.base import BaseCommand
from pml_app.models import Task, Manager

class Command(BaseCommand):
    help = 'Create sample tasks for testing'

    def handle(self, *args, **options):
        # Get managers from database
        managers = Manager.objects.all()
        if not managers.exists():
            self.stdout.write(self.style.ERROR('No managers found in database. Please create managers first.'))
            return

        # Create sample tasks
        sample_tasks = [
            {
                'task_name': 'Develop User Authentication',
                'manager': managers.first(),
                'team_member_id': 1
            },
            {
                'task_name': 'Design Database Schema',
                'manager': managers.first(),
                'team_member_id': 2
            },
            {
                'task_name': 'Create API Endpoints',
                'manager': managers.last() if managers.count() > 1 else managers.first(),
                'team_member_id': 1
            },
            {
                'task_name': 'Implement Frontend Components',
                'manager': managers.last() if managers.count() > 1 else managers.first(),
                'team_member_id': 2
            }
        ]

        for task_data in sample_tasks:
            task, created = Task.objects.get_or_create(
                task_name=task_data['task_name'],
                defaults={
                    'manager': task_data['manager'],
                    'team_member_id': task_data['team_member_id']
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created task: {task.task_name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Task already exists: {task.task_name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Task creation completed. Total tasks: {Task.objects.count()}')
        )