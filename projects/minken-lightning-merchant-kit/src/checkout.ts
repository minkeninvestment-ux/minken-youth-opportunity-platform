import type { CreateInvoiceInput, LightningAdapter, LightningInvoice } from "./types.js";

/** A tiny provider-agnostic reference interface, not an HTTP service. */
export class CheckoutService {
  constructor(private readonly adapter: LightningAdapter) {}

  async start(input: CreateInvoiceInput): Promise<LightningInvoice> {
    if (!Number.isSafeInteger(input.amountSats) || input.amountSats <= 0) {
      throw new RangeError("amountSats must be a positive safe integer");
    }
    if (!input.memo || input.memo.trim().length > 200) {
      throw new RangeError("memo must contain 1–200 characters");
    }
    if (input.expiresInSeconds !== undefined &&
        (!Number.isSafeInteger(input.expiresInSeconds) || input.expiresInSeconds < 60 || input.expiresInSeconds > 3600)) {
      throw new RangeError("expiresInSeconds must be a whole number between 60 and 3600");
    }
    return this.adapter.createInvoice({ ...input, memo: input.memo.trim() });
  }

  async status(invoiceId: string): Promise<LightningInvoice | undefined> {
    if (!invoiceId.trim()) throw new RangeError("invoiceId must not be empty");
    return this.adapter.getInvoice(invoiceId);
  }
}
