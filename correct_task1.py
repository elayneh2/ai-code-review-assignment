from __future__ import annotations

from typing import Iterable, Mapping, Any


def calculate_average_order_value(orders: Iterable[Mapping[str, Any]]) -> float:
    """
    Calculate average order value across non-cancelled orders.

    - Excludes orders where status == "cancelled" (case-insensitive).
    - Raises ValueError if there are no non-cancelled orders to average.
    """
    total = 0.0
    counter = 0

    for order in orders:
        # Defensive access: treat missing status as non-cancelled only if explicitly desired.
        status = str(order.get("status", "")).strip().lower()
        if status == "cancelled":
            continue

        if "amount" not in order:
            raise KeyError("Order is missing required field: 'amount'")

        amount = order["amount"]
        try:
            total += float(amount)
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid order amount: {amount!r}") from e

        counter += 1

    if counter == 0:
        raise ValueError("Cannot compute AOV: no non-cancelled orders.")

    return total / counter
