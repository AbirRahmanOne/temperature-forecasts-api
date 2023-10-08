import logging

from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from tfplatfrom.utils.utils import fetch_next_seven_days_forecast_data
from tfplatfrom.models import District

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


