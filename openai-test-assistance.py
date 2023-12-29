from openai import OpenAI

# Create an OpenAI client instance
client = OpenAI()

# Define the assistant
assistant_name = "Fitness Coach"
assistant_instructions = "You are a personal training with 20 year expereince working with 40+ men with shoulder injuries."

# Define the assistant
assistant = client.beta.assistants.create(
    name=assistant_name,
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview",
)

thread = client.beta.threads.create()

