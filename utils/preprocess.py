def clean_text(text):
    text = text.lower()
    text = text.replace("[^a-z]", "")
    return text
