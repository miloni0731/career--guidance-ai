import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def compute_cosine_similarity(vec1, vec2):
    """Compute cosine similarity between two vectors."""
    return cosine_similarity(vec1.reshape(1, -1), vec2.reshape(1, -1))[0][0]

def find_most_similar(query_vec, candidate_vecs, candidate_texts):
    """Find the most similar text from candidates."""
    similarities = [
        compute_cosine_similarity(query_vec, vec)
        for vec in candidate_vecs
    ]
    max_idx = np.argmax(similarities)
    return candidate_texts[max_idx], similarities[max_idx]

def get_top_k_similar(query_vec, candidate_vecs, candidate_texts, k=3):
    """Get top k most similar texts from candidates."""
    similarities = [
        compute_cosine_similarity(query_vec, vec)
        for vec in candidate_vecs
    ]
    top_k_indices = np.argsort(similarities)[-k:][::-1]
    return [
        (candidate_texts[idx], similarities[idx])
        for idx in top_k_indices
    ] 