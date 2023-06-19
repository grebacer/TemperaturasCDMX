### this file will initiate the pipeline, first steps gets the data from service
#url1 = 'https://datos.cdmx.gob.mx/dataset/bae265a8-d1f6-4614-b399-4184bc93e027/resource/deb5c583-84e2-4e07-a706-1b3a0dbc99b0/download/limite-de-las-alcaldas.json'
import pandas as pd
import requests

def pull_data(url):
  response = requests.get(url)
  data_json = response.json() 
  return data_json

def json_to_pd(data_json,data_string):
  

  return pd.json_normalize(data_cdmx[data_string])
  
  
