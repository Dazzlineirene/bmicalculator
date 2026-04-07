import streamlit as st
from PIL import Image
st.title("CHIOMA'S BMI CALCULATOR")

img = Image.open("C:\\Users\\eyehc\\Downloads\\905513-obesity-3217137.jpg")

st.image(img,width=500)
name = st.text_input("Enter your name")
weight = st.number_input("Weight (kg)")
status = st.radio("select height", ("cm", "m", "ft"))
if status == "cm":
    height = st.number_input("Height (cm)")
    try:
        bmi = weight / ((height/100) ** 2)
    except:
        st.error("Please enter a valid height in cm")
elif status == "m":
    height = st.number_input("Height (m)")
    try:
        bmi = weight / (height ** 2)
    except:
        st.error("Please enter a valid height in m")
else:
    height =st.number_input ("Height in (ft)")
    try:
        bmi = weight / ((height/3.28) ** 2)
    except:
        st.error("Please enter a valid height in ft")
if st.button("Calculate BMI"):
    st.text("Your BMI is {}".format(bmi))
    if (bmi < 16):
        st.error(f"{name}, you are extremely underweight")
    elif (bmi >= 16 and bmi < 18.5):
        st.warning(f"{name}, you are underweight")
    elif (bmi >= 18.5 and bmi < 25):
        st.success(f"{name}, you are healthy")
    elif (bmi >= 25 and bmi < 30):
        st.warning(f"{name}, you are overweight")
    else:
        st.error(f"{name}, you are extremely overweight")



