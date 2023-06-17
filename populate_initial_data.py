
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dynamic_menu.settings')
django.setup()

from django.contrib.auth.models import Group #, Permission
from django.db import connection
from menus.models import  District, Person
from django.core.management.base import BaseCommand

class Command(BaseCommand):


    def create_districts(self):
        # Check if District instances exist
        if not District.objects.exists():
            # Create District instances
            district_data = [
                {'id': 2, 'name': 'Λευκωσία'},
                {'id': 3, 'name': 'Αμμόχωστος'},
                {'id': 4, 'name': 'Λάρνακα'},
                {'id': 5, 'name': 'Λεμεσός'},
                {'id': 6, 'name': 'Πάφος'},
                # Add more districts as needed
            ]

            for data in district_data:
                district_id = data.get('id')
                district_name = data.get('name')

                if district_id or district_name:
                    district_kwargs = {}
                    if district_id:
                        district_kwargs['id'] = district_id
                    if district_name:
                        district_kwargs['name'] = district_name

                    District.objects.create(**district_kwargs)

    def create_people(self):
        for district in District.objects.all():
            for i in range(1, 4):
                Person.objects.create(name=district.name + str(i), district=district)

    def reset_primary_key_sequence(self,table_name):
        with connection.cursor() as cursor:
            # cursor.execute(f"ALTER SEQUENCE {table_name}_id_seq RESTART WITH 1;")
            cursor.execute(f"UPDATE 'sqlite_sequence' SET 'seq' = 0 WHERE 'name' = '{table_name}';")


    def handle(self, *args, **options):

        District.objects.all().delete()
        self.reset_primary_key_sequence('menus_district')
        self.create_districts()
        print('Districts created')
        Person.objects.all().delete()
        self.reset_primary_key_sequence('menus_people')
        self.create_people()
        print('Persons created')



if __name__ == '__main__':
    # run handle() method of Command class
    Command().handle()
    