# Minken Lightning Merchant Kit (MLMK)

**Status: public starter scaffold with mock checkout and tests. It does NOT connect to a real Bitcoin/Lightning node or process payments.**

A proposed MIT-licensed TypeScript toolkit for non-custodial merchant checkout experiences on the Bitcoin Lightning Network. Project sponsor: Minken Investment Ltd (Minken Africa), Nairobi, Kenya.

## Implemented today

- Provider-agnostic TypeScript LightningAdapter interface and CheckoutService
- In-memory MockLightningAdapter with explicitly NONPAYABLE demo invoice strings
- Four automated tests and an offline demo
- Development roadmap and security limitations

## Run

Requirements: Node.js 20+ and npm.

1. Run `npm install`
2. Run `npm test`
3. Run `npm run demo`

All simulated invoices begin with `DEMO_ONLY_NOT_A_REAL_LIGHTNING_INVOICE_` and cannot be paid.

## Proposed future work

Testable regtest adapter for LND or Core Lightning, invoice-status persistence, idempotent events, signed webhooks, a merchant checkout demo, and English/Swahili onboarding. These features are **proposed, not implemented**.

## Safety and limits

No real wallet, testnet, Lightning node, customer money, private keys, M-PESA settlement, production payment integration, or merchants are claimed. Do not use this code to transfer funds.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Proposed milestones](docs/ROADMAP.md)
- [Security](docs/SECURITY.md)
- [LAB funding concept](docs/FUNDING_PROPOSAL.md)
- [Contributing](CONTRIBUTING.md)

## Funding status

This project is a starter contribution, NOT a formal Let Africa Build grant application or award. LAB requires its separate official application form and GitHub project proposal. An African Lightning engineering lead has not yet been confirmed.

## License and contact

MIT License (c) 2026 Minken Investment Ltd. Office No. 5, Second Floor, Western Heights, Westlands, Nairobi, Kenya. https://www.minkenafrica.co.ke
