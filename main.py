# import urllib library
from urllib.request import urlopen
# import json
import json

counter = 0

def checker(value):
  
  try:
    url = "https://explorer.natureserve.org/api/data/taxon/ELEMENT_GLOBAL.2." + str(value)
    global counter
    counter += 1
    response = urlopen(url)
  except Exception:
    print('Invalid Link')
    return
  data_json = json.loads(response.read())

  elementGlobalId = str(data_json['elementGlobalId']) or  'Does not Exist'
  nameCategory = str(data_json["nameCategory"]["nameCategoryDescEn"]) or 'Does not Exist'
  

  print('counter: ' + str(counter) + ' ' + 'elementGlobalId: ' + elementGlobalId + ' ' + 'type : ' + nameCategory)

# print(checker(147299)) # Aloe Vera

# print(checker(299)) # Error Plant

# Animal Range Apporixamtion (100002 - 125003)

# Plant Range Approximation (125003 - 161769)
  # Non-Vascular Plants and Fungus (125003 - 127851)
  # Vascular Plant [The focus of our app] (127851-161769)


for i in range(127850,162000):
  checker(i)