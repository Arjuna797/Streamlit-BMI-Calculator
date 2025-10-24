# 1. Start from an official Python base image
# Using "slim" makes your final image smaller
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file *first*
# This is a best-practice for Docker caching
COPY requirements.txt .

# 4. Install the Python dependencies
# --no-cache-dir keeps the image lean
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all your application code into the container
COPY . .

# 6. Expose the port Streamlit runs on (this is documentation)
EXPOSE 8501

# 7. Define the command to run when the container starts
# This will launch your Streamlit app
CMD ["streamlit", "run", "bmi_app.py"]