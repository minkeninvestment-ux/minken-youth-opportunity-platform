import type { CreateInvoiceInput, LightningAdapter, LightningInvoice } from "../types.js";

/** Fake backend for deterministic demos ONLY: no funds, keys, network or BOLT11. */
export class MockLightningAdapter implements LightningAdapter {
  private readonly invoices = new Map<string, LightningInvoice>();
  private nextId = 1;

  constructor(private readonly clock: () => number = () => Date.now()) {}

  async createInvoice(input: CreateInvoiceInput): Promise<LightningInvoice> {
    const now = this.clock();
    const id = `demo-invoice-${this.nextId++}`;
    const invoice: LightningInvoice = {
      id,
      paymentRequest: `DEMO_ONLY_NOT_A_REAL_LIGHTNING_INVOICE_${id}`,
      amountSats: input.amountSats,
      memo: input.memo,
      createdAt: new Date(now).toISOString(),
      expiresAt: new Date(now + (input.expiresInSeconds ?? 900) * 1000).toISOString(),
      status: "unpaid"
    };
    this.invoices.set(id, invoice);
    return { ...invoice };
  }

  async getInvoice(id: string): Promise<LightningInvoice | undefined> {
    const invoice = this.invoices.get(id);
    if (!invoice) return undefined;
    if (invoice.status === "unpaid" && this.clock() >= Date.parse(invoice.expiresAt)) {
      invoice.status = "expired";
    }
    return { ...invoice };
  }

  /** Demo-only local simulation; never expose through a payment API. */
  settleForDemo(id: string): boolean {
    const invoice = this.invoices.get(id);
    if (!invoice || invoice.status !== "unpaid" || this.clock() >= Date.parse(invoice.expiresAt)) return false;
    invoice.status = "settled";
    return true;
  }
}
