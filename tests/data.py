# Load model directly
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("yanekyuk/camembert-keyword-extractor")
model = AutoModelForTokenClassification.from_pretrained("yanekyuk/camembert-keyword-extractor")


print(model("I'm thinking of taking up a new hobby, like painting or photography. I want something creative to relax and express myself"))