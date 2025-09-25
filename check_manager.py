#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pml.settings')
django.setup()

# Now we can import Django models
from pml_app.models import Manager

# Get all manager records
managers = Manager.objects.all()
print(f"Total managers found: {len(managers)}")

# Display manager details
for manager in managers:
    print(f"Manager ID: {manager.manager_id}, Name: {manager.name}, Password: {manager.password}")

# If no managers found, let's create a test manager
if len(managers) == 0:
    print("No managers found. Creating a test manager...")
    new_manager = Manager(manager_id=101, name="Test Manager", password="manager123")
    new_manager.save()
    print(f"Created test manager with ID: {new_manager.manager_id}")
