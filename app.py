from pathlib import Path
import sys
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from minken_platform.recommender import YouthProfile, recommend_opportunities

st.set_page_config(page_title="Minken Youth Opportunity Platform", page_icon="🌍", layout="wide")
st.title("Minken Youth Opportunity Platform")
st.caption("Open-source AI/Data Science prototype for youth opportunity discovery")
st.info("Prototype only. Included opportunities are synthetic demonstration data, not live or verified listings.")

with st.sidebar:
    st.header("Your profile")
    skills = st.text_area("Skills", placeholder="e.g. communication, Excel, coding")
    interests = st.text_area("Interests", placeholder="e.g. technology, entrepreneurship, climate")
    goal = st.text_input("Goal", placeholder="e.g. find training and startup support")
    education = st.selectbox("Education level", ["any","primary","secondary","certificate","diploma","university"])
    location = st.text_input("Location", value="Kenya")
    top_k = st.slider("Number of recommendations", 1, 10, 5)

opportunities = pd.read_csv(ROOT / "data" / "sample_opportunities.csv")

if st.button("Find opportunities", type="primary"):
    profile = YouthProfile(skills=skills, interests=interests, goal=goal, education=education, location=location)
    results = recommend_opportunities(profile, opportunities, top_k=top_k)
    st.subheader("Recommended opportunities")
    if results.empty:
        st.warning("No recommendations were generated. Try adding more profile information.")
    else:
        for _, row in results.iterrows():
            with st.container(border=True):
                st.markdown(f"### {row['title']}")
                st.write(row["description"])
                c1, c2, c3 = st.columns(3)
                c1.metric("Match score", f"{row['score']:.0%}")
                c2.write(f"**Type:** {row['type']}")
                c3.write(f"**Location:** {row['location']}")
                st.write(f"**Why this matched:** {row['match_reason']}")
                st.caption("Synthetic opportunity for prototype demonstration only.")
else:
    st.markdown("""
### How it works
The prototype converts the profile text and each opportunity description into TF-IDF vectors, compares them using cosine similarity, and adds small transparent boosts for location and education alignment.

**This tool supports discovery; it does not determine eligibility, hiring, funding, credit, or admission decisions.**
""")
