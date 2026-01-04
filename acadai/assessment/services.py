from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def grade_text_answer(student_text: str, expected_text: str) -> float:
    if not student_text or not expected_text:
        return 0.0

    student_text = student_text.strip()
    expected_text = expected_text.strip()

    if len(student_text.split()) < 3 < len(expected_text.split()):
        return 0.0


    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1,2),
        min_df=1
    )

    try:
        tfidf = vectorizer.fit_transform([student_text, expected_text])
        similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
        return round(similarity, 2)
    except ValueError:
        return 0.0
