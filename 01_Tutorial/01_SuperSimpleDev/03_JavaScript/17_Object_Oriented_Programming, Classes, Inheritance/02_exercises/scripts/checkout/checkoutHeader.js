import { cart } from "../../data/cart.js";

export function renderCheckoutHeader() {
  let cartQuantity = 0;

  cart.forEach((cartItem) => {
    cartQuantity += cartItem.quantity;
  });

  const checkoutHeaderHTML = `
    <div class="header-content">
      <div class="checkout-header-left-section">
        <a href="amazon.html">
          <img class="amazon-logo" src="images/amazon-logo.png">
          <img class="amazon-mobile-logo" src="images/amazon-mobile-logo.png">
        </a>
      </div>

      <div class="checkout-header-middle-section">
        Checkout (<a class="return-to-home-link js-return-to-home-link" href="amazon.html">${cartQuantity} items</a>)
      </div>

      <div class="checkout-header-right-section">
        <img src="images/icons/checkout-lock-icon.png">
      </div>
    </div>
  `; // 完美格式的template字符串要让``位于不同的两行，还要让它们中间空出一行，然后用Tab退一格，再粘贴，格式就完美了。

  document.querySelector(".js-checkout-header").innerHTML = checkoutHeaderHTML;
}

// 2026.09.07 11:16

// 2026.09.07 11:24
