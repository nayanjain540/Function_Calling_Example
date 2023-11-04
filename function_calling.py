import openai
import json
import requests
openai.api_key = "YOUR-OPEN-AI-KEY"
weather_api_key = "Weather-API-KEY"

# Weather API KEY
# https://www.weatherapi.com/

def get_weather_forecast(city: str):
    # call any API to push mobile number
    url = f"""http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}&aqi=yes"""

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    weather_json = response.text

    return {
            "weather":weather_json
        }

def find_email_address(email_address: str):
    # call any API to push email address
    email_address = email_address.replace(" ","")
    return {
            "email_address":email_address
        }


functions = [
    {
        "name": "get_weather_forecast",
        "description": "Use this function to get weather forecast of any city. The output will be in JSON format.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Any city in this world",
                }
            },
            "required": ["city"],
        },
    },
    {
        "name": "find_email_address",
        "description": "Use this function to find an email address in any format. The output will be in JSON format.",
        "parameters": {
            "type": "object",
            "properties": {
                "email_address": {
                    "type": "string",
                    "description": "Any email address written in a particular format.",
                }
            },
            "required": ["email_address"],
        },
    }
]


def ask_question(question: str):
    # First API call
    messages = [{"role": "user", "content": question}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        functions=functions,
        function_call="auto",
    )
    response_message = response["choices"][0]["message"]
    # Figure out which function to call
    if response_message.get("function_call"):
        available_functions = {
            "find_email_address": find_email_address,
            "get_weather_forecast": get_weather_forecast
        }
        function_name = response_message["function_call"]["name"]
        print(function_name)
        function_to_call = available_functions[function_name]

        function_args = json.loads(response_message["function_call"]["arguments"])
        # Call the user defined function

        if function_name == "get_weather_forecast":
            function_response = function_to_call(
                city=function_args.get('city')
            )
        else:
            function_response = function_to_call(
                email_address=function_args.get('email_address')
            )

        function_response = str(function_response)
        print(function_response)
        messages.append(response_message)
        print(response_message)
        # Add the data from the function so chatGPT has that in its history
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )
        # Second API call to answer the users question based on the data retrieved from the custom function
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=messages,
        )
        answer = second_response['choices'][0]['message']['content']
        return answer

print(ask_question("Is there any email address in this sentence in a coded format. nayan jain 540 @ gmail . com"))
print(ask_question("What is the weather forecast of London."))
print(ask_question("I am living in Mumbai, why is it so hot today"))