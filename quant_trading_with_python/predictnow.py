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

import os
 
params = {'timeseries': 'yes', 'type': 'regression', 'feature_selection': 'none', 'analysis': 'none', 'boost': 'gbdt', 'testsize': '0.2', 'weights': 'no', 'eda': 'yes', 'prob_calib': 'no', 'mode': 'train'}

# LET'S CREATE THE MODEL BY SENDING THE PARAMETERS TO PREDICTNOW.AI
response = client.create_model(
 username=username, # only letters, numbers, or underscores
 model_name="test1",
 params=params,
)
