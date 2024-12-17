import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from PIL import Image
import pickle

# importing model
fmodel = pickle.load(open('models/fert.sav', 'rb'))
fsc = pickle.load(open('models/fstandscaler.sav', 'rb'))
fmx = pickle.load(open('models/fminmaxscaler.sav', 'rb'))
model = pickle.load(open('models/rfc_model.sav', 'rb'))
sc = pickle.load(open('models/rfc_sc_model.sav', 'rb'))
mx = pickle.load(open('models/rfc_mx_model.sav', 'rb'))


def Crop_predict(N, P, K, temp, humidity, ph, rainfall):
    
    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    scaled_features = mx.transform(single_pred)
    final_features = sc.transform(scaled_features)
    prediction = model.predict(final_features)

    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = "{} is the best crop to be cultivated right there".format(crop)
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
    return result

def Fertilizer_predict(Temparature,Humidity ,Moisture,Soil_Type, Crop_Type,Nitrogen,Potassium,Phosphorous):
    
    feature_list_1= [Temparature, Humidity ,Moisture,Soil_Type, Crop_Type, Nitrogen, Potassium, Phosphorous]
    single_pred_1= np.array(feature_list_1).reshape(1, -1)
    st.write(single_pred_1)
    #scaled_features_1= fmx.transform(single_pred_1)
    #final_features_1 = fsc.transform(scaled_features_1)
    #prediction_1= fmodel.predict(final_features_1)
    prediction_1= fmodel.predict(single_pred_1)

    fert_dict = {
        1: 'Urea',
        2: 'DAP',
        3: '14-35-14',
        4: '28-28',
        5: '17-17-17',
        6: '20-20',
        7: '10-26-26'
    }

    # Check if prediction is in the fertilizer dictionary
    if prediction_1[0] in fert_dict:
        recommended_fert = fert_dict[prediction_1[0]]
        result= "{} is the recommended fertilizer to be used.".format(recommended_fert)
    else:
        result ="Sorry, we are not able to recommend a proper fertilizer for this environment."
    return result

def main():
    with st.sidebar:
        
        selected = option_menu('Crop Recommendation System', 
                              ['CROP Details',"Fertilizer Recommendation"],
                              icons=['Crop','Fertilizer'],   
                              default_index=0)
 
    if selected == 'CROP Details':
        st.subheader("Crop Details")
        st.write("\n")
       
       
        # getting the input data from the user
        col1, col2, col3,col4= st.columns(4)
       
        with col1:
            N = st.text_input('Nitrogen')
           
        with col2:
            P = st.text_input('Phosporous')
       
        with col3:
            K = st.text_input('Pottasium')       
        with col1:
            temp = st.text_input('Temperature')
                   
        with col2:
            humidity = st.text_input('Humidity')
        with col3:
            ph = st.text_input('Ph')
       
        with col1:
            rainfall = st.text_input('Rainfall')
               
        with col4:
            image = Image.open('templates/farming.jpg')
            st.image(image,width = 400)  
        if st.button('Crop Predict'):
            result = Crop_predict(N, P, K, temp, humidity, ph, rainfall)
            st.success(result)
            st.write("\n")

    if selected == 'Fertilizer Recommendation':
        st.subheader("Fertilizer Details")
        st.write("\n")
       
       
        # getting the input data from the user
        col1, col2, col3,col4= st.columns(4)
       
        with col1:
            Temprature = st.text_input('Temperature')
            
        with col2:
            Humidity = st.text_input('Humidity')
                  
        with col3:
            Moisture = st.text_input('Moisture')     
        
        with col1:
            Soil_Type = st.text_input('Soil Type')
                   
        with col2:
            Crop_Type = st.text_input('Crop Type')
       
        with col3:
            Nitrogen = st.text_input('Nitrogen')
       
        with col1:
            Pottassium = st.text_input('Pottasium')
                   
        with col2:
            Phosphorous = st.text_input('Phosporous')              
                
        
        with col4:
            image = Image.open('templates/farming.jpg')
            st.image(image,width = 400)  
        if st.button('Fertilizer Predict'):
            result = Fertilizer_predict(Temprature,Humidity ,Moisture,Soil_Type,Crop_Type,Nitrogen,Pottassium,Phosphorous)
            st.success(result)
            st.write("\n")      


   
       


if __name__ == "__main__":
    main()
 
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.markdown("<p style = 'color:grey;'>This is a prediction web app for informational purposes only.</p>",unsafe_allow_html=True)
st.write("\n")
st.write("\n")
st.markdown('<p style="font-size:12px; color:#808080;">©2024 Project by Hiren & Varadhrajan Team - All Rights Reserved</p>', unsafe_allow_html=True)
