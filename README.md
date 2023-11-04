# Function_Calling_Example
This is simple Python script to depict the implementation of function calling of CHAT GPT

# pip install openai

# Generate your OPEN AI key from here: https://platform.openai.com/

# Generate your weather API key from here: https://www.weatherapi.com/

# This script is depicting two different use cases.

# 1. In LinkedIN chat you are not allowed to share your email address, however it can be shared in this format: nayan jain 540 @ gmail . com. Function calling can be leveraged to detect email address, flag the user by calling an API. 

# 2. Depicting how it can be used in a weather forecasting Chatbot where user can ask weather forecast about any city in a free flowing format. ChatGPT will extract the city, call the necessary function and pass the City name as argument. And return the answer in an Human Readable Format. 

# Replace the below two variables in the script
# openai.api_key = "YOUR-OPEN-AI-KEY"
# weather_api_key = "Weather-API-KEY"
# And then python function_calling.py