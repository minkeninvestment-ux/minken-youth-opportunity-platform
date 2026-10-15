import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from minken_platform.recommender import YouthProfile, recommend_opportunities

def sample_df():
    return pd.DataFrame([
        {"title":"Data Skills","description":"Learn Python, statistics and data analysis","type":"Training","location":"Kenya / Remote","education_level":"secondary","skills":"python data statistics"},
        {"title":"Creative Careers","description":"Build a creative media portfolio","type":"Career Support","location":"Kenya","education_level":"secondary","skills":"design media portfolio"},
    ])

def test_data_profile_prefers_data_opportunity():
    profile = YouthProfile(skills="Python Excel", interests="data science", goal="learn data analysis", education="secondary", location="Kenya")
    result = recommend_opportunities(profile, sample_df(), top_k=1)
    assert result.iloc[0]["title"] == "Data Skills"
    assert 0 <= result.iloc[0]["score"] <= 1

def test_empty_profile_returns_no_recommendations():
    result = recommend_opportunities(YouthProfile(location=""), sample_df())
    assert result.empty

def test_missing_columns_raise_value_error():
    broken = pd.DataFrame([{"title":"Incomplete"}])
    try:
        recommend_opportunities(YouthProfile(skills="data"), broken)
    except ValueError as exc:
        assert "Missing required columns" in str(exc)
    else:
        raise AssertionError("Expected ValueError")
