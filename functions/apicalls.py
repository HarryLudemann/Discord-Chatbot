# Import Modules
import requests
import json
#import Api python packages
from foaas import fuck

def get_inspire_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  print("bot:", quote)
  return(quote)

def get_foass(author): 
  response = fuck.random(from_=author).text
  print("bot:", response)
  return response


if (__name__ == "__main__"):
  get_inspire_quote()
  get_foass('Hazzah')