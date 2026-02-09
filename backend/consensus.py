from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def consensus_output(texts: list[str]) -> str:
    sentences = []
    for t in texts:
        sentences.extend(t.split("."))

    embeddings = model.encode(sentences, convert_to_tensor=True)
    similarity = util.cos_sim(embeddings, embeddings)

    final_sentences = []
    for i, row in enumerate(similarity):
        if (row > 0.7).sum() >= 2:
            final_sentences.append(sentences[i])

    return ". ".join(set(final_sentences))
