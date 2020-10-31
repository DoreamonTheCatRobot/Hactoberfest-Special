
# Take input of which city to pull weather info about using Visual Crossing Weather API
# Display the high and low temperature for the day and the current weather condition
# Collect historical data using same API; Average high temps and low temps, and display how much 
# warmer or colder the city is today than the past 5 year average. 
# 
 

import datetime
import pyowm
import requests
import json
from dateutil.relativedelta import relativedelta
from statistics import mean
import os




def main():
  print("Welcome to the weather trends app! \n\nThis app will give you today's weather highlights in your city, and show you how much warmer or cooler the day's temperatures are compared with the temperatures on the same day over the last 5 years. \n\n")
  destination1 = input("Which city are you searching?\n")
  destination2 = " "+ input("What is the 2 character state abbreviation?\n")
  location = ("'"+destination1+ destination2+",USA'")

  print("Loading weather data for "+location.replace("'","")+"...")
  date_time = datetime.datetime.now()
  currWeather = getCurrWeather(location)
  jprint(currWeather)
  #jprint(currWeather)  ## For reviewing the return
  histWeather = getHistWeather(location, date_time)

  output(currWeather, histWeather, date_time, location)
  



# Get current data 
def getCurrWeather(location): 
  url = "https://visual-crossing-weather.p.rapidapi.com/forecast"
  querystring = {"contentType":"json","shortColumnNames":"false","unitGroup":"us","location":location,"aggregateHours":"24"}
  headers = {
      'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
      'x-rapidapi-key': str(input("API Key: "))
      }
  return requests.request("GET", url, headers=headers, params=querystring).json()




# Get Historical Data
def getHistWeather(location, date_time):
  url = "https://visual-crossing-weather.p.rapidapi.com/history"
  highs = []
  lows = []
  years = [1,2,3,4,5]

  yesterdayStart = date_time - relativedelta(day=1)
  yesterStart= str(yesterdayStart).replace(" ","T").split(".")[0]
  yesterEnd = str(yesterdayStart).replace(" ","T")[0 : 11]+"11:59:59"
  
  querystring = {"contentType":"json","shortColumnNames":"false","startDateTime":yesterdayStart,"aggregateHours":"24","location":location,"endDateTime":yesterEnd,"unitGroup":"us"}
  headers = {
      'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
      'x-rapidapi-key': str(input("API Key: "))
      }

  for y in years:
    newStart = date_time - relativedelta(years=y)
    startDate= str(newStart).replace(" ","T").split(".")[0]
    endDate = str(newStart).replace(" ","T")[0 : 11]+"11:59:59"
  
    querystring = {"contentType":"json","shortColumnNames":"false","startDateTime":startDate,"aggregateHours":"24","location":location,"endDateTime":endDate,"unitGroup":"us"}
    headers = {
        'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
        'x-rapidapi-key': "6ddad74814msh2669d30ecf9c405p141986jsn865d1cfcae33"
        }


    max = requests.request("GET", url, headers=headers, params=querystring).json()["locations"][location]['values'][0]['maxt']
    min = requests.request("GET", url, headers=headers, params=querystring).json()["locations"][location]['values'][0]['mint']
    if max != None:
      highs.append(max)
    if min != None:
      lows.append(min)

  return [mean(highs) , mean(lows)]






def output(currWeather, histWeather, today, location): 
  print("\n\n\nHere is the weather report for " + location.replace("'","") +" for"+ today.strftime(" %m/%d/%Y: \n"))

  conditions = currWeather["locations"][location]['values'][0]['conditions']
  maxt = currWeather["locations"][location]['values'][0]['maxt']
  mint = currWeather["locations"][location]['values'][0]['mint']
  print("Today will be "+ conditions.lower() + " with a high of " + str(int(round(maxt,0)))+"F degrees and a low of "+str(int(round(mint,0))) +"F degrees.\n")

  outputCompareHigh = ""
  outputCompareLow = ""
  highcompare = maxt-histWeather[0]
  lowcompare = mint-histWeather[1]
  if highcompare >0:
    outputCompareHigh = "F warmer than the 5 year average "
  else:
    outputCompareHigh = "F colder than the 5 year average "

  if highcompare >0:
    outputCompareLow = "F warmer than the 5 year average."
  else:
    outputCompareLow = "F colder than the 5 year average."

  print("Today's high is " + str(int(round(abs(highcompare), 0)))+ outputCompareHigh+ "and the low is "+ str(int(round(abs(lowcompare), 0)))+outputCompareLow)
        



  print(os.getcwd())


 #Utility method for pretty printing and reviewing the json response of API call
def jprint(obj):
  prettyText = json.dumps(obj, sort_keys=True, indent=4)
  print(prettyText)



if __name__ == "__main__":
  main()