from itertools import combinations
from collections import defaultdict


def extract_relationships(documents, keyword_dict):
    relationships = defaultdict(list)

    for idx, doc in enumerate(documents):
        keywords = keyword_dict[f"Document_{idx+1}"]
        # Get all combinations of keywords in a document
        for pair in combinations(keywords, 2):
            relationships[pair[0]].append(pair[1])
            relationships[pair[1]].append(pair[0])

    return relationships
