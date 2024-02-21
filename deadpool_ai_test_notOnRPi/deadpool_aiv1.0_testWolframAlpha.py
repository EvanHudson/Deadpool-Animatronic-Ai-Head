import openai
import pyttsx3
import wikipedia
import difflib
import wolframalpha
import requests

app_id = "7PTKWL-RQ6U3QAJX3" # Directly set the app_id with your API key
client = wolframalpha.Client(app_id)
    


def get_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        response.raise_for_status()  # Check for HTTP errors
        return response.json()["ip"]
    except requests.RequestException as e:
        print(f"Error fetching IP: {e}")
        return None
# OpenAI API key
openai.api_key = "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"

# Specify the path to your text file using single-quotes
file_path = r'C:\Users\robot\AppData\Local\Programs\Python\Python311\deadpool_ai\deadpool_prompt.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the entire content of the file into a string
    deadpool_prompt = file.read()

# Now, deadpool_prompt contains the string read from the file
print(deadpool_prompt)

# Rest of your code...
Deadpool = True
# Initial conversation history
conversation_history = [
    {"role": "system", "content": deadpool_prompt},
    {"role": "user", "content": deadpool_prompt},  # Include content from the file in the conversation
]

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

while True:
    # Get user input
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    try:
        location = get_ip()
        query_url = f"http://api.wolframalpha.com/v1/conversation.jsp?" \
                    f"appid={app_id}" \
                    f"&geolocation={app_id}" \
                    f"&i={user_input}" \

        r = requests.get(query_url).json()
        answer = r["result"]
        conversation_id = r["conversationID"]
        host = r["host"]

        user_input+=f"From wolfram Api: {answer}"
    except:
        print(" ")
    # Break the loop if the user enters "exit" or an empty input
    
   # Check if the user is asking to look up something on Wikipedia
    if "wikipedia" in user_input.lower():
        # Extract the search term from the user input
        search_terms_to_remove = ["wikipedia", "look up", "in", "on"]
        search_term = user_input
        for term in search_terms_to_remove:
            search_term = search_term.replace(term, "").strip()

        try:
            # Perform the Wikipedia search
            wikipedia_page = wikipedia.summary(search_term)
            user_input = f"from Wikipedia API: {wikipedia_page} if it has nothing to do with the topic then inform the user that the found wiki is not correct and only talk about the title of the wikipedia page and give suggested wikipedia titles that cover that topic. User input: {user_input}"
            print(search_term + ' ' + wikipedia_page)
        except wikipedia.exceptions.PageError:
            user_input += "No Wikipedia page found for the given input tell the user to try to use a different title/ search term."
            print("Error: No Wikipedia page found.")

    if Deadpool:
        # Add user input to conversation history
        messages = conversation_history + [{"role": "user", "content": user_input}]

        # Make API call
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
        )

        # Get and print assistant's response
        #curse censor replacement
        deadpool_response = response['choices'][0]['message']['content'].strip()
        deadpool_response=deadpool_response.replace("F*ck","Fuck")
        deadpool_response=deadpool_response.replace("f*ck","fuck")
        deadpool_response=deadpool_response.replace("Sh*t","Shit")
        deadpool_response=deadpool_response.replace("sh*t","shit")
        deadpool_response=deadpool_response.replace("D*ck","Dick")
        deadpool_response=deadpool_response.replace("d*ck","dick")
        deadpool_response=deadpool_response.replace("*nt","unt")
        deadpool_response=deadpool_response.replace("*tch","itch")
        deadpool_response=deadpool_response.replace("*ck","ock")
        deadpool_response=deadpool_response.replace("a**","ass")
        deadpool_response=deadpool_response.replace("b*lls","balls")
        deadpool_response=deadpool_response.replace("w*nker","wanker")
        deadpool_response=deadpool_response.replace("*ssy","ussy")
        deadpool_response=deadpool_response.replace("*ss","ass")
        deadpool_response=deadpool_response.replace("d*mn","damn")
        deadpool_response=deadpool_response.replace("t*ts","tits")
        deadpool_response=deadpool_response.replace("wh*re","whore")
        deadpool_response=deadpool_response.replace("sl*t","slut")
        deadpool_response=deadpool_response.replace("*ll","ell")
        deadpool_response=deadpool_response.replace("t*t","tit")
        deadpool_response=deadpool_response.replace("b*tt","butt")
        deadpool_response=deadpool_response.replace("tw*t","twat")



        print(f"Deadpool: {deadpool_response}")

        # Set the voice to a male voice
        engine.setProperty('gender', 'male')
      

        # Speak the assistant's response
        engine.say(deadpool_response)
        engine.runAndWait()

        # Add assistant's response to conversation history
        conversation_history = messages + [{"role": "assistant", "content": deadpool_response}]
