import requests
from twilio.rest import Client


OWN_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"  ##5 days data per 3 hour 

#twilio details/demo account
#can save the below details as environment variables for security
account_sid = "ACb395f4340abc099e6fbffcb1ff018d08"
auth_token = "ba9adbab774994c0cab1349c41eeeae5"



app_id= "a78968366441aa0fc85eb472a42fc47d"
latitude = 26.200603
longitude = 92.937576

weather_parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": app_id,
}


response = requests.get(OWN_Endpoint, params=weather_parameters)
weather_data = response.json()


#Check if it will rain(id= 2xx,3xx,5xx,6xx are rain or likely worst)
id_data_list = []
for i in range(0,4): #need data for 12 hours. since data is per 3 hours so first 4 data is enough
    id_data = weather_data['list'][i]['weather'][0]['id']
    id_data_list.append(id_data)


is_rain = False

for item in id_data_list:
    if item<700:
        is_rain = True
    
if is_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="It's gonna rain today, Don't forget to bring an umbrella",
                     from_='+12029785045',
                     to='+916002059806'
                 )
    print(message.status)
