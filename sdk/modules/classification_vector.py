from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from scipy.special import expit


def classification_vector(text: str) -> int:
    model_name: str = "cardiffnlp/tweet-topic-21-multi"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    
    tokens = tokenizer(text, return_tensors='pt')
    output = model(**tokens)
    
    scores = output[0][0].detach().numpy()
    scores = expit(scores)
    
    predictions = (scores >= 0.5) * 1
    
    return hash(tuple(predictions.tolist()))
