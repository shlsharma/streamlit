import joblib
import streamlit as st

model_name = 'RF_Loan_model.joblib'
model = joblib.load(model_name)

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

    if st.button('Submit')

if __name__ == '__main__':
    main()