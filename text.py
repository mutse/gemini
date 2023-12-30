import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key=os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Who are you?")
print(response.text)
