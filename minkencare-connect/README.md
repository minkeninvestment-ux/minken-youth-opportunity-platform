# MinkenCare Connect — FemTech demonstration

**Developer:** Minken Investment Ltd (Minken Africa), Kenya  
**Status:** Early-stage *functional interface demonstration*, not a deployed clinical service or a validated health product.

This repository folder contains a small, accessible, browser-based prototype to illustrate aspects of the planned MinkenCare Connect project. Its design comes from the Minken Africa Super App concept: MinkenCare, MinkenVoice and future MinkenHealthNow modules.

## Run the demo

1. Download this folder (or clone this repository and check out `minkencare-connect-femtech`).
2. Open `minkencare-connect/index.html` in a browser, or start `python3 -m http.server 8000` from the repository root and browse to `http://localhost:8000/minkencare-connect/`.
3. Use the English / Kiswahili selector, search demo service options by county, create a local reminder, and generate a *draft-only* referral reference.

**No registration, API key or patient information is required.** All service-provider labels are synthetic and no clinical provider is verified or connected.

## Demonstrated functionality

- Responsive mobile-first interface with English and Kiswahili text.
- County-based service discovery against clearly labelled synthetic demonstration entries.
- Draft referral workflow that creates a local visual reference (no messages are sent).
- General appointment/reminder entry held in browser localStorage (no SMS, booking or server sync).
- Static guided support with short, prewritten explanations (not an AI chatbot, diagnosis or clinical triage).
- Accessibility-oriented labels and live status messaging.

## Intended future technology

The proposed full solution may integrate AI/NLP for multilingual information access, healthcare partner referral APIs, consent controls, secure cloud infrastructure and human clinical review. **These components are not implemented in this demo.** Do not represent this repository as evidence of a completed AI model, tested medical device, actual pilot, operational provider network or clinical safety validation.

## Ethics, privacy and safety

This demo must **not** be used for real medical decisions, emergencies, clinical referrals or sharing sensitive health information. There is no backend or clinical data handling. Only an optional appointment reminder is stored locally in the current browser; use **Clear** to erase it. No data is transmitted to Minken or third parties. Content is illustrative and awaits qualified clinical and safeguarding review before field use.

In an emergency, seek immediate help from a qualified local emergency service or healthcare provider. The demo has no escalation capability.

## Current evidence

- Functional interface: included in this folder.
- Clinical adviser and partner agreements: **not evidenced**.
- Real user testing / quantitative or qualitative pilot results: **not yet available**.
- Security assessment, ethics approval and compliance sign-off: **not performed**.
- Public hosting and production operation: **not implemented**.

## Roadmap

1. Co-design with women, adolescents and qualified Kenyan health professionals.
2. Define consent, safeguarding, privacy and clinical escalation requirements.
3. Build secure backend and appropriately governed provider integrations.
4. Add human-reviewed multilingual content and test AI features only with safety evaluation.
5. Conduct supervised usability testing and record actual quantitative and qualitative results.
6. Assess legal compliance and clinical safety before wider pilot or launch.

## Licensing

Apache-2.0, following the parent repository license. See [../LICENSE](../LICENSE).

## Contact

Minken Investment Ltd (Minken Africa) · [www.minkenafrica.co.ke](https://www.minkenafrica.co.ke) · minkeninvestment@gmail.com

> **Funding application integrity:** This source is a demonstration of an early concept. It does not by itself meet a funder's requirements for a validated working health product, pilot metrics or a real-team live-demo video.
