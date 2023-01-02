import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Classify the sentiment in these tweets: 1. Estou cansado de trabalhar neste projeto 2. Este bolo me parece bom 3. Estou satisfeito com esta tarefa.",
  temperature=0,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response['choices'][0]['text'])