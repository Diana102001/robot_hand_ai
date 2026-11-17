
# grasping/grasp_presets.py

from interfaces.commands import HandCommand


GRASP_PRESETS = {
    "open_hand": {
        "thumb": 0.0,
        "index": 0.0,
        "middle": 0.0,
        "ring": 0.0,
    },

    "power_grasp": {
        "thumb": 0.8,
        "index": 0.9,
        "middle": 0.9,
        "ring": 0.9,
    },

    "precision_grasp": {
        "thumb": 0.3,
        "index": 0.4,
        "middle": 0.1,
        "ring": 0.0,
    },
}


def get_grasp_command(grasp_name: str) -> HandCommand:
    if grasp_name not in GRASP_PRESETS:
        raise ValueError(f"Unknown grasp: {grasp_name}")

    command = HandCommand(
        finger_targets=GRASP_PRESETS[grasp_name].copy()
    )

    command.validate()
    return command
