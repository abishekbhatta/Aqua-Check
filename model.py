import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

#creating panda dataframe from a water_pollution.csv file 

df = pd.read_csv("water_pollution.csv")

water_pollution = df.copy()

#preprocessing data for optimal accuracy

for col in ['ph', 'Hardness','Solids', 'Chloramines','Sulfate','Conductivity','Organic_carbon','Trihalomethanes','Turbidity']:
    
    # z-score normalization of each values of the dataframe

    mean = water_pollution[col].mean()
    std = water_pollution[col].std()

    water_pollution[col] = (water_pollution[col] - mean) / std

    # outlier removal using Inter-Quartile Range and z-score method
    
    water_pollution = water_pollution[(water_pollution[col] <= mean + (3 * std))]
    q75,q25 = np.percentile(water_pollution.loc[:,col],[75,25])
    intr_qr = q75-q25
 
    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)
 
    water_pollution.loc[water_pollution[col] < min, col] = np.nan
    water_pollution.loc[water_pollution[col] > max, col] = np.nan 

#replacing missing values with mean value of each column in the dataframes

water_pollution.fillna(water_pollution.mean(numeric_only=True).round(1), inplace=True)

#over-sampling the dataset using Synthetic Minority Oversampling Technique (SMOTE) to create equal number of observations 

oversample = SMOTE()

X = water_pollution.drop(columns="Polluted")                                                           
y = water_pollution["Polluted"]     

# X --> features of dataset
# y --> target variable

X, y = oversample.fit_resample(X, y)

#creating random forest classifier model and fitting training data to the model

RFC = RandomForestClassifier()
RFC.fit(X, y)