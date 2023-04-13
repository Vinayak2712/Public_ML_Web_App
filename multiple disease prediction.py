# importing the necessary libraries

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the models 

diabetes_model = pickle.load(open("D:/work/models/trained_model.sav", 'rb'))

heart_disease_model = pickle.load(open("D:/work/models/heart_disease_model.sav", 'rb'))

parkinsons_model = pickle.load(open("D:/work/models/parkinsons_model.sav", 'rb'))

#creating sidebar option 

with st.sidebar:
    
    selected = option_menu(          
                           "Multiple  Disease Predition System",
                           ['Diabetes Prediction',
                            'Heart disease Prediction',
                            'Parkinsosns Prediction'],
                           icons = ['activity','heart', 'person'],
                           default_index= 0)


# creating page for each option that should appear after selecting the option

if (selected == 'Diabetes Prediction'):
    
    # page title should be
    
    st.title("Diabetes Prediction using ML")
    
    # creating the columns for input according the dataset that is trained
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of 	Pregnancies ")
        
    with col2:
        Glucose = st.text_input("Glucose level")
        
    
    with col3:
        BloodPressure = st.text_input("value of BloodPressure ")
        
    with col1:
        SkinThickness = st.text_input(" SkinThickness  Value")
        
    
    with col2:
        Insulin = st.text_input(" Insulin level ")
        
    with col3:
        BMI = st.text_input("BMI value ")
        
    with col1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction value")
        
    with col2:
        Age = st.text_input("Age of the person")
        
    #creating prediction code
    
    diab_diagnosis = " "
    
    #creating the button for the prediction 
    
    if st.button('Diabtese Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,	BloodPressure,	SkinThickness,	Insulin,BMI, DiabetesPedigreeFunction,Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = "The person is Diabetic"
            
        if (diab_prediction[0] == 0):
            diab_diagnosis = "The Person is not Diabetic"            
            
    st.success(diab_diagnosis)
            

if (selected == 'Heart disease Prediction'):
    st.title('Heart Disease Prediction Using ML')
    
    #creating columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Enter your Age ")
        
    with col2:
        sex = st.text_input(" Enter your Sex (1 = male; 0 = female)")
    
    with col3:
        cp = st.text_input(" Enter Chest Pain Type (0,1,2,3,4)")
        
    with col1:
        trtbps = st.text_input(" resting blood pressure")
        
    with col2:
        chol = st.text_input("serum cholestoral in mg/dl")
        
    with col3:
        fbs = st.text_input("fasting blood sugar > 120 mg/dl")
        
    with col1:
        restecg = st.text_input("resting electrocardiographic results (values 0,1,2)")
    
    with col2:
        thalachh = st.text_input("maximum heart rate achieved")
    
    with col3:
        exng = st.text_input("exercise induced angina")
    
    with col1:
        oldpeak = st.text_input("ST depression induced by exercise relative to rest")
    
    with col2:
        slp = st.text_input("the slope of the peak exercise ST segment")
    
    with col3:
        caa = st.text_input("number of major vessels (0-3) colored by flourosopy")
    
    with col1:
        thall = st.text_input("Enter Value (thal: 0 = normal; 1 = fixed defect; 2 = reversable defect)")
        
    #creating the prediction code
    
    heart_diagnosis = ' '
    
    if st.button('Heart Disease Test'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp,	trtbps,	chol,	fbs, restecg, thalachh,	exng, oldpeak, slp,	caa, thall]])
        
        if (st.button[0] == 1):
            heart_diagnosis = "The person has Heart Disease"
        if (st.button[0]==0):
            heart_diagnosis = " The person does not have Heart Disease"
    st.success(heart_diagnosis)
    
    
    
    
    
    
if(selected == 'Parkinsosns Prediction'):
    st.title('Parkinsons Prediction using ML')
    
    # creating the columns for the output we have
    col1, col2, col3 , col4, col5 = st.columns(5)
    
    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
        
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
        
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
    
    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")
        
    with col5:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
        
    with col1:
        RAP = st.text_input("MDVP:RAP")
    with col2:
        PPQ = st.text_input("MDVP:PPQ")
    with col3:
        DDP = st.text_input("MDVP:DDP")
    with col4:
        Shimmer = st.text_input("MDVP : shimmer")
    with col5:
        Shimmer_dB = st.text_input("MDVP: shimmer_dB")
    
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    #creating the prediction code we have
    
    parkin_diagnosis = ""
    
    if st.button('Parkinsons Test Result'):
        parkin_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if (parkin_diagnosis[0]==1):
            parkin_diagnosis = "The person has Parkinson's disease"
        else:
            parkin_diagnosis = "The person does not have Parkinson's disease"
            
    st.success(parkin_diagnosis)
    
    
    
    
    


