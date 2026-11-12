import { CheckoutService, MockLightningAdapter } from "../dist/index.js";

const adapter = new MockLightningAdapter();
const checkout = new CheckoutService(adapter);
const invoice = await checkout.start({ amountSats: 1200, memo: "Demo merchant order" });
console.log("Created DEMO ONLY invoice (cannot be paid):", invoice);
console.log("Simulated settlement:", adapter.settleForDemo(invoice.id));
console.log("Status:", (await checkout.status(invoice.id))?.status);
