from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
import requests
from requests.structures import CaseInsensitiveDict
import json
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny

def get_token():
    url = 'https://www.ura.gov.sg/uraDataService/insertNewToken.action'
    headers = CaseInsensitiveDict()
    headers= {
        "User-Agent": "Myhost",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept-Language": "en-US,en;q=0.5",
        "AccessKey": "70c5cc64-7065-40e8-9921-3b068b8f237e"
    }
    response = requests.get(url, headers=headers)
    response_data = response.text
    return response_data


#/api/carpark/
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def carpark(request):
    tokenResponse = get_token()
    tokenResponseJson = json.loads(tokenResponse)
    token = tokenResponseJson["Result"]
    url = "https://www.ura.gov.sg/uraDataService/invokeUraDS?service=Car_Park_Availability"
    headers = CaseInsensitiveDict()
    headers= {
        "User-Agent": "Myhost",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept-Language": "en-US,en;q=0.5",
        "AccessKey": "70c5cc64-7065-40e8-9921-3b068b8f237e",
        "Token": token
    }
    response = requests.get(url, headers=headers)
    response_data = response.json()
    return Response(response_data)

#/api/taxi/
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def taxiAvailability(request):
    url = "https://api.data.gov.sg/v1/transport/taxi-availability"
    response = requests.get(url)
    response_data = response.json()
    return Response(response_data)