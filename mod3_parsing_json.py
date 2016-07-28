import urllib2
import config
import requests
import json
'''
Created on Jul 26, 2016

@author: rafacarv
'''
#This is where you program starts.
if __name__ == '__main__':
    
    #Greet the user by writing something on the console.
    print ("Hello! Welcome!")
    
    #Asks for an input
    city = raw_input("In which city are you? ")
    
    #Builds the URL by adding the city name and the API's key
    url = "http://api.openweathermap.org/data/2.5/weather?mode=json&units=metric&q={}&APPID={}".format(urllib2.quote(city), config.weather_api_key)
    
    #Use that URL and request from the API server.
    api_response = requests.get(url)
    
    #Get the json-encoded content from response
    response_json = api_response.json()
    
    #print (json.dumps(response_json,indent=4))
    
    #Parsing the information to make sense out of it.
    temp = response_json["main"]["temp"]
    temp_min = response_json["main"]["temp_min"]
    temp_max = response_json["main"]["temp_max"]
    
    #Print an information that makes sense.
    print ("The temperature in {} is currently {} (Max: {} / Min: {})".format(city, temp, temp_max, temp_min))