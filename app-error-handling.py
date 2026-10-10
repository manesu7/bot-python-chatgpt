import openai
from openai import OpenAI

client = OpenAI(
    api_key = 'MY_KEY_HERE'
)

# define prompt
messages = []
messages.append({'role': 'system', 'content': 'you are a mentoring software developers, don't only provide answers also ask guiding questions'})
messages.append({'role': 'user', 'content': 'why is my website down?'})

try:
    # make an api call
    response = client.chat.completions.create(messages=messages, model="gpt-5.4", max_completion_tokens=500)

    # print the response
    print(response.choices[0].message.content)

# authentication issues
except openai.AuthenticationError:
    print('no valid token / authentication error')

except openai.BadRequestError:
    print('invalid request, read the manual!')