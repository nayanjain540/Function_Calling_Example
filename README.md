# Function_Calling_Example
This is a simple Python script to depict the implementation of function calling of CHAT GPT

Install requirements
```
pip install openai
```

```
Generate your OPEN AI key from here: https://platform.openai.com/

Generate your weather API key from here: https://www.weatherapi.com/
```

# This script depicts two different use cases.
1. In the LinkedIn chat you are not allowed to share your email address, however, users do share their email address in this particular format which LinkedIn is not able to detect: nayan jain 540 @ gmail . com. Function calling can be leveraged to detect email addresses and then flag the user by calling an API. 
2. Depicting how it can be used in a weather forecasting tool where users can ask for weather forecasts about any city in a free-flowing format. ChatGPT will extract the city, call the necessary function and pass the City name as an argument. And return the answer in a Human Readable Format. 


Replace the below two variables in the script
```
openai.api_key = "YOUR-OPEN-AI-KEY"
weather_api_key = "Weather-API-KEY"
```

```
python function_calling.py
```