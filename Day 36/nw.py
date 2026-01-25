import requests
import os
from twilio.rest import Client
key = os.environ.get("token")

account_sid = 'AC97e7aa54cd9fe9c69ad07fef7c56369b'
auth_token = os.environ.get("auth")
client = Client(account_sid, auth_token)


param = {
    "lat" : 51.489935,
    "lon" : -0.851912,
    "appid" : key
}
api = "https://pro.openweathermap.org/data/2.5/forecast"
response = requests.get(api,params=param)
response.raise_for_status()
ans = response.json()
for i in range(len(ans["list"])):
    if ans["list"][i]["weather"][0]["id"] < 700:
        # message = client.messages.create(
        #     messaging_service_sid='MGccc212e0e55c72f8debce48369af8891',
        #     body="It's goin to rain",
        #     to="+919315206806",
        print("hello")