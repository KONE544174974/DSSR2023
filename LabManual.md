# Streamlit App Guide

This lab hands-on manual guides you to build a Streamlit App as shown in [this example](https://ecom-churn-prediction.streamlit.app/) using basic Python programming and the [Streamlit](https://streamlit.io/) library.

This guide will not cover the basics of Python programming and the use cases of each API in the Streamlit library. It will just show the steps to build the E-Commerce Prediction and Visualization Streamlit App.

This guide uses [GitHub Codespace](https://github.com/features/codespaces) as the code editor, which already has some libraries used in the development of this app pre-installed. If you are using your local environment, you will need to install all used libraries manually into your machine. 

> If you have uploaded all relevant files and set up your GitHub Codespace, you may skip Step 01 and proceed to Step 02.

## Step 01: Setting Up GitHub Codespace

After you have created a GitHub repository, click the `<> Code` button > 'Codespaces' > 'Add codespace on main', then a new tab should appear which loads your codespace.

After it has done loading, upload the following files into the Codespace:

* Pipeline file `pipeline.pkl`
* Original dataset in a folder `E-Commerce-Dataset`
    * Name the csv file `dataset.csv`
* Checkpoint datasets in a folder `Dataset-Checkpoints`
    * `cleaned_data.csv`
    * `balance_cleaned_data.csv`

Then, create a python file named `Visualization.py`. A pop up should appear informing you to install Python dependencies, install and wait.

## Step 02: Installing Other Libraries

After you have done installing the Python dependencies, you will need to install the following libraries by pasting the code below in the **Terminal**:

```sh
pip install streamlit xgboost
```

After the installation is complete, paste the following code in the Terminal again:

```sh
streamlit run Visualisation.py --server.enableCORS false --server.enableXsrfProtection false
```

After a short while, a pop up will occur, click "Open in Browser" and view your Streamlit app, which should be empty at the moment.

## Step 03: Writing in Streamlit

Now that we have the web app running at the same time, our changes in the `Visualization.py` file will be updated dynamically in the web app also. We will be using the Streamlit [text-related APIs](https://docs.streamlit.io/library/api-reference/text) for this part. Paste the following code in your python file.

```py
import streamlit

# Page title
st.title('Churn Dataset')
st.markdown('---')

# Page description
st.markdown('''This project is inspired by [Yeo Jie Hui](https://my.linkedin.com/in/yeo-jie-hui)\'s Data Science 
            [Final Year Project](https://drive.google.com/file/d/1dD_I4pSMqhEnLbed1jQ90sJU-SQt7cTE/view?usp=sharing) 
            on predicting customer churn based on their behaviours online. This project\'s GitHub repository can be found 
            in [this link](https://github.com/dscum/DSSR2023), where it contains the EDA notebooks, the checkpoint datasets, 
            pipeline model and etc.''')
st.markdown('''The original dataset source is from Kaggle\'s 
            [E Commerce Dataset](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction).''')
```

Go back to the web app, you should see a message at the top right of the screen informing that the source code has changed, so you can click "Always Rerun" to see the code changes update dynamically in the web app. Now, you should be able to see some texts in your web app.

## Step 04: Dataset Viewing

Our first component in the visualization part is **View Dataset**. We will need to use the `pandas` library for this section, hence you will need to paste the import code below at the top of your python file.

```py
import pandas as pd
```

Then, paste the code below after the text code in your python file.

```py
# Cache data
@st.cache_data
def get_data(path: str, **kwargs) -> pd.DataFrame:
    '''Load data into dataframe'''
    dataframe = pd.read_csv(path, **kwargs)
    return dataframe
```

> Streamlit has a crucial component call data caching annotated by `@st.cache_data` which allows a function to cache the data reading so that the data is stored in cache and can be accessible without the need to reread the data from the csv file everytime.

Then, paste the code below to display the first component.

```py
# View dataset
st.header('View Dataset')

tab1, tab2, tab3 = st.tabs(['Original Dataset', 'Cleaned Dataset', 'Scaled & Balanced Dataset'])

with tab1: 

    df = get_data('./E-Commerce-Dataset/dataset.csv')
    n_rows = st.slider('Number of rows to view', 1, len(df) - 1)
    st.dataframe(df.head(n_rows))

with tab2: 

    df = get_data('./Dataset-Checkpoints/cleaned_data.csv', index_col=0)
    n_rows = st.slider('Number of rows to view', 1, len(df) - 1)
    st.dataframe(df.head(n_rows))

with tab3: 

    df = get_data('./Dataset-Checkpoints/balance_cleaned_data.csv', index_col=0)
    n_rows = st.slider('Number of rows to view', 1, len(df) - 1)
    st.dataframe(df.head(n_rows))
```

Here we create 3 tabs each reading and displaying the respective datasets with varying number of rows based on user input using the `st.slider()` function.

## Step 05: Column Distribution

Our next component in the visualization part is the **View Data Distribution in a Column**. We will need to use the `matplotlib` library for this section, hence you will need to paste the import code again at the top of the python file.

```py
import matplotlib.pyplot as plt
```

Then, paste the code below to display the second component.

```py
# Visualize Distribution
st.header('Visualize Distribution')

tab1, tab2, tab3 = st.tabs(['Original Dataset', 'Cleaned Dataset', 'Scaled & Balanced Dataset'])
submit = None

with tab1:

    col1, col2 = st.columns(2)
    df = get_data('./E-Commerce-Dataset/dataset.csv')
    selected_column = None

    with col1.form('ori_dataset_viz'):
        selected_column = st.selectbox('Select a Column', df.columns)
        submit = st.form_submit_button('Visualize', use_container_width=True)

    if submit:
        fig, ax = plt.subplots()
        ax.hist(df[selected_column], ec='black', color='#f63366')
        ax.set_title(selected_column)
        col2.pyplot(fig)

with tab2:

    col1, col2 = st.columns(2)
    df = get_data('./Dataset-Checkpoints/cleaned_data.csv', index_col=0)
    selected_column = None

    with col1.form('clean_dataset_viz'):
        selected_column = st.selectbox('Select a Column', df.columns)
        submit = st.form_submit_button('Visualize', use_container_width=True)

    if submit:
        fig, ax = plt.subplots()
        ax.hist(df[selected_column], ec='black', color='#f63366')
        ax.set_title(selected_column)
        col2.pyplot(fig)

with tab3:

    col1, col2 = st.columns(2)
    df = get_data('./Dataset-Checkpoints/balance_cleaned_data.csv', index_col=0)
    selected_column = None

    with col1.form('scaled_dataset_viz'):
        selected_column = st.selectbox('Select a Column', df.columns)
        submit = st.form_submit_button('Visualize', use_container_width=True)

    if submit:
        fig, ax = plt.subplots()
        ax.hist(df[selected_column], ec='black', color='#f63366')
        ax.set_title(selected_column)
        col2.pyplot(fig)
```

Again we create 3 tabs for each dataset, then we use the streamlit's `column()` method to split our content into multiple columns. Then, we use the `form()` method to get user input first and then the `st.form_submit_button()` to invoke the block of statements inside the `if` condition, i.e. displaying the distribution as a histogram.

Here, we can see that the graph barely fits in its place, we can change the page config to set the default view size as `'wide'`. We can also set other configurations like page title, page icon etc. using the code below, which must be pasted right after the import statements before any other statements are executed:

```py
# Page config
st.set_page_config(
    page_title='Customer Churn',
    page_icon='🛒',
    layout='wide',
)
```

Now our app looks fine and nice.

## Step 06: Prediction Page

Now that we are done with our `Visualization.py`, we want to create our 2nd page in the Streamlit app. To do so, we can create a `pages` folder.

Then in the folder, create a python file named `1_🤖_Churn_Prediction.py`. The `1` at the front indicates the first page after the `Visualization.py` page, the `_` indicates a whitespace. 

> Note that the file name after `1_` will be the name displayed in the sidebar of the Streamlit app, the same goes to the `Visualization.py` where the page name is `Visualization`.

Here in the prediction page, we will also start with writing the page texts first. But again since we are at a different python file, we will need to import the necessary libraries again.

```py
import streamlit as st

# Page title
st.title('🤖 Churn Prediction')
st.markdown('---')
```

As you can see from the web application, your second page loads perfectly fine!

## Step 07: Preparing User Input Data Storage for Prediction

In this part, we will be collecting all relevant values for our ML model pipeline prediction. We will start with a dictionary that stores all values to be converted into a `pandas` dataframe, which columns follows the exact same columns for the pipeline input. Again we need to import the library and place it at the top of the file.

```py
import pandas as pd
```

Then, paste the code below after the text section.

```py
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
```

We will also declare and initialize various variables for them to have the global scope.

```py
# Predict button state -> boolean
predict = None
```

## Step 08: Input Widgets

We can start writing the input components code using the Streamlit [Input Widget APIs](https://docs.streamlit.io/library/api-reference/widgets).

```py
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
```

Here, we use a combination of different input widgets and other text APIs to let our 'form' looks nicer. Each of the values are inserted into its designated column with the array's `append()` method.

## Step 09: Prediction

After we have all of our data stored in the form of [Python Dictionary](https://www.w3schools.com/python/python_dictionaries.asp), we can convert it into a dataframe to be used as the pipeline model input with `pd.DataFrame(user_input)`.

But before that, we will need to load our pipeline model into our python file. And to do that, we will need to import the `joblib` library which we used to save our model in the notebook previously. Again, paste the import code at the top of the file.

```oy
import joblib
```

Then, we can load our pipeline model with the following code:

```py
# Preload and constants
pipeline = joblib.load('./pipeline.pkl')
```

Then, we can bring our dataframe into our model for prediction using the code below, which should be pasted after the big `with` block:

```py
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
```

Here we display our user input data as a dataframe at the left, then the result of the prediction at the right, where we utilize `st.success()` to display a box with green background and `st.error()` to display a box with red background.

Then, we are done, we can proceed with the app deployment on [Streamlit Community Cloud](https://streamlit.io/cloud).

## Step 10: App Deployment

To deploy the streamlit app on the community cloud, we will need to have a `requirements.txt` file in our repository, which stores all libraries and dependencies used in our project. We can generate this file by pasting this code in the **Terminal**:

```sh
pip freeze > requirements.txt
```

Then, commit and push everything to the GitHub repository under "Version Control" tab at the sidebar of your GitHub Codespace.

Next, head on to [Streamlit page](https://streamlit.io/) and "Sign In" > "Continue with GitHub". After you have done signing in, you should see a dashboard of your deployed app (which should be none if you are new to Streamlit). Click the "New App" button, then click "Paste GitHub URL", and paste the URL to your `Visualization.py` file in your GitHub repository, which should look like the sample URL given in the text field.

Then, you can optionally set an App URL, and finally click "Deploy!", and you just need to wait for the code to set up on the Streamlit Community Cloud and your app will be public. Share it to your friends to showcase this skill!

---

## Copyright

This project guide is created and owned by [LimJY03](https://github.com/LimJY03) and [Jiehui0827](https://github.com/Jiehui0827), licensed under [MIT License](https://github.com/dscum/DSSR2023/blob/main/LICENSE).