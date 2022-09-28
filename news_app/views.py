from rest_framework import decorators, permissions
from rest_framework.response import Response

@decorators.api_view(['GET'])   
@decorators.permission_classes([permissions.AllowAny])
def getEntertainmentNews(request):
    print("Inside Entertainment Function")