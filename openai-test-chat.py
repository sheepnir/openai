from openai import OpenAI

# Create an OpenAI client instance
client = OpenAI()

# Define the content for the system role
system_content = "You are a fitness coach."

# Define the content for the user role
user_content = "I'm a 45 years old, beginner. Carft a plan for my first training."

# Create a chat completion request to the OpenAI API
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Specifies the model to use for generating responses
    messages=[
        # System message setting context for the AI
        {"role": "system", "content": system_content},
        # User message with a specific query for the AI
        {"role": "user", "content": user_content},
    ],
)

# Print the response from the AI
# Extracts and prints the AI's response from the completion object
print(completion.choices[0].message)
