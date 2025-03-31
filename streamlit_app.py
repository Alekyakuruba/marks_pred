import streamlit as st
import sklearn
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Students_marks_prediction")
st.markdown(
    "The dataset contains modifications with regards to the original for illustrative & learning purposes"
)

time_study = st.slider('How many hours does the student read?', 0, 10, 20)
#accommodates = st.slider('How many people does the listing accommodate?', 1, 16, 2)
#instant_bookable = st.radio(
    #"Is the listing instantly bookable?",
    #("True", "False"))
#instant_bookable = 1 if instant_bookable == "True" else 0

user_input = [[time_study]]#, accommodates, instant_bookable]]

if st.button('Predict?'):
    st.write("The model predicts that the average tip for this marks is:", model.predict(user_input).round(2))
