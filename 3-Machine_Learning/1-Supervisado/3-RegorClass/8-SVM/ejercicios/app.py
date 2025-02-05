import streamlit as st
import pickle

st.title("Mi modelo")

x1 = st.slider("Introduzca variable x1", 0, 130, 30)

x2 = st.slider("Introduzca variable x2", 0, 130, 30)

with open("finished_model.pkl", 'rb') as archivo_entrada:
    modelo = pickle.load(archivo_entrada)

if st.button("Predecir"):
    st.write(modelo.predict([[x1,x2]]))


st.feedback('stars')
st.metric("My metric", 42, 2)