
# main.py

from config.settings import ACTIVE_FINGERS
from grasping.grasp_presets import get_grasp_command


def main():
    print("Dexterous Hand AI Project")
    print("-------------------------")

    print("Active fingers:", ACTIVE_FINGERS)

    command = get_grasp_command("power_grasp")

    print("\nExample grasp command:")
    for finger, target in command.finger_targets.items():
        print(f"{finger}: {target:.2f}")

    print("\nCommand validation:", command.validate())


if __name__ == "__main__":
    main()
