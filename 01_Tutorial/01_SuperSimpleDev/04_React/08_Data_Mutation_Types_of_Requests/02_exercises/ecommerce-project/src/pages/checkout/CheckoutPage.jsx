import axios from "axios";
import { useState, useEffect } from "react";
import { CheckoutHeader } from "./CheckoutHeader";
import { OrderSummary } from "./OrderSummary";
import { PaymentSummary } from "./PaymentSummary";
import "./CheckoutPage.css";

export function CheckoutPage({ cart, loadCart }) {
  const [deliveryOptions, setDeliveryOptions] = useState([]);
  const [paymentSummary, setPaymentSummary] = useState(null);

  // This useEffect will only run once.
  useEffect(() => {
    // const fetchCheckoutData = async () => {
    //   const response = await axios.get(
    //     "/api/delivery-options?expand=estimatedDeliveryTime",
    //   );
    //   setDeliveryOptions(response.data);
    // };
    // fetchCheckoutData();
    // const fetchPaymentData = async () => {
    //   const response = await axios.get("/api/payment-summary");
    //   setPaymentSummary(response.data);
    // };
    // fetchPaymentData();
    // 上面的是我写的，我写了两个分开的。
    // 下面的是Simon写的，他把两个合并了，复用了一个变量，所以要把该变量用let声明。

    const fetchCheckoutData = async () => {
      const response = await axios.get(
        "/api/delivery-options?expand=estimatedDeliveryTime",
      );
      setDeliveryOptions(response.data);
    };

    fetchCheckoutData();
  }, []);

  // 哎呀我去，上面我本来就已经分开写了，这个地方自己做主处理得很好。
  useEffect(() => {
    const fetchPaymentSummary = async () => {
      const response = await axios.get("/api/payment-summary");
      setPaymentSummary(response.data);
    };

    fetchPaymentSummary();
  }, [cart]);

  return (
    <>
      <title>Checkout</title>

      <link rel="icon" type="image/svg+xml" href="cart-favicon.png" />

      <CheckoutHeader cart={cart} />

      <div className="checkout-page">
        <div className="page-title">Review your order</div>

        <div className="checkout-grid">
          <OrderSummary
            cart={cart}
            deliveryOptions={deliveryOptions}
            loadCart={loadCart}
          />

          <PaymentSummary paymentSummary={paymentSummary} loadCart={loadCart} />
        </div>
      </div>
    </>
  );
}
