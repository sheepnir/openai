# Importing the OpenAI library to interact with the OpenAI API.
from openai import OpenAI

# Defining the main function that encapsulates our chat functionality.
def main():
    # Initializing the OpenAI client.
    client = OpenAI()

    # Defining the system's role and its expertise.
    system_content = "You are a fitness expert in men over 40 with shoulder pain"

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
