import streamlit as st

st.write("""
# Test Score Prediction App
This app predicts your test score based on number of hours you have studied in a week
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
   
    num = st.number_input("Hour's studied in a week",min_value= 0.0,max_value= 168.0)
   
    
    return num

x = user_input_features()
b = 0.02963934787473239
m = 1.4774173755483797
y = m*x + b
st.subheader('The test score you can expect considering the hours you studied:')
if x:
   st.write(y)
else:
   st.write(0.0)
