def evaluate_resume(text, keywords):
    score = 0
    feedback = []
    match_count = 0

    for keyword in keywords:
        if keyword.lower() in text.lower():
            feedback.append(f"✅ Keyword found: {keyword}")
            match_count += 1
        else:
            feedback.append(f"❌ Missing keyword: {keyword}")

    score = int((match_count / len(keywords)) * 100)
    return score, feedback

