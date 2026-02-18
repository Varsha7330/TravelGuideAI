import google.generativeai as genai

genai.configure(api_key="AIzaSyAzcoFa8C1kmiITDbdQLCMcaKBMV02dSJ0")

for m in genai.list_models():
    print(m.name, m.supported_generation_methods)
