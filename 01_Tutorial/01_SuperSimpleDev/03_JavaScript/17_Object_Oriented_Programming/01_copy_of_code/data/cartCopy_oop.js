import { validDeliveryOption } from "./deliveryOptions.js";

function Cart() {
  const cart = {
    cartItems: undefined,

    loadFromStorage() {
      // Shorthand Method Syntax
      // Regular function syntax here.
      // Not an arrow function.
      this.cartItems = JSON.parse(localStorage.getItem("cart-oop"));

      if (!this.cartItems) {
        this.cartItems = [
          {
            productId: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
            quantity: 2,
            deliveryOptionId: "1",
          },
          {
            productId: "15b6fc6f-327a-4ec4-896f-486349e85a3d",
            quantity: 1,
            deliveryOptionId: "2",
          },
        ];
      }
    },

    saveToStorage() {
      localStorage.setItem("cart-oop", JSON.stringify(this.cartItems));
    },

    addToCart(productId) {
      let matchingItem;

      this.cartItems.forEach((cartItem) => {
        if (productId === cartItem.productId) {
          matchingItem = cartItem;
        }
      });

      if (matchingItem) {
        matchingItem.quantity += 1;
      } else {
        this.cartItems.push({
          productId: productId,
          quantity: 1,
          deliveryOptionId: "1",
        });
      }

      this.saveToStorage();
    },

    removeFromCart(productId) {
      const newCart = [];

      this.cartItems.forEach((cartItem) => {
        if (cartItem.productId !== productId) {
          newCart.push(cartItem);
        }
      });

      this.cartItems = newCart;

      this.saveToStorage();
    },

    updateDeliveryOption(productId, deliveryOptionId) {
      let matchingItem;

      this.cartItems.forEach((cartItem) => {
        if (productId === cartItem.productId) {
          matchingItem = cartItem;
        }
      });

      if (!matchingItem) {
        return;
      }

      if (!validDeliveryOption(deliveryOptionId)) {
        return;
      }

      matchingItem.deliveryOptionId = deliveryOptionId;

      this.saveToStorage();
    },
  };

  return cart;
}

// export let cart;
// A shortcut for **export let cart = undefined;**

// 2026.09.07 18:00

// 16l

// 2026.09.08 19:52

// 16m

// 2026.09.08 20:07

// 2026.09.08 20:30

// OOP

// 2026.09.09 11:26

const cart = Cart();
const businessCart = Cart();

cart.loadFromStorage();

businessCart.loadFromStorage();

console.log(cart);
console.log(businessCart);

// 2026.09.09 12:06
