from openai import OpenAI
import os

# pass the api key
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)

# define prompt
messages = []
messages.append({'role': 'user', 'content': 'what color is the sky?'})

# make an api call
response = client.chat.completions.create(messages=messages, model="gpt-5.4", max_completion_tokens=500)

# print the response
print(response.choices[0].message.content)