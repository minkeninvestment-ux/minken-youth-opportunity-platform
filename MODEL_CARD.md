# Model Card

**Version:** 0.1.0  
**Type:** TF-IDF vectorisation + cosine similarity + transparent rule-based boosts.  
**Purpose:** Rank opportunity descriptions against self-described skills, interests, goals, education and broad location.

## Limitations
Text similarity may miss context, synonyms and multilingual nuance. Simple ranking can over-reward repeated keywords. The prototype has not been validated on representative real-world user data. Scores are not probabilities of success or eligibility.
