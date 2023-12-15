# DSSR2023

Here are some links related to the event itself.

* [Workshop Link](https://gdsc.community.dev/events/details/developer-student-clubs-university-of-malaya-presents-data-science-speed-run-dssr/)
* [Workshop Handbook]()

Here are some important links related to this repository.

* [Colab Notebook](./E_Commerce_Customer_Churn.ipynb)
* [Kaggle Dataset](./E-Commerce-Dataset)
* [Streamlit App]()

---

## Running Streamlit from GitHub Codespace

Running streamlit from a virtual environment is shown in the [streamlit docs](https://docs.streamlit.io/library/get-started/create-an-app), however doing the command lines will cause a [forever loading error](https://stackoverflow.com/questions/70177733/the-streamlit-app-stops-with-please-wait-and-then-stops/70184078) on the streamlit preview app.

To properly run streamlit preview from GitHub codespace, we add some additional flags to the command.

```
--server.enableCORS false --server.enableXsrfProtection false
```

For example, to test if streamlit is properly installed, we will run the following:

```sh
streamlit hello --server.enableCORS false --server.enableXsrfProtection false
```

Or if we want to run our `app.py`, we can write the following in the terminal:

```sh
streamlit run app.py --server.enableCORS false --server.enableXsrfProtection false
```