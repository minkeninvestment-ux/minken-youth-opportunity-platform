# Architecture

## Implemented

Local demo and tests -> CheckoutService -> LightningAdapter -> MockLightningAdapter (in-memory, nonpayable strings).

- CheckoutService validates amount, memo and expiry.
- The mock stores invoice status in memory for deterministic demonstrations.
- No network, persistence, wallet or live Lightning node exists.

## Proposed only

Merchant example -> TypeScript SDK / Node.js API -> LND or Core Lightning adapter -> isolated regtest -> idempotent event log -> authenticated webhooks.

The regtest adapter, authentication, production security, and payment processing are **not implemented**.
