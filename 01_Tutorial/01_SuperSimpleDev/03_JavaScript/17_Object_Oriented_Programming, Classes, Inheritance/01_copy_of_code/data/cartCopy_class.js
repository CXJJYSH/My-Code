import { validDeliveryOption } from "./deliveryOptions.js";

class Cart {
  cartItems; // Public property
  #localStorageKey; // Private property

  constructor(localStorageKey) {
    this.#localStorageKey = localStorageKey;
    this.#loadFromStorage();
  } // **this** points to the object that we generate

  #loadFromStorage() {
    // Shorthand Method Syntax
    // Regular function syntax here.
    // Not an arrow function.
    this.cartItems = JSON.parse(localStorage.getItem(this.#localStorageKey));

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
  }

  saveToStorage() {
    localStorage.setItem(this.#localStorageKey, JSON.stringify(this.cartItems));
  }

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
  }

  removeFromCart(productId) {
    const newCart = [];

    this.cartItems.forEach((cartItem) => {
      if (cartItem.productId !== productId) {
        newCart.push(cartItem);
      }
    });

    this.cartItems = newCart;

    this.saveToStorage();
  }

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
  }
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

// 2026.09.09 12:06

const cart = new Cart("cart-oop"); // 这里的参数是给constructor的。
const businessCart = new Cart("cart-business");

console.log(cart);
console.log(businessCart);

console.log(businessCart instanceof Cart);
