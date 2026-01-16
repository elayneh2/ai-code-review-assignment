from __future__ import annotations

from typing import Iterable, Any


def average_valid_measurements(values: Iterable[Any]) -> float:
    """
    Average numeric measurements, ignoring missing/invalid entries.

    - Ignores None values.
    - Ignores values that cannot be converted to float.
    - Raises ValueError if there are no valid numeric values.
    """
    total = 0.0
    counter = 0

    for value in values:
        if value is None:
            continue

        try:
            total += float(v)
        except (TypeError, ValueError):
            # Ignore invalid entries rather than failing the whole aggregation.
            continue

        counter += 1

    if counter == 0:
        raise ValueError("Cannot compute average: no valid numeric measurements.")

    return total / counter
