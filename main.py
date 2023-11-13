import numpy as np
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(
        api_key=os.environ['API_KEY'],  # this is also the default, it can be omitted
    )

response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  response_format={ "type": "json_object"},
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)
print(response.choices[0].message.content)

