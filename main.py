from nlp import extract_required_entities
from vision import detect_text

access_token_NLP = "AIzaSyD68bu29Fz6o5SA1XgmKKnEFLsT2GANQew"
access_token_VIS = "AIzaSyDjPaFGT8u9INRU9r7JA2a7_syWkNdAPzU"

def extract_entities_from_img(img_path):

    text = detect_text(img_path, access_token_NLP)
    #entities = extract_required_entities(text, access_token_VIS)

    return text
	
print (extract_entities_from_img("DL.jpg"))
