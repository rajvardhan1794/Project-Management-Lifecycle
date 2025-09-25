from django.core.management.base import BaseCommand
from pml_app.models import Admin, Manager, TeamMember

class Command(BaseCommand):
    help = 'Create initial test users'

    def handle(self, *args, **kwargs):
        # Create admin if it doesn't exist
        if not Admin.objects.filter(admin_id=1).exists():
            Admin.objects.create(
                admin_id=1,
                name="admin",
                password="admin123"
            )
            self.stdout.write(self.style.SUCCESS('Admin created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Admin already exists'))
            
        # Create manager if it doesn't exist
        if not Manager.objects.filter(manager_id=1).exists():
            Manager.objects.create(
                manager_id=1,
                name="manager",
                password="manager123"
            )
            self.stdout.write(self.style.SUCCESS('Manager created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Manager already exists'))
            
        # Create team member if it doesn't exist
        if not TeamMember.objects.filter(team_member_id=1).exists():
            TeamMember.objects.create(
                team_member_id=1,
                team_member_name="team",
                password="team123"
            )
            self.stdout.write(self.style.SUCCESS('Team Member created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Team Member already exists'))
