from django.http import HttpResponse, JsonResponse
import openai
import os
from dotenv import load_dotenv,dotenv_values

load_dotenv()

openai.my_api_key = os.getenv("OPENAI_API_KEY")

def userHome(req):
    print("You are in Home")
    return HttpResponse("Welcome to Home!")
   
def genItinerary(req):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Generate 2 days itinerary in Goa"}
        ],
        max_tokens=2500,
        temperature=0.6,
        frequency_penalty=1,
        presence_penalty=1
    )

    genratedIti = res['choices'][0]['message']['content']
    genIti_days = genratedIti.split('\n\n')
    itinerary = []
    for genDay in genIti_days:
        itinerary.append(genDay.split('\n'))

    return JsonResponse(itinerary, safe=False)
   

