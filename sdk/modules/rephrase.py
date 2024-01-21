import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration


def rephrase(text: str) -> list[str]:
    device = torch.device("cuda") if torch.cuda.is_available() else "cpu"

    model_name: str = "unikei/t5-base-split-and-rephrase"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)
    
    if device == 'cuda':
        model = model.half()
        
    complex_tokenized = tokenizer(
        text, 
        padding="max_length", 
        truncation=True,
        max_length=256, 
        return_tensors='pt'
    )
    
    # Перемещаем тензоры на то же устройство, что и модель
    complex_tokenized = {k: v.to(device) for k, v in complex_tokenized.items()}

    simple_tokenized = model.generate(
        complex_tokenized['input_ids'],
        attention_mask=complex_tokenized['attention_mask'],
        max_length=256,
        num_beams=3
    )
    
    simple_sentences = tokenizer.batch_decode(
        simple_tokenized,
        skip_special_tokens=True
    )
    
    return simple_sentences
