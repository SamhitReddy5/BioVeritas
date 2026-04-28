# FAST VERSION — no API lag for demo

def verification_score(sentence):
    sentence = sentence.lower()

    fake_keywords = [
        "cure", "instant", "garlic", "lemon", "bleach",
        "herbal", "miracle", "detox", "home remedy"
    ]

    score = 0

    for word in fake_keywords:
        if word in sentence:
            score -= 0.25  # strong penalty

    return score