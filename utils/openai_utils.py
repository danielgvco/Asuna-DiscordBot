import os
import openai
from dotenv import load_dotenv
from . import helper
import ast

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

def generate_chat(messages):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    response = completion.choices[0].message['content']
    return response

def generate_text(message):
    completions = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=200,
        temperature=0
    )
    message = completions.choices[0].text
    response =  message.strip()
    return response

def basic_moderation(message):
    response = openai.Moderation.create(
        input=message
    )
    flagged = response["results"][0]["flagged"]
    return flagged

def high_moderation(message):
    clean_message = message.replace("\n", " ").replace("\"", "")
    prompt = helper.get_value_from_json("resources/openai_prompts.json", "follow_rules").format(clean_message=clean_message)
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0
    )

    answer = response.choices[0].text.strip().lower()
    clean_answer = answer.replace(".", "")
    
    final_answer = helper.true_or_false(clean_answer)
    print(final_answer)
    print(type(final_answer))
    return final_answer