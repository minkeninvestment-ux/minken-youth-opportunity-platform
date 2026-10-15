# Minken Youth Opportunity Platform

Open-source AI and data science prototype for helping young people discover relevant jobs, skills programmes, entrepreneurship support, funding and financial-literacy opportunities.

> **Prototype status:** Early-stage open-source prototype. The included opportunity records are synthetic demonstration data and must not be treated as live, verified opportunities.

## Why this project exists

Young people often search across disconnected websites and networks for employment, training, entrepreneurship and funding opportunities. This prototype explores a transparent recommendation approach that ranks opportunities against a user's interests, skills, education, broad location and goals.

## What the prototype does

- Accepts a simple youth profile: skills, interests, goals, education level and broad location.
- Uses TF-IDF text vectorisation and cosine similarity to rank sample opportunities.
- Adds small transparent boosts for location and education-level alignment.
- Returns a human-readable explanation of why each opportunity was recommended.
- Runs locally through a Streamlit interface.
- Includes unit tests and GitHub Actions testing.

## Technology

Python 3.11+, pandas, scikit-learn, Streamlit and pytest.

The current method is intentionally lightweight and explainable. Future iterations may evaluate multilingual NLP, semantic embeddings and fairness-aware ranking only after appropriate user research, safeguarding review and data-governance controls.

## Quick start

```bash
git clone https://github.com/minkeninvestment-ux/minken-youth-opportunity-platform.git
cd minken-youth-opportunity-platform
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Run tests with:

```bash
pytest -q
```

## Open-source commitment

MINKEN INVESTMENT LTD (Minken Africa) intends this prototype to remain open and reusable. Contributions that improve accessibility, localisation, transparency, safeguarding and usefulness for underserved young people are welcome.

## Safety and safeguarding

This prototype is an opportunity-discovery aid. It must not be used to make automated decisions about hiring, credit, admissions, funding eligibility, public benefits or other high-impact outcomes.

Before any production deployment involving children or adolescents, the project should undergo dedicated safeguarding, privacy, security and responsible-AI review.

## Data

The records in `data/sample_opportunities.csv` are fictitious examples created only to demonstrate the matching engine. They are not live opportunities.

## License

Apache License 2.0. See [LICENSE](LICENSE).

## Organisation

Developed as an open-source prototype by **MINKEN INVESTMENT LTD (Minken Africa)**, Kenya.
