# Streamlit to build the apps
# run this app: python -m streamlit run ecomm.py
# Deploy in streamlit first upload file in git then create app from streamlit
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def main():
    st.title("This is my streamlit app")
    st.sidebar.title("upload the sidebar menu")

    uploaded_file = st.sidebar.file_uploader("upload yourfile", type=["csv", "xlsx"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file)

            st.sidebar.success("file uploaded successfully!")
            st.subheader("data overview")
            st.dataframe(data.head())

            st.subheader("Basic info of data")
            st.write("shape of data", data.shape)
            st.write("columns in my data", data.columns)
            st.write("missing value", data.isnull().sum())

            st.subheader("Show stat of data")
            st.write(data.describe())

        except:
            print("Fail")


if __name__ == "__main__":
    main()
