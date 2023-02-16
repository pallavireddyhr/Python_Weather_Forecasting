#Importing requests module, which allows us to send http requests easily
import requests

#Asking User to Enter the city for which the user wants to know Weather status
city=input("Enter The City: ")

#Printing The City Name
print("Presenting Weather Reports for "+city+" city: ")

#Making use of 'wttr' ,It's a Console oriented Weather Forecast Service
url='https://wttr.in/{}'.format(city)

# Making use of 'requests' module to send http requests
result=requests.get(url)

#Printing The Weather Forecast of the specified city
print(result.text)

