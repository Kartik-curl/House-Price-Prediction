import numpy as np

import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_absolute_percentage_error,accuracy_score
def etl():
    
    #extract
    data= pd.read_csv("Dataset.csv")
    df = pd.DataFrame(data)

    #transform
    #print(df.head())
    #print(df.columns)
    #print(df.notnull().sum())
    #print(df["HOUSE_TYPE"].value_counts())
    #print(df["Owner_type"].value_counts())
    #print(df["Area_Type"].value_counts())
    #print(df["Location"].value_counts())
    df=df.drop(columns=["css-11nfaq3","Unnamed: 4","Unnamed: 6","Unnamed: 7","Location","Purpose","Owner_name","HOUSE_TYPE","Area_Type"],)
    df = df.dropna()
    #print(df.notna().sum())

    def to_number(data):
        value,unit = data.split()
        num_value=float(value[1:])
        
        if unit== "Cr":
            num = num_value*10000000
            return num
        elif unit == "L" or unit == "Lacs":
            num = num_value* 100000
            return num
        elif unit == "K":
            num = num_value*1000
            return num
        else:
            return num_value*1000

    def value_split(data):
        value,unit = data.split()
        return float(value)

    df["Flat_Price"]= df["Flat_Price"].apply(to_number)
    df["EMI_Starts"] = df["EMI_Starts"].apply(to_number)
    df["Price_per_sq.ft"]=df["Price_per_sq.ft"].apply(to_number)
    df["Total_Sq.ft"]=df["Total_Sq.ft"].apply(value_split)
    df["BHK"]= df["BHK"].apply(value_split)
    
    #print(df.head())
    #print(df["Owner_type"].value_counts())
    #load
    with open("exstracted.pkl","wb") as f:
        pickle.dump(df,f)
    #print(df.head())


    #visual representation
    #plt.scatter(df["EMI_Starts"],df["Flat_Price"])
    #plt.scatter(df["Price_per_sq.ft"],df["Flat_Price"])
    #plt.scatter(df["Owner_type"],df["Flat_Price"])

def train_model():
    etl()
    with open("extracted.pkl","rb") as file:
        df = pickle.load(file)
       
    y= df["Flat_Price"]
    X = df.drop(columns=["Flat_Price"])
    lbc=LabelEncoder()
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    X_train["Owner_type"] = lbc.fit_transform(X_train["Owner_type"])
    X_test["Owner_type"] = lbc.transform(X_test["Owner_type"])
    with open("labelenc.pkl","wb") as file:
        pickle.dump(lbc,file)
    model = LinearRegression()
    model.fit(X_train,y_train)
    with open("model.pkl","wb") as file:
        pickle.dump(model,file)
    print("Model Trained Successfully")

def predict(input):
  
    with open("labelenc.pkl","rb") as f:
        lbc= pickle.load(f)
    input[0][4]=lbc.transform([input[0][4]])[0]               # 0 because transform returns array[2]
    with open("model.pkl","rb") as file:
        model = pickle.load(file)
        output = np.round(model.predict(input)[0],2)            # same here 0 to return only answer without squere braces
        return output

