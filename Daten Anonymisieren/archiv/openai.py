import openai



openai.api_key = 'xxx'


response = openai.Completion.create(
  engine='davinci',
  prompt='korrigiere den code',
  max_tokens=100
)

print(response.choices[0].text.strip())

