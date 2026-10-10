import openai
from openai import OpenAI
import wikipedia

# pass the api key
client = OpenAI(
    api_key = 'MY_SECRET_KEY'
)

# get user input
title = input('title of the page: ')

# get the wikipedia content
page = wikipedia.page(title=title, auto_suggest=False)

# define prompt
prompt = 'Write a summary of the following article: ' + page.content[:10000]


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
