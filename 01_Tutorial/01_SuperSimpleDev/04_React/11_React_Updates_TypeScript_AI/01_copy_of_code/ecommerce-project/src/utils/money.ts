// TypeScript does not have enough information to figure out the type.
// We have to set the type manually.
export function formatMoney(amoutCents: number) {
  // There are several ways to solve this. This is one example:
  // - Switch the negative number to positive using * -1.
  // - Put the negative sign at the front of the result.
  if (amoutCents < 0) {
    amoutCents = amoutCents * -1;
    return `-$${(amoutCents / 100).toFixed(2)}`;
  }

  return `$${(amoutCents / 100).toFixed(2)}`;
}
