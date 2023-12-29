from openai import OpenAI

# Define the prompt as a variable
prompt_text = "A cute Weimaraner puppy"

# Create an OpenAI client instance
client = OpenAI()

# Use the prompt variable in the API call.n=2 makes two images.
response = client.images.generate(prompt=prompt_text, n=2, size="1024x1024")

# Print the response
print(response)
