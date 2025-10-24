import streamlit as st

# --- Page Configuration ---
# Sets the title of the browser tab and a layout
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

# --- Main App ---

# 1. Title and Description
st.title("Interactive BMI Calculator ⚖️")
st.markdown("Calculate your Body Mass Index (BMI) easily. BMI is a measure of body fat based on height and weight.")

# 2. Input Fields
st.header("Enter Your Details")

# Use columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    # Input for weight (in kilograms)
    weight = st.number_input(
        "Enter your weight (in kg)", 
        min_value=10.0, 
        value=70.0, 
        step=0.5
    )

with col2:
    # Input for height (in centimeters)
    height_cm = st.number_input(
        "Enter your height (in cm)", 
        min_value=50.0, 
        value=170.0, 
        step=1.0
    )

# 3. Calculation Button and Logic
if st.button("Calculate BMI"):
    if height_cm > 0 and weight > 0:
        # Convert height from cm to meters
        height_m = height_cm / 100
        
        # Calculate BMI: weight / (height * height)
        bmi = weight / (height_m ** 2)
        
        # 4. Display the Result
        st.header("Your Result")
        
        # st.metric displays a number in a big, bold way
        st.metric(label="Your BMI is", value=f"{bmi:.2f}")
        
        # 5. Display the BMI Category
        if bmi < 18.5:
            st.warning("You are **Underweight**.")
            st.image("https://media.giphy.com/media/l41lISmpe8hOHPimY/giphy.gif")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a **Normal weight**. Great job!")
            st.image("https://media.giphy.com/media/3o7TKrEzvL3vt1I2li/giphy.gif")
        elif 25 <= bmi < 29.9:
            st.warning("You are **Overweight**.")
            st.image("https://media.giphy.com/media/l0K41MJ0tQeFv9t0A/giphy.gif")
        else:
            st.error("You are in the **Obesity** category.")
            st.image("https://media.giphy.com/media/G8kOQJHNlwmxf528Gf/giphy.gif")
            
    else:
        # Error message if inputs are invalid
        st.error("Please enter valid weight and height.")

# --- Sidebar Information ---
st.sidebar.header("What is BMI?")
st.sidebar.info(
    "BMI is a value derived from the mass (weight) and height of a person. "
    "It's a convenient rule of thumb used to broadly categorize a person as "
    "underweight, normal weight, overweight, or obese."
)
st.sidebar.header("BMI Categories")
st.sidebar.markdown(
    """
    - **Underweight**: Below 18.5
    - **Normal**: 18.5–24.9
    - **Overweight**: 25.0–29.9
    - **Obesity**: 30.0 and above
    """
)