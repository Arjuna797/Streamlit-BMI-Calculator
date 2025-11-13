# ⚖️ Interactive BMI Calculator
Ex - 192.168.1.102 abc.local
A simple web application built with Streamlit to calculate your Body Mass Index (BMI) easily.


A simple web application built with Streamlit to calculate your Body Mass Index (BMI) easily.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

*(Note: Replace the URL above with your app's URL after you deploy it!)*

## 🚀 Features

* **Easy Input:** Enter your weight (in kg) and height (in cm).
* **Instant Calculation:** Click a button to see your BMI.
* **Clear Results:** Displays the BMI score and the corresponding category (Underweight, Normal, Overweight, or Obesity) with a color-coded message.
* **Helpful Info:** A sidebar explains what BMI is and lists the standard categories.

*(Tip: Take a screenshot of your running app and add it here.)*

## 🏃 How to Run Locally

### On Windows

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the app:**
    ```bash
    streamlit run bmi_app.py
    ```

### On Ubuntu (Virtual Machine Migration)

#### Dependency Installation on Ubuntu

1.  **Ensure Python and pip are installed:**
    - Python 3.7+ is required. Check if installed:
      ```bash
      python3 --version
      ```
    - If not installed, install Python 3 and pip:
      ```bash
      sudo apt update
      sudo apt install python3 python3-pip python3-venv
      ```

2.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

3.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    - This installs Streamlit, the only required dependency for this project.

#### Project Execution on Ubuntu

1.  **Activate the virtual environment (if not already active):**
    ```bash
    source venv/bin/activate
    ```

2.  **Run the app:**
    ```bash
    streamlit run bmi_app.py
    ```

3.  **Access the app:**
    - Open a web browser and navigate to the URL provided in the terminal (usually `http://localhost:8501`).

## ☁️ Deployment

This app is deployed on **Streamlit Community Cloud**.
