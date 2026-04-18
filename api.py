from google import genai
from gtts import gTTS
import os
import io
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)

#note genarator
def generate_note(images):
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images, "Summraize The pictue in note formate at max 100-120 word, make sure add necessary markdown"]
    )
    return response.text

def generate_audio(txt):
    s1 = txt.replace("#","")
    s2 = s1.replace("*","")
    
    audio_buffer = io.BytesIO() # create a memory spece to write a audio
    
    audio = gTTS(text=s2,lang='en', slow=False)
    audio.write_to_fp(audio_buffer)
    
    return audio_buffer


def generate_quize(image, deficulty):
    
    resposce = client.models.generate_content(
        model= "gemini-3-flash-preview",
        contents= [image,f"Generate 5 to 10 Quize's with option's base on the deficulty {deficulty} with proper markdown also give correct answer"]
    )
    
    return resposce.text
    