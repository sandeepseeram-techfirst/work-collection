input_features= df['Date'].values
for i in range(len(input_features)):
    #/ split y_pred[‘Date'] into actual date and parameters string
    date_params =input_features[i].split(' ') 
    params = date_params[1]
   if i==0: 
 #initializing max_index and its parameters value 
    #E.g. (2.5, 60, 0.2)
    params_cond_optimized = params 
      y_pred_max = y_pred[i].values
    else:
        if y_pred[i].values>= y_pred_max:
        #updating max_index and its parameters value 
        params_cond_optimized = params 
          y_pred_max = y_pred[i].values
 # params_cond_optimized is “conditionally optimal” parameters for the
 # next day 
 