# Elizabeth Wong github.com/e-lizabethwong
# Hack49 Prompt Engineering Workshop
import apikey
from openai import OpenAI


client = OpenAI(
    api_key=apikey.key
)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Describe an elephant in 20 words"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")