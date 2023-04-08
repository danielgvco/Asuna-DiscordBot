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
        max_tokens=1500,
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

def high_moderation(message, rules):
    system_prompt = helper.get_value_from_json("resources/openai_prompts.json", "follow_rules")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": system_prompt.format(rules=rules)},
        {"role": "user", "content": f"{message}"}
        ],
        temperature=0,
        max_tokens=2,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    response = completion.choices[0].message['content']
    clean_response = response.replace(".", "")
    boolean_response = ast.literal_eval(clean_response)
    return boolean_response