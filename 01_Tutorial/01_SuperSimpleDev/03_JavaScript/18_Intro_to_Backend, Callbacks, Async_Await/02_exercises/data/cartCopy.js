import { validDeliveryOption } from "./deliveryOptions.js";

export let cart;

loadFromStorage();

export function loadFromStorage() {
  cart = JSON.parse(localStorage.getItem("cart"));

  if (!cart) {
    cart = [
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

function saveToStorage() {
  localStorage.setItem("cart", JSON.stringify(cart));
}

export function addToCart(productId) {
  let matchingItem;

  cart.forEach((cartItem) => {
    if (productId === cartItem.productId) {
      matchingItem = cartItem;
    }
  });

  if (matchingItem) {
    matchingItem.quantity += 1;
  } else {
    cart.push({
      productId: productId,
      quantity: 1,
      deliveryOptionId: "1",
    });
  }

  saveToStorage();
}

export function removeFromCart(productId) {
  const newCart = [];

  cart.forEach((cartItem) => {
    if (cartItem.productId !== productId) {
      newCart.push(cartItem);
    }
  });

  cart = newCart;

  saveToStorage();
}

export function updateDeliveryOption(productId, deliveryOptionId) {
  let matchingItem;

  cart.forEach((cartItem) => {
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

  saveToStorage();
}

// 2026.09.07 18:00

// 16l

// 2026.09.08 19:52

// 16m

// 2026.09.08 20:07

// 2026.09.08 20:30

export function loadCart(fun) {
  const xhr = new XMLHttpRequest();

  xhr.addEventListener("load", () => {
    console.log(xhr.response);

    fun();
  });

  xhr.open("GET", "https://supersimplebackend.dev/cart");
  xhr.send();
}

export async function loadCartFetch() {
  const response = await fetch("https://supersimplebackend.dev/cart");
  const text = await response.text();
  console.log(text);
  return text;
}

// Extra feature: make the cart empty after creating an order.
export function resetCart() {
  cart = [];
  saveToStorage();
}

export function calculateCartQuantity() {
  let cartQuantity = 0;

  cart.forEach((cartItem) => {
    cartQuantity += cartItem.quantity;
  });

  return cartQuantity;
}

export function updateQuantity(productId, newQuantity) {
  let matchingItem;

  cart.forEach((cartItem) => {
    if (productId === cartItem.productId) {
      matchingItem = cartItem;
    }
  });

  matchingItem.quantity = newQuantity; // 这里不是复制出一个新的对象，而是让matchingItem指向同一个对象。

  saveToStorage(); // 这个是另外编写的一个函数，不是JS内置的。
}

export function updateCartQuantity() {
  const cartQuantity = calculateCartQuantity();

  document.querySelector(".js-cart-quantity").innerHTML = cartQuantity;
}
