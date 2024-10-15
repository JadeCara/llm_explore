from keybert import KeyBERT
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords_tfidf(documents, top_n=5):
    # Initialize the TF-IDF vectorizer
    vectorizer = TfidfVectorizer(max_df=0.85, stop_words='english')

    # Fit and transform the documents
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Extract the words and their TF-IDF scores
    feature_names = vectorizer.get_feature_names_out()

    # For each document, get the top N keywords
    keyword_dict = {}
    for doc_idx, doc in enumerate(tfidf_matrix):
        doc_vector = doc.toarray().flatten()
        top_indices = doc_vector.argsort()[-top_n:][::-1]
        top_keywords = [feature_names[i] for i in top_indices]
        keyword_dict[f"Document_{doc_idx+1}"] = top_keywords

    return keyword_dict


def extract_keywords_keybert(documents, top_n=5):
    model = KeyBERT()
    keyword_dict = {}

    for idx, doc in enumerate(documents):
        keywords = model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=top_n)
        keyword_dict[f"Document_{idx+1}"] = [keyword[0] for keyword in keywords]

    return keyword_dict


# Example usage
documents = [
    "Artificial intelligence is intelligence demonstrated by machines.",
    "Machine learning is a subset of AI focused on the development of algorithms.",
    "Deep learning is a subset of machine learning involving neural networks."
]
print("TFIDF:", extract_keywords_tfidf(documents))
print("KEYBERT:", extract_keywords_keybert(documents))
