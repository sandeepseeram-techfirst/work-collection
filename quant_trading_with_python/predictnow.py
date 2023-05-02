# TO BEGIN ANY WORK WITH PREDICTNOW.AI CLIENT, WE START BY IMPORTING AND CREATING A CLASS INSTANCE
from predictnow.pdapi import PredictNowClient
import pandas as pd
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 
api_host = "http://12.34.567.890:1000" # our SaaS server
username = "helloWorld"
email = "helloWorld@yourmail.com"
client = PredictNowClient(api_host,api_key)
# You will need to edit this input dataset file path and labelname!
file_path = 'my_amazing_features.xlsx'
labelname = 'Next_day_strategy_return'



 