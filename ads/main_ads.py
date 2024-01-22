import pickle
import streamlit as st

with open("model.pickle", 'rb')as file:
    model = pickle.load(file)

tv = st.text_input("ads on TV")

if st.button("Predict"):
    y_pred = model.predict([[float(tv)]])
    print(y_pred[0])
    st.write(y_pred[0])


