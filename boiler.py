# import urllib library
from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://explorer.natureserve.org/api/data/taxon/ELEMENT_GLOBAL.2.140000"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
  
# print the json response
# print(data_json)

# parse_json
print('elementGlobalId: ' + str(data_json['elementGlobalId']) + ' '
      + 'type : ' + str(data_json["nameCategory"]["nameCategoryDescEn"])

)