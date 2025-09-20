#!/usr/bin/env python
import os
import sys
import django

# Add backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend'))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Diploma_Cracker_v1.settings')
django.setup()

from testapp.models import Subject

print("=== EXISTING SUBJECTS IN DATABASE ===")
subjects = Subject.objects.all()
for subject in subjects:
    print(f"ID: {subject.id}, Name: '{subject.sub_name}', Type: {subject.sub_type}")

print(f"\nTotal subjects: {subjects.count()}")