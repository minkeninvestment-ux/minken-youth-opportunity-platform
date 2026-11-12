import test from "node:test";
import assert from "node:assert/strict";
import { CheckoutService, MockLightningAdapter } from "../dist/index.js";

test("mock checkout creates a clearly unpayable demo invoice", async () => {
  const checkout = new CheckoutService(new MockLightningAdapter(() => 1_700_000_000_000));
  const invoice = await checkout.start({ amountSats: 1200, memo: " Shop purchase " });
  assert.equal(invoice.amountSats, 1200);
  assert.equal(invoice.memo, "Shop purchase");
  assert.match(invoice.paymentRequest, /^DEMO_ONLY_NOT_A_REAL_LIGHTNING_INVOICE_/);
  assert.equal(invoice.status, "unpaid");
});

test("invalid amount and expiry are rejected", async () => {
  const checkout = new CheckoutService(new MockLightningAdapter());
  await assert.rejects(() => checkout.start({ amountSats: 0, memo: "Order" }), RangeError);
  await assert.rejects(() => checkout.start({ amountSats: 1.5, memo: "Order" }), RangeError);
  await assert.rejects(() => checkout.start({ amountSats: 100, memo: "Order", expiresInSeconds: 5 }), RangeError);
});

test("settlement and expiry are simulated only by the mock", async () => {
  let now = 1_700_000_000_000;
  const adapter = new MockLightningAdapter(() => now);
  const checkout = new CheckoutService(adapter);
  const paid = await checkout.start({ amountSats: 100, memo: "Order" });
  assert.equal(adapter.settleForDemo(paid.id), true);
  assert.equal((await checkout.status(paid.id))?.status, "settled");
  const expiring = await checkout.start({ amountSats: 100, memo: "Order", expiresInSeconds: 60 });
  now += 60_000;
  assert.equal((await checkout.status(expiring.id))?.status, "expired");
  assert.equal(adapter.settleForDemo(expiring.id), false);
});

test("status lookup returns undefined for unknown invoice", async () => {
  const checkout = new CheckoutService(new MockLightningAdapter());
  assert.equal(await checkout.status("does-not-exist"), undefined);
});
