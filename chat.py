# Importing the OpenAI library to interact with the OpenAI API.
from openai import OpenAI

def load_properties(filepath):
    # Initialize an empty dictionary to store properties
    props = {}

    # Open the properties file for reading
    with open(filepath, "r") as f:
        # Iterate over each line in the file
        for line in f:
            # Strip whitespace from the beginning and end of the line
            line = line.strip()

            # Ignore empty lines and lines that start with a '#' (comments)
            if line and not line.startswith("#"):
                # Split the line into key and value at the first '='
                key_value = line.split("=", 1)

                # Check if the line is properly formatted with a key and value
                if len(key_value) == 2:
                    # Assign the key-value pair to the dictionary
                    # Also stripping any leading/trailing whitespace from key and value
                    props[key_value[0].strip()] = key_value[1].strip()

    # Return the dictionary containing all the properties
    return props


# Defining the main function that encapsulates our chat functionality.
def main():
    # Load configuration properties
    config = load_properties("configuration.properties")
    system_content = config.get("system_content", "Default system content")

    # Initializing the OpenAI client.
    client = OpenAI()

    # Initializing chat_record as an empty list to store the chat history.
    chat_record = []

    # Starting an infinite loop to keep the conversation going.
    while True:
        try:
            # Prompting the user for input and providing an option to exit.
            user_content = input("What would you like to know? (Type 'exit' to quit): ")
            
            # Adding the user's message to the chat history.
            chat_record.append(f"User: {user_content}")
            
            # Checking if the user wants to exit the chat.
            if user_content.lower() == 'exit':
                break

            # Sending the user's question to the OpenAI API.
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": user_content}
                ]
            )

            # Extracting the AI's response and adding it to the chat history.
            ai_response = response.choices[0].message.content
            chat_record.append(f"AI: {ai_response}")

            # Printing the AI's response.
            print(ai_response)


        # Catching any exceptions that occur during the API call.
        except Exception as e:
            # Printing the error message.
            print(f"An error occurred: {e}")
    
    print("\nChat History:")
    for message in chat_record:
        print(message)

# Ensuring that the script runs only when executed directly (not imported).
if __name__ == "__main__":
    main()
