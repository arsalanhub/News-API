from rest_framework import decorators, permissions
from rest_framework.response import Response
from bs4 import BeautifulSoup
import urllib.request

@decorators.api_view(['GET'])   
@decorators.permission_classes([permissions.AllowAny])
def getEntertainmentNews(request):
    response = urllib.request.urlopen("https://indianexpress.com/section/entertainment/page/3/")
    page_source = response.read()

    soup = BeautifulSoup(page_source, "html.parser")

    data = soup.find_all("div", class_="title")
    dataArr = []
    for i in data:
        dataDict = dict()
        dataDict["title"] = i.a.text
        dataArr.append(dataDict)
    return Response(dataArr, 200)