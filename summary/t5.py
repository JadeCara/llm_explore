from transformers import T5ForConditionalGeneration, T5Tokenizer

def summarize_document(text, model_name="t5-small", max_length=150, min_length=30, do_sample=False):
    """
    Summarizes a given document using the specified Hugging Face model.

    Args:
        text (str): The text of the document to summarize.
        model_name (str): The name of the pre-trained model to use from Hugging Face.
        max_length (int): Maximum length of the summary.
        min_length (int): Minimum length of the summary.
        do_sample (bool): Whether or not to sample for the summary generation.

    Returns:
        str: The summarized text.
    """

    model = T5ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    input_text = "summarize: " + text
    inputs = tokenizer.encode(input_text, return_tensors="pt", truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length,
                                 length_penalty=2.0, num_beams=4, early_stopping=True,
                                 do_sample=do_sample)

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

if __name__ == "__main__":
    document_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.
    Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize
    its chance of successfully achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines (or computers)
    that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving".
    """

    summary = summarize_document(document_text, model_name="t5-small")

    print("Summary:")
    print(summary)
