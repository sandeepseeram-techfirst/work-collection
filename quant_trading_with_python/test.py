input_features= df['Date'].values
for i in range(len(input_features)):
    #/ split y_pred[‘Date'] into actual date and parameters string
    date_params =input_features[i].split(' ') 
    params = date_params[1]
