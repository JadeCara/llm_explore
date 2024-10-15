from transformers import BartForConditionalGeneration, BartTokenizer


def summarize_document_with_bart(text, model_name="facebook/bart-large-cnn"):
    model = BartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BartTokenizer.from_pretrained(model_name)

    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", truncation=True)
    summary_ids = model.generate(
        inputs,
        max_length=150,
        min_length=30,
        num_beams=4,
        length_penalty=2.0,
        early_stopping=True,
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
