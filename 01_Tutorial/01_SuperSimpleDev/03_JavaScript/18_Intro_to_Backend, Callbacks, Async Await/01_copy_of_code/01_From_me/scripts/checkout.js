import { renderCheckoutHeader } from "./checkout/checkoutHeader.js";
import { renderOrderSummary } from "./checkout/orderSummary.js";
import { renderPaymentSummary } from "./checkout/paymentSummary.js";
// import "../data/cartCopy_class.js"; // Run all the code
import "../data/car.js";
// import "../data/backend_practice.js";
import { loadProducts } from "../data/products.js";

loadProducts(() => {
  renderCheckoutHeader();
  renderOrderSummary();
  renderPaymentSummary();
});

// 2026.09.07 11:17

// 2026.09.07 11:24

// 2026.09.14 13:52
