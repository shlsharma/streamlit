import joblib
import streamlit as st
import numpy as np

model_name = 'RF_Loan_model.joblib'
file_url = "https://raw.githubusercontent.com/manifoldailearning/Complete-MLOps-BootCamp/main/Build-ML-App-Streamlit/RF_Loan_model.joblib"
wget.download(file_url)
model = joblib.load(model_name)

def prediction(Gender, Married, Dependents, Education, SelfEmployed,
                ApplicantIncome, CoapplicantIncome, LoanAmount, LoanAmountTerm, CreditHistory,
                PropertyArea):
    if Gender == "Male":
        Gender = 1
    else:
        Gender = 0

    if Married == "Yes":
        Married = 1
    else:
        Married = 0

    if Education == "Graduate":
        Education = 0
    else:
        Education = 1

    if SelfEmployed == "Yes":
        SelfEmployed = 1
    else:
        SelfEmployed = 0

    TotalIncome = np.log(ApplicantIncome+CoapplicantIncome)

    if CreditHistory == "Outstanding Loan":
        CreditHistory = 1
    else:
        CreditHistory = 0

    if PropertyArea == "Rural":
        PropertyArea = 0
    elif PropertyArea == "Semi Urban":
        PropertyArea = 1
    else:
        PropertyArea = 2

    predict = model.predict([[Gender, Married, Dependents, Education, SelfEmployed, LoanAmount, 
                             LoanAmountTerm, CreditHistory, PropertyArea, TotalIncome]])
    print(print(predict))

    if predict == 0:
        pred = "Rejected"
    else:
        pred = "Approved"
    
    return pred

def main():
    # front end
    st.title('Welcome to Loan Application')
    st.header('Please enter your details to proceed with your loan applicaiton')

    Gender = st.selectbox('Gender', ('Male', 'Female'))
    Married = st.selectbox('Married', ('Yes', 'No'))
    Dependents = st.number_input('Number of Dependents')
    Education = st.selectbox('Education', ('Graduate', 'Not Graduate'))
    SelfEmployed = st.selectbox('Self Employed', ('Yes', 'No'))
    ApplicantIncome = st.number_input('Enter the applicant income')
    CoapplicantIncome = st.number_input('Enter the coapplicant income')
    LoanAmount = st.number_input('Enter the loan amount')
    LoanAmountTerm = st.number_input('Enter the loan amount term')
    CreditHistory = st.selectbox('Credit History', ('Outstanding Loan', 'No Outstanding Loan'))
    PropertyArea = st.selectbox('Property Area', ('Rural', 'Urban', 'Semi Urban'))

    if st.button('Predict'):
        result = prediction(Gender, Married, Dependents, Education, SelfEmployed,
                            ApplicantIncome, CoapplicantIncome, LoanAmount, LoanAmountTerm, CreditHistory,
                            PropertyArea)
        
        if result == "Approved":
            st.success("Your Loan Application is Approved")
        else:
            st.error("Your Loan Application is Rejected")

if __name__ == '__main__':
    main()