import streamlit as st
import pandas as pd
import joblib

# Page title
st.title('🤖 Churn Prediction')
st.markdown('---')

# Preload and constants
pipeline = joblib.load('./pipeline.pkl')

user_input = {
    'Tenure': [], 
    'CityTier': [], 
    'WarehouseToHome': [], 
    'HourSpendOnApp': [], 
    'NumberOfDeviceRegistered': [], 
    'SatisfactionScore': [], 
    'NumberOfAddress': [], 
    'Complain': [], 
    'OrderAmountHikeFromlastYear': [], 
    'CouponUsed': [], 
    'OrderCount': [], 
    'DaySinceLastOrder': [], 
    'CashbackAmount': [], 
    'PreferredLoginDevice_Mobile Phone': [], 
    'PreferredPaymentMode_Credit Card': [], 
    'PreferredPaymentMode_Debit Card': [], 
    'PreferredPaymentMode_E wallet': [], 
    'PreferredPaymentMode_UPI': [], 
    'Gender_Male': [], 
    'PreferedOrderCat_Grocery': [], 
    'PreferedOrderCat_Laptop & Accessory': [], 
    'PreferedOrderCat_Mobile Phone': [], 
    'MaritalStatus_Married': [], 
    'MaritalStatus_Single': [],
}

predict = None

with st.form(key='prediction'):

    st.markdown('### User Demographics')
    
    # Row 1
    col1, col2, col3 = st.columns(3)

    user_input['Gender_Male'].append(int(col1.selectbox('Gender', ['Male', 'Female']) == 'Male'))
    marital = col2.selectbox('Marital Status', ['Divorced', 'Married', 'Single'])
    user_input['MaritalStatus_Married'].append(int(marital == 'Married'))
    user_input['MaritalStatus_Single'].append(int(marital == 'Single'))
    user_input['CityTier'].append(col3.selectbox('City Tier', [1, 2, 3]))

    # Row 2
    col1, col2 = st.columns([1, 2])

    user_input['Tenure'].append(col1.slider('Tenure', max_value=50))
    user_input['WarehouseToHome'].append(col2.slider('Warehouse to Home (miles)', max_value=150))

    st.write('---')


    st.markdown('### User Preference')

    col1, col2, col3 = st.columns(3)
    
    user_input['PreferredLoginDevice_Mobile Phone'].append(int(col1.selectbox('Preferred Login Device', ['Mobile Phone', 'Computer']) == 'Mobile Phone'))

    payment_mode = col2.selectbox('Preferred Payment Mode', ['Cash on Delivery', 'Credit Card', 'Debit Card', 'E Wallet', 'UPI'])
    user_input['PreferredPaymentMode_Credit Card'].append(int(payment_mode == 'Credit Card'))
    user_input['PreferredPaymentMode_Debit Card'].append(int(payment_mode == 'Debit Card'))
    user_input['PreferredPaymentMode_E wallet'].append(int(payment_mode == 'E Wallet'))
    user_input['PreferredPaymentMode_UPI'].append(int(payment_mode == 'UPI') )

    order_cat = col3.selectbox('Preferred Order Category', ['Fashion', 'Grocery', 'Laptop & Accessory', 'Mobile Phone'])
    user_input['PreferedOrderCat_Grocery'].append(int(order_cat == 'Grocery'))
    user_input['PreferedOrderCat_Laptop & Accessory'].append(int(order_cat == 'Laptop & Accessory'))
    user_input['PreferedOrderCat_Mobile Phone'].append(int(order_cat == 'Mobile Phone'))

    st.write('---')


    st.markdown('### User Behaviour')

    col1, col2, col3 = st.columns(3)
    user_input['HourSpendOnApp'].append(col1.slider('Hours Spent On App', max_value=50))
    user_input['NumberOfDeviceRegistered'].append(col2.slider('Number Of Device Registered', min_value=1, max_value=15))
    user_input['NumberOfAddress'].append(col3.slider('Number Of Address', min_value=1, max_value=10))
    user_input['CouponUsed'].append(col1.slider('Number of Coupon Used', max_value=10))
    user_input['OrderCount'].append(col2.slider('Order Count', max_value=10))
    user_input['DaySinceLastOrder'].append(col3.slider('Day Since Last Order', max_value=10))
    col1, col2 = st.columns([1, 2])
    user_input['CashbackAmount'].append(col1.number_input('Cashback Amount', min_value = 0.00, step=0.01, max_value=400.00)   )
    user_input['OrderAmountHikeFromlastYear'].append(col2.number_input('Order Amount Hike From Last Year', min_value=10.0, step=0.1, max_value=100.0))

    st.write('---')


    st.markdown('### User Satisfaction')

    user_input['SatisfactionScore'].append(st.radio('Satisfaction Score', [1, 2, 3, 4, 5], horizontal=True))
    user_input['Complain'].append(int(st.checkbox('User Complain')))

    predict = st.form_submit_button('Predict', use_container_width=True)

if predict:

    col1, col2 = st.columns([1, 3])

    with col1:

        st.markdown('### User Data')        
        st.dataframe(pd.DataFrame(user_input).T, use_container_width=True)

    with col2:

        st.markdown('### Prediction Result')
        prediction = pipeline.predict(pd.DataFrame(user_input))

        if prediction[0]:

            st.success('''😃  
                    The Customer is Likely to Churn
                    ''')
            
        else:

            st.error('''☹  
                    The Customer is Unlikely to Churn
                    ''')