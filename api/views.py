from rest_framework import generics

from .models import TimeUsage
from .serializers import TimeUsageSerializer


class ListTimeSpent(generics.GenericAPIView):
    """
    View to list usage of time statistics for
    each country
    """

    serializer_class = TimeUsageSerializer
    lookup_field = "uuid"

    def get_queryset(self, request):
        country = request.query_params["country"]
        if country is None:
            queryset = TimeUsage.objects.all()
        else:
            queryset = TimeUsage.objects.filter(country=country)
        return queryset
