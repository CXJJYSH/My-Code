export function formatMoney(amoutCents) {
  return `$${(amoutCents / 100).toFixed(2)}`;
}
