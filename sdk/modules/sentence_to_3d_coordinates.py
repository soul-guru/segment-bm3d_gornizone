from pprint import pprint

from sentence_transformers import SentenceTransformer
from transformers import BertModel, BertTokenizer
from sklearn.decomposition import PCA

from sdk.profile import profiler_point, profiler_close_point


def sentence_to_3d_coordinates(text: str, max_length: int = 1024) -> list[int]:
    model_name = 'bert-base-uncased'
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertModel.from_pretrained(model_name)
    # model = SentenceTransformer("thenlper/gte-large")
    
    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=max_length
    )
    
    point = profiler_point(f"model = BertModel.from_pretrained({model_name}); model('...')")
    outputs = model(**inputs)
    profiler_close_point(point) 
    
    last_hidden_states = outputs.last_hidden_state.squeeze().detach().numpy()
    
    if last_hidden_states.ndim == 1:
        last_hidden_states = last_hidden_states.reshape(1, -1)

    point = profiler_point("PCA(n_components=3, random_state=42)")
    pca = PCA(n_components=3, random_state=42)
    
    reduced_vectors = pca.fit_transform(last_hidden_states)
    profiler_close_point(point) 
    
    return reduced_vectors.mean(axis=0)
