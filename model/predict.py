import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
from utils.image_encoder import encode_image

# Load model & tokenizer
model = load_model("model/model.h5")
tokenizer = pickle.load(open("model/tokenizer.pkl", "rb"))

max_length = 34

def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

def generate_caption(image):
    photo = encode_image(image)

    in_text = "startseq"

    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)

        yhat = model.predict([photo, sequence], verbose=0)
        yhat = np.argmax(yhat)

        word = word_for_id(yhat, tokenizer)
        if word is None:
            break

        in_text += " " + word

        if word == "endseq":
            break

    final = in_text.replace("startseq", "").replace("endseq", "")
    return final.strip()
