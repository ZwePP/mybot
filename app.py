import os
from dotenv import load_dotenv
from openai import OpenAI

#Environment Setup
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API")
GPT_MODEL = os.getenv("GPT_MODEL")

client = OpenAI(
    api_key=OPENAI_API_KEY
)

#GPT Function
def gpt_response(user_prompt):
    response = client.responses.create(
    model=GPT_MODEL,
    input = [
        {"role": "system", 
         "content": """You are an assistant that have knowledge in IT field. \
        Generate best responses as simple as possible. \
        If you can't find the resource or don't know the answer, be direct. 
        Avoid generating too many words in a sentence. Only keypoints """},

        {
            "role" : "user",
            "content" : "What is the optimal temperature for computer operation?"
        },
        {
            "role": "assistant",
            "content" : f"Optimal temperature range: 30% - 50%. - prevent static electricity -reduce risks of corrosion"
        },


        {"role": "user", 
         "content": user_prompt}
    ],
    )
    string_response = response.output[0].content[0].text
    return string_response




if __name__ == "__main__":
    user_input = input("Input: ")
    while(user_input != 'q'):
        answer = gpt_response(user_input)
        print(answer)
        user_input = input("Input (q to exit!): ")
