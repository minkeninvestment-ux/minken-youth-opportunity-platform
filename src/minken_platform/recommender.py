from __future__ import annotations

from dataclasses import dataclass
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@dataclass(frozen=True)
class YouthProfile:
    skills: str = ""
    interests: str = ""
    goal: str = ""
    education: str = "any"
    location: str = "Kenya"

    def as_text(self) -> str:
        parts = [self.skills, self.interests, self.goal]
        if self.education and self.education.strip().lower() != "any":
            parts.append(self.education)
        if self.location and self.location.strip():
            parts.append(self.location)
        return " ".join(part.strip() for part in parts if part and part.strip())

def _normalise(value: object) -> str:
    return str(value or "").strip().lower()

def recommend_opportunities(profile: YouthProfile, opportunities: pd.DataFrame, top_k: int = 5) -> pd.DataFrame:
    required = {"title","description","type","location","education_level","skills"}
    missing = required.difference(opportunities.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if opportunities.empty:
        return opportunities.assign(score=pd.Series(dtype=float), match_reason=pd.Series(dtype=str))

    profile_text = profile.as_text().strip()
    if not profile_text:
        return pd.DataFrame(columns=list(opportunities.columns) + ["score","match_reason"])

    docs = (
        opportunities["title"].fillna("") + " " +
        opportunities["description"].fillna("") + " " +
        opportunities["type"].fillna("") + " " +
        opportunities["skills"].fillna("")
    ).tolist()

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vectorizer.fit_transform([profile_text] + docs)
    scores = cosine_similarity(matrix[0:1], matrix[1:]).flatten()

    output = opportunities.copy().reset_index(drop=True)
    output["score"] = scores
    reasons = []

    profile_location = _normalise(profile.location)
    profile_education = _normalise(profile.education)

    for idx, row in output.iterrows():
        bits = []
        location_text = _normalise(row["location"])
        education_text = _normalise(row["education_level"])

        if profile_location and (profile_location in location_text or "kenya" in location_text or "remote" in location_text):
            output.at[idx, "score"] += 0.08
            bits.append("location alignment")
        if profile_education not in {"","any"} and (profile_education in education_text or "any" in education_text):
            output.at[idx, "score"] += 0.06
            bits.append("education alignment")
        if not bits:
            bits.append("text similarity to your stated skills, interests and goal")
        reasons.append(", ".join(bits))

    output["score"] = output["score"].clip(lower=0, upper=1)
    output["match_reason"] = reasons
    return output.sort_values(["score","title"], ascending=[False,True]).head(max(1,int(top_k))).reset_index(drop=True)
