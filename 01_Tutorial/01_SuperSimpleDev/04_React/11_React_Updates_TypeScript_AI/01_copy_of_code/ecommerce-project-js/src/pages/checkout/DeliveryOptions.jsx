import dayjs from "dayjs";
import axios from "axios";
import { formatMoney } from "../../utils/money";

export function DeliveryOptions({ cartItem, deliveryOptions, loadCart }) {
  return (
    <div className="delivery-options">
      <div className="delivery-options-title">Choose a delivery option:</div>

      {deliveryOptions.map((deliveryOption) => {
        let priceString = "FREE Shipping";

        if (deliveryOption.priceCents > 0) {
          priceString = `${formatMoney(deliveryOption.priceCents)} - Shipping`;
        }

        const updateDeliveryOption = async () => {
          await axios.put(`/api/cart-items/${cartItem.productId}`, {
            deliveryOptionId: deliveryOption.id,
          });

          await loadCart();
        };

        return (
          <div
            key={deliveryOption.id}
            className="delivery-option"
            onClick={updateDeliveryOption}
          >
            <input
              type="radio"
              checked={deliveryOption.id === cartItem.deliveryOptionId}
              // 前面的是这个选项固定的id，后面的是上面的函数更改的当前货物的快递方案id。
              onChange={() => {}}
              className="delivery-option-input"
              name={`delivery-option-${cartItem.productId}`}
            />
            <div>
              <div className="delivery-option-date">
                {dayjs(deliveryOption.estimatedDeliveryTimeMs).format(
                  "dddd, MMMM D",
                )}
              </div>
              <div className="delivery-option-price">{priceString}</div>
            </div>
          </div>
        );
      })}
    </div>
  );
}
