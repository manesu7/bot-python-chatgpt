import openai
from openai import OpenAI
import wikipedia

# pass the api key
client = OpenAI(
    api_key = 'My_Secret_KEY'
)

# define prompt
prompt =  'Create a 5-bullet point summary of: '
messages = []
messages.append({'role': 'user', 'content': prompt})

try:
    # make an api call
    response = client.chat.completions.create(messages=messages, model="gpt-5.4")

    # print the response
    print(response.choices[0].message.content)

# authentication issue
except openai.AuthenticationError:
    print('no valid token / authentication error')

except openai.BadRequestError as e:
    print('invalid request, read the manual!')
    print(e)
    

