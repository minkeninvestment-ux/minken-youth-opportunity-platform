/** Lightning adapter contract. No production adapter is included. */
export type InvoiceStatus = "unpaid" | "settled" | "expired";

export interface CreateInvoiceInput {
  /** Amount in whole satoshis; must be a positive safe integer. */
  amountSats: number;
  memo: string;
  /** Invoice expiry window. Defaults to 900 seconds. */
  expiresInSeconds?: number;
}

export interface LightningInvoice {
  id: string;
  /** In the mock adapter this is NOT a BOLT11 invoice and cannot be paid. */
  paymentRequest: string;
  amountSats: number;
  memo: string;
  createdAt: string;
  expiresAt: string;
  status: InvoiceStatus;
}

export interface LightningAdapter {
  createInvoice(input: CreateInvoiceInput): Promise<LightningInvoice>;
  getInvoice(invoiceId: string): Promise<LightningInvoice | undefined>;
}
