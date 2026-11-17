
# tests/test_commands.py

import pytest

from interfaces.commands import HandCommand
from grasping.grasp_presets import get_grasp_command


def test_power_grasp_has_four_fingers():
    command = get_grasp_command("power_grasp")

    assert command.validate()
    assert len(command.finger_targets) == 4


def test_invalid_curl_is_rejected():
    command = HandCommand(
        finger_targets={
            "thumb": 0.0,
            "index": 0.5,
            "middle": 1.5,
            "ring": 0.0,
        }
    )

    with pytest.raises(ValueError):
        command.validate()


def test_missing_finger_is_rejected():
    command = HandCommand(
        finger_targets={
            "thumb": 0.0,
            "index": 0.5,
            "middle": 0.5,
        }
    )

    with pytest.raises(ValueError):
        command.validate()
