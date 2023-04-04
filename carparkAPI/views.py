from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from requests.structures import CaseInsensitiveDict

# Create your views here.
def get_token():
    url = "https://www.ura.gov.sg/uraDataService/insertNewToken.action"
    headers = CaseInsensitiveDict()
    headers["AccessKey"] = "70c5cc64-7065-40e8-9921-3b068b8f237e"
    response = requests.get(url, headers=headers)
    response_data = response.json()
    return response_data["Result"]

@api_view(['GET'])
def carpark(request):
    token = get_token()
    url = "https://www.ura.gov.sg/uraDataService/invokeUraDS?service=Car_Park_Availability"
    headers = CaseInsensitiveDict()
    headers["AccessKey"] = "70c5cc64-7065-40e8-9921-3b068b8f237e"
    headers["Token"] = token
    response = requests.get(url, headers=headers)
    response_data = response.json()
    print(response.status_code)
    return Response(response_data)