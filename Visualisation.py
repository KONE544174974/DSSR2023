import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title='Customer Churn',
    page_icon='🛒',
    layout='wide',
)

# Cache data
@st.cache_data
def get_data(path: str, **kwargs) -> pd.DataFrame:
    '''Load data into dataframe'''

    dataframe = pd.read_csv(path, **kwargs)

    return dataframe

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