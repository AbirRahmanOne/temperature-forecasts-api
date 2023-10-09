import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tfplatfrom.utils.utils import fetch_next_seven_days_forecast_data,fetch_forecast_data_day_wise

logger = logging.getLogger(__name__)


class CoolestTenDistrictsAPIView(APIView):

    @staticmethod
    def get(request):
        try:

            forecast_data = fetch_next_seven_days_forecast_data()
            sorted(forecast_data, key=lambda x: x['avg_temp'], reverse=True)
            coolest_districts = []
            for data in forecast_data[:10]:
                coolest_districts.append(data['district_name'])
            return Response({"message": "success", "data": coolest_districts}, status=status.HTTP_200_OK)

        except Exception as ex:
            logger.error(str(ex), exc_info=True)
        return Response({"message": "Serve error!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CompareTemperatureAPIView(APIView):

    @staticmethod
    def post(request):
        try:
            friend_lat = request.data.get('src_lat', None)
            friend_long = request.data.get('src_long', None)
            travel_date = request.data.get('travel_date', None)

            travel_lat = request.data.get('travel_lat', None)
            travel_long = request.data.get('travel_long', None)

            friend_temp_forecast_data = fetch_forecast_data_day_wise(friend_lat, friend_long, travel_date)
            avg_temp_at_friend_location = (sum(friend_temp_forecast_data) / 7.00)
            destination_temp_forecast_data = fetch_forecast_data_day_wise(travel_lat, travel_long, travel_date)
            avg_temp_at_des_location = (sum(destination_temp_forecast_data)/ 7.00)

            if avg_temp_at_friend_location > avg_temp_at_des_location:
                return Response({"message": "You Should Travel"}, status=status.HTTP_200_OK)

            else:
                return Response({"message": "Too Hot! Shouldn't travel"}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex), exc_info=True)
        return Response({"message": "Serve error!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
