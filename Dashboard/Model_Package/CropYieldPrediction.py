import joblib
import pandas as pd
import numpy as np
def RFModel(data):	
    df = pd.DataFrame(data,index = [0])
    df_coded = pd.get_dummies(df)
    model_columns = joblib.load('/root/Keyur Khant/Project/AgriProject/Dashboard/Model FIle/FinalModel_columns.pkl')
    df_coded1 = df_coded.reindex(columns=model_columns, fill_value=0)
    X = df_coded1.values
    mean = [2.00518381e+03, 2.64384429e+01, 3.52928187e+01, 3.50587999e+01,
	       5.21416735e+02, 2.34488658e+01, 4.45252100e+02, 2.18564159e+01,
	       1.72535958e+01, 4.30264891e-02, 4.08312601e-02, 2.98551149e-02,
	       4.59534611e-02, 4.69779014e-02, 4.30264891e-02, 2.64890970e-02,
	       2.75135372e-02, 3.92214254e-02, 4.36118835e-02, 4.37582321e-02,
	       5.32708913e-02, 3.77579394e-02, 4.90267818e-02, 2.37084736e-02,
	       2.59037026e-02, 5.79540465e-02, 2.37084736e-02, 1.94643641e-02,
	       3.96604712e-02, 4.77096444e-02, 5.01975706e-02, 3.93677740e-02,
	       1.44885116e-02, 5.37099371e-02, 3.38065271e-02, 5.02561101e-01,
	       1.93180155e-01, 1.05224645e-01, 1.99034099e-01, 4.08312601e-02,
	       7.34669984e-02, 2.00497585e-02, 3.98068198e-02, 3.71725450e-02,
	       3.45382702e-02, 2.64890970e-02, 4.25874433e-02, 7.63939704e-02,
	       1.94643641e-02, 5.66369091e-02, 3.68798478e-02, 5.09293136e-02,
	       2.85379775e-02, 2.48792624e-03, 3.43919216e-02, 1.85862725e-02,
	       2.80989317e-02, 3.32211327e-02, 2.06351529e-02, 4.53680667e-03,
	       7.17108152e-03, 3.54163618e-02, 4.14166545e-02, 4.09776087e-02,
	       1.08297966e-02, 2.92697205e-03, 2.69281428e-02, 1.65373921e-02,
	       4.28801405e-02, 4.37582321e-02, 5.41489829e-03]
    var = [2.10064583e+01, 1.10924927e+01, 2.77719294e+02, 1.73446500e+01,
	       1.86746463e+05, 2.30840652e+02, 1.53951260e+05, 2.56208554e+02,
	       1.96800848e+01, 4.11752103e-02, 3.91640683e-02, 2.89637870e-02,
	       4.38417406e-02, 4.47709781e-02, 4.11752103e-02, 2.57874248e-02,
	       2.67565425e-02, 3.76831052e-02, 4.17098871e-02, 4.18434492e-02,
	       5.04331034e-02, 3.63322774e-02, 4.66231565e-02, 2.31463819e-02,
	       2.52327008e-02, 5.45953750e-02, 2.31463819e-02, 1.90855026e-02,
	       3.80875183e-02, 4.54334342e-02, 4.76777745e-02, 3.78179524e-02,
	       1.42785947e-02, 5.08251797e-02, 3.26636459e-02, 2.49993441e-01,
	       1.55861583e-01, 9.41524192e-02, 1.59419527e-01, 3.91640683e-02,
	       6.80695985e-02, 1.96477657e-02, 3.82222369e-02, 3.57907469e-02,
	       3.33453781e-02, 2.57874248e-02, 4.07737530e-02, 7.05579317e-02,
	       1.90855026e-02, 5.34291696e-02, 3.55197246e-02, 4.83355186e-02,
	       2.77235613e-02, 2.48173646e-03, 3.32091173e-02, 1.82408230e-02,
	       2.73093817e-02, 3.21174891e-02, 2.02093434e-02, 4.51622406e-03,
	       7.11965711e-03, 3.41620431e-02, 3.97013152e-02, 3.92984443e-02,
	       1.07125121e-02, 2.91840488e-03, 2.62030180e-02, 1.62639067e-02,
	       4.10414340e-02, 4.18434492e-02, 5.38557716e-03]

    for i in range(len(X[0])):
    	X[0][i] = (X[0][i] - mean[i]) / (np.sqrt(var[i]))
	    
    model = joblib.load('/root/Keyur Khant/Project/AgriProject/Dashboard/Model FIle/FinalRFModel.pkl')  
    y_pred = model.predict(X)

    return y_pred[0].round(3)

