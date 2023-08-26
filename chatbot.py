import openai

openai.api_key = "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"
model_engine = "text-davinci-003"
chatbot_prompt = """
Imagine yourself as a personal trainer. Your primary goal is to assist users to the best of your ability. This may involve answering questions, 
providing helpful information, or completing tasks based on user input. In order to effectively assist users, it is important to be detailed and thorough in your responses. 
Use examples and evidence to support your points and justify your recommendations or solutions.

Here is an example:
 I'm lactose intolerance. Can I substitute it with different product?
Chatbot: Sure, I can help you with that. What kind of dietary changes are you looking to make? Are you looking to cut calories, reduce carbohydrates, or focus on a specific type of food?

<conversation_history>
User: <user_input>
Chatbot:"""


def get_response(conversation_history, user_input):
    prompt = chatbot_prompt.replace(
        "<conversation_history>", conversation_history).replace("<user input>", user_input)

    # Get the response from GPT-3
    response = openai.Completion.create(
        engine=model_engine, prompt=prompt, max_tokens=2048, n=1, stop=None, temperature=0.5)

    # Extract the response from the response object
    response_text = response["choices"][0]["text"]

    chatbot_response = response_text.strip()

    return chatbot_response


def main():
    conversation_history = ""

    while True:
        user_input = input("> ")
        if user_input == "exit":
            break
        chatbot_response = get_response(conversation_history, user_input)
        print(f"Chatbot: {chatbot_response}")
        conversation_history += f"User: {user_input}\nChatbot: {chatbot_response}\n"

main()