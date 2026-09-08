import {
  addToCart,
  cart,
  loadFromStorage,
  removeFromCart,
  updateDeliveryOption,
} from "../../data/cartCopy.js";

describe("test suite: addToCart", () => {
  beforeEach(() => {
    spyOn(localStorage, "setItem");
  });

  it("adds an existingg product to the cart", () => {
    spyOn(localStorage, "getItem").and.callFake(() => {
      return JSON.stringify([
        {
          productId: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
          quantity: 1,
          deliveryOptionId: "1",
        },
      ]);
    });
    loadFromStorage();

    addToCart("e43638ce-6aa0-4b85-b27f-e1d07eb678c6");
    expect(cart.length).toEqual(1);

    expect(localStorage.setItem).toHaveBeenCalledTimes(1);
    expect(localStorage.setItem).toHaveBeenCalledWith(
      "cart",
      JSON.stringify([
        {
          productId: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
          quantity: 2, // 加了一个已有的商品之后商品数量从一到了二。
          deliveryOptionId: "1",
        },
      ]),
    );

    expect(cart[0].productId).toEqual("e43638ce-6aa0-4b85-b27f-e1d07eb678c6");
    expect(cart[0].quantity).toEqual(2);
  });

  it("adds a new product to the cart", () => {
    spyOn(localStorage, "getItem").and.callFake(() => {
      return JSON.stringify([]);
    });
    loadFromStorage();

    addToCart("e43638ce-6aa0-4b85-b27f-e1d07eb678c6");
    expect(cart.length).toEqual(1);

    expect(localStorage.setItem).toHaveBeenCalledTimes(1);
    expect(localStorage.setItem).toHaveBeenCalledWith(
      "cart",
      JSON.stringify([
        {
          productId: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
          quantity: 1,
          deliveryOptionId: "1",
        },
      ]),
    );
    expect(cart[0].productId).toEqual("e43638ce-6aa0-4b85-b27f-e1d07eb678c6");
    expect(cart[0].quantity).toEqual(1);
  });
});

describe("test suite: removeFromCart", () => {
  beforeEach(() => {
    spyOn(localStorage, "setItem");
  });

  it("removes a product from the cart", () => {
    spyOn(localStorage, "getItem").and.callFake(() => {
      return JSON.stringify([
        {
          productId: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
          quantity: 1,
          deliveryOptionId: "1",
        },
      ]);
    });

    loadFromStorage();

    removeFromCart("e43638ce-6aa0-4b85-b27f-e1d07eb678c6");

    expect(cart.length).toEqual(0);
    expect(localStorage.setItem).toHaveBeenCalledTimes(1);
    expect(localStorage.setItem).toHaveBeenCalledWith(
      "cart",
      JSON.stringify([]),
    );
  });

  it("does nothing if product is not in the cart", () => {
    spyOn(localStorage, "getItem").and.callFake(() => {
      return JSON.stringify([
        {
          productId: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
          quantity: 1,
          deliveryOptionId: "1",
        },
      ]);
    });

    loadFromStorage();

    removeFromCart("does-not-exist");

    expect(cart.length).toEqual(1);
    expect(cart[0].productId).toEqual("e43638ce-6aa0-4b85-b27f-e1d07eb678c6");
    expect(cart[0].quantity).toEqual(1);
    expect(localStorage.setItem).toHaveBeenCalledTimes(1);
    expect(localStorage.setItem).toHaveBeenCalledWith(
      "cart",
      JSON.stringify([
        {
          productId: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
          quantity: 1,
          deliveryOptionId: "1",
        },
      ]),
    );
  });
});

describe("test suite: updateDeliveryOption", () => {
  beforeEach(() => {
    spyOn(localStorage, "setItem");
  });

  it("basic test: updates the delivery opiton", () => {
    spyOn(localStorage, "getItem").and.callFake(() => {
      return JSON.stringify([
        {
          productId: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
          quantity: 1,
          deliveryOptionId: "1",
        },
      ]);
    });

    loadFromStorage();

    updateDeliveryOption("e43638ce-6aa0-4b85-b27f-e1d07eb678c6", "3");

    expect(cart.length).toEqual(1);
    expect(cart[0].productId).toEqual("e43638ce-6aa0-4b85-b27f-e1d07eb678c6");
    expect(cart[0].quantity).toEqual(1);
    expect(cart[0].deliveryOptionId).toEqual("3");
    expect(localStorage.setItem).toHaveBeenCalledTimes(1);
    expect(localStorage.setItem).toHaveBeenCalledWith(
      "cart",
      JSON.stringify([
        {
          productId: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
          quantity: 1,
          deliveryOptionId: "3",
        },
      ]),
    );
  });

  it("edge test: does nothing if the product is not in the cart", () => {
    spyOn(localStorage, "getItem").and.callFake(() => {
      return JSON.stringify([
        {
          productId: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
          quantity: 1,
          deliveryOptionId: "1",
        },
      ]);
    });

    loadFromStorage();

    updateDeliveryOption("does-not-exist", "3");

    expect(cart.length).toEqual(1);
    expect(cart[0].productId).toEqual("e43638ce-6aa0-4b85-b27f-e1d07eb678c6");
    expect(cart[0].quantity).toEqual(1);
    expect(cart[0].deliveryOptionId).toEqual("1");
    expect(localStorage.setItem).toHaveBeenCalledTimes(0);
  });
});

// 2026.09.07 18:00

// 16d

// 2026.09.08 14:58

// 16e

// 2026.09.08 15:01

// 16k

// 2026.09.08 19:36
