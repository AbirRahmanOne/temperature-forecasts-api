from urllib.request import urlopen
import json
from tfplatfrom.models import District


def fetch_forecast_data(lang, long):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lang}&longitude={long}&hourly=temperature_2m&current_weather=true"
    response = urlopen(base_url)
    forecast_data_json = json.loads(response.read())

    hourly_temp_data = forecast_data_json['hourly']['temperature_2m']

    temp_list_at_2m = []
    day = 14
    for i in range(7):
        if i != 0:
            day += 24
        temp_list_at_2m.append(hourly_temp_data[day])

    return temp_list_at_2m


def fetch_next_seven_days_forecast_data():

    districts_qs = District.objects.all()

    coolest_ten_dis = []
    for district in districts_qs:
        temp_at_2m = fetch_forecast_data(district.lat, district.long)
        avg_temp = (sum(temp_at_2m) / 7.00)
        coolest_ten_dis.append({"district_name": district.name, "avg_temp": avg_temp})

    return coolest_ten_dis
