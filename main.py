import openai

provider = "text-davinci-003"
openai.api_key = "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"
sentiment = "Classify the sentiment in these tweets: 1. Estou cansado de trabalhar neste projeto 2. Este bolo me parece bom 3. Estou satisfeito com esta tarefa."

response = openai.Completion.create(
  model=provider,
  prompt=classifier,
  temperature=0,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response['choices'][0]['text'])
