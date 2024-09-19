import nmap3 
from groq import Groq

client = Groq(
    # This is the default and can be omitted
    api_key="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",
)
nmap3 = nmap3.Nmap()
results = nmap3.scan_top_ports("scanme.nmap.org")

print(results)

#set GROQ_API_KEY in the secrets

msg = str(results)

# Create the Groq client

# Set the system prompt
system_prompt = {
    "role": "system",
    "content":msg +
    "Summarize the data properly highlighting the open and closed ports and protocols used"
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
