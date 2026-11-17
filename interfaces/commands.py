
# interfaces/commands.py

from dataclasses import dataclass
from typing import Dict

from config.settings import ACTIVE_FINGERS


@dataclass
class HandCommand:
    """
    Robot-independent hand command.

    Each finger receives a normalized target:
        0.0 = open
        1.0 = fully curled
    """

    finger_targets: Dict[str, float]
    status: str = "ok"

    def validate(self):
        expected = set(ACTIVE_FINGERS)
        received = set(self.finger_targets)

        if received != expected:
            raise ValueError(
                f"Expected fingers {expected}, "
                f"received {received}"
            )

        for finger, value in self.finger_targets.items():
            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Invalid target for {finger}: {value}"
                )

        return True
