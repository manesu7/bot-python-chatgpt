from openai import OpenAI

#pass the api key
client = OpenAI(
    api_key = 'my-api-key'
)

# define prompt
message = {'role': 'user', 'content': 'why is my website down?'}
messages = []
messages.append(message)

# make an api call
response = client.chat.completions.create(messages=messages, model="gpt-5.4")

# print the response
print(response)

# print the response
print(response.choices[0].message.content)