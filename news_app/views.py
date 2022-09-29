from rest_framework import decorators, permissions
from rest_framework.response import Response
from bs4 import BeautifulSoup
import urllib.request

@decorators.api_view(['GET'])   
@decorators.permission_classes([permissions.AllowAny])
def getEntertainmentNews(request):
    dataArr = []
    for pageNumber in range(1, 3, 1):
        response = urllib.request.urlopen("https://indianexpress.com/section/entertainment/page/{}/".format(pageNumber))
        page_source = response.read()

        soup = BeautifulSoup(page_source, "html.parser")

        data = soup.find_all("div", class_="articles")

        for i in data:
            dataDict = dict()
            dataDict["title"] = i.div.find_next_sibling("div").a.text
            dataDict["image"] = i.div.a.img["data-lazy-src"]
            dataDict["body"] = i.p.text
            dataArr.append(dataDict)
    return Response(dataArr, 200)