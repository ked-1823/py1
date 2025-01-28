import random

responses = {
    "hello": ["hii there!", "hello buddy!", "heyy!, how can I assist you"],
    "how are you": ["I am fine, what about you?", "I am great, thanks for asking"],
    "bye": ["bye bro, have a good day!", "bye", "see you later", "bye, take care"],
    "mkc": ["tu mkc","ae ji gali kahe de rahe ho!!","tu bsdk"],
    "time":["right now its {time}."]
}

fallback_response = "didn't understand"

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "time" in user_input:
        current_time=time.strftime('%H:%M:%S')
        return
    random.choice(responses["time"]).format(time=current_time)
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])  # Fixed: return the random choice

    return fallback_response  # This should be outside the for loop

print("I am your chatbot. Type 'bye' to exit")  # Fixed: capitalization and spacing
while True:  # Fixed: capitalization of True
    user_input = input("you: ")
    if "bye" in user_input.lower():
        print("chatbot: goodbye")
        break
    response = chatbot_response(user_input)
    print(f"chatbot: {response}")