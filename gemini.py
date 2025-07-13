import google.generativeai as genai

genai.configure(api_key='AIzaSyAwBwCgVSDroSIVAe_j6-GYFZjcAiNi6Bs')

model = genai.GenerativeModel('gemini-1.5-flash')

def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

def text_summarization(text):
    response = model.generate_content(f"Summarize this: {text}")
    return response.text.strip()

def question_answer(context, question):
    response = model.generate_content(f"Context{context}\n Question:{question}")

def sentiment_analysis(text):
    response = model.generate_content(f"analyze the sentiment of this text: {text}")
    return response.text.strip()

def text_translation(text, target_language):
    response = model.generate_content(f"Translate this text into {target_language}: {text}")
    return response.text.strip()

if __name__ == "__main__":

    #1
    prompt = "The quick brown fox"
    print("Generate Text:", generate_text(prompt))

    #2 
    text = "The quick brown fox jumps over the lazy dog. Its a common example used in typography"
    print("Summary:", text_summarization(text))

    #3
    context = "The quick brown fox jumps over the lazy dog."
    question = "What does the fox jump over?"
    print("Answer:", question_answer(context, question))

    #4
    text = "The quick brown fox jumps gracefully over the lazy dog."
    print("Sentiment:", sentiment_analysis(text))

    #5
    text = "The quick brown fox jumps over the lazy dog."
    target_language = "Urdu"
    print("Translation:", text_translation(text, target_language))