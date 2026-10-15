# Architecture

The prototype separates the Streamlit interface, recommendation engine and synthetic opportunity data.

```text
User profile -> Streamlit UI -> TF-IDF/cosine recommendation engine -> ranked opportunities + explanation
```

The design prioritises explainability, data minimisation and replaceable data sources. A production system would add authenticated administration, verified-source ingestion, moderation, audit logs, multilingual support, role-based access, encrypted storage, monitoring and safeguarding controls.
