import { renderCheckoutHeader } from "./checkout/checkoutHeader.js";
import { renderOrderSummary } from "./checkout/orderSummary.js";
import { renderPaymentSummary } from "./checkout/paymentSummary.js";
// import "../data/cartCopy_class.js"; // Run all the code
import "../data/car.js";
// import "../data/backend_practice.js";
import { loadProducts, loadProductsFetch } from "../data/products.js";
import { loadCart, loadCartFetch } from "../data/cartCopy.js";

async function loadPage() {
  try {
    // throw "error1";

    // const value = await new Promise((resolve, reject) => {
    //   // throw "error2";
    //   loadCart(() => {
    //     // reject("error3");
    //     resolve("value3");
    //   });
    // });

    await Promise.all([loadProductsFetch(), loadCartFetch()]);
  } catch (error) {
    console.log("Unexpected error. Please try again later.");
  }

  renderCheckoutHeader();
  renderOrderSummary();
  renderPaymentSummary();

  // return "value2"; // converted to resolve('value2');
}
loadPage();

// Promise.all([
//   loadProductsFetch(),

//   new Promise((resolve) => {
//     loadCart(() => {
//       resolve();
//     });
//   }),
// ]).then((values) => {
//   console.log(values);
//   renderCheckoutHeader();
//   renderOrderSummary();
//   renderPaymentSummary();
// });

// new Promise((resolve) => {
//   loadProducts(() => {
//     resolve("value1");
//   });
// })
//   .then((value) => {
//     console.log(value);

//     return new Promise((resolve) => {
//       loadCart(() => {
//         resolve();
//       });
//     });
//   })
//   .then(() => {
//     renderCheckoutHeader();
//     renderOrderSummary();
//     renderPaymentSummary();
//   });

// loadProducts(() => {
//   loadCart(() => {
//     renderCheckoutHeader();
//     renderOrderSummary();
//     renderPaymentSummary();
//   });
// });

// 2026.09.07 11:17

// 2026.09.07 11:24

// 2026.09.14 13:52
