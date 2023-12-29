import google.generativeai as genai

genai.configure(api_key="AIzaSyBrt3xPUMHQa1fVQgpKoXG0uNEFUECu7EU")
model_usual = genai.GenerativeModel('gemini-pro')
model_vision = genai.GenerativeModel('gemini-pro-vision')


def list_models() -> None:
    for m in genai.list_models():
        print(m)
        if "generateContent" in m.supported_generation_methods:
            print(m.name)

if __name__ == "__main__":
    list_models()