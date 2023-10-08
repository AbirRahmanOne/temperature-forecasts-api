from urllib.request import urlopen
from django.core.management.base import BaseCommand
import json

# importing District model
from tfplatfrom.models import District

# Api urls
base_url = "https://raw.githubusercontent.com/strativ-dev/technical-screening-test/main/bd-districts.json"


def add_districts():
    response = urlopen(base_url)
    data_json = json.loads(response.read())

    #Data already added
    if District.objects.count():
        return 0

    # Error Handler
    # if response.status_code != 200:
    #     return 0

    districts_data = data_json['districts']

    for data in districts_data:
        district = District(
            division_id=data['division_id'],
            name=data['name'],
            bn_name=data['bn_name'],
            lat=data['lat'],
            long=data['long'],

        )
        district.save()
        total_add_countries = District.objects.all()

    return len(total_add_countries)


def clear_data():
    District.objects.all().delete()


class Command(BaseCommand):

    def handle(self, *args, **options):
        # clear_data()
        total_districts = add_districts()
        print(f"Successfully added, {total_districts} districts data.")



