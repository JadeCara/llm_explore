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


if __name__ == "__main__":
    document_text = (
        """Artificial intelligence (AI) is intelligence demonstrated by machines, """
        """in contrast to the natural intelligence displayed by humans and animals."""
        """Leading AI textbooks define the field as the study of "intelligent agents": """
        """any device that perceives its environment and takes actions that maximize"""
        """its chance of successfully achieving its goals. Colloquially, the term """
        """"artificial intelligence" is often used to describe machines (or computers)"""
        """that mimic "cognitive" functions that humans associate with the human mind, """
        """such as "learning" and "problem solving"."""
    )

    summary = summarize_document_with_bart(document_text)

    print("Summary:")
    print(summary)
