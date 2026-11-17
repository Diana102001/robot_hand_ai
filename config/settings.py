
# config/settings.py

PROJECT_NAME = "Vision-Controlled Dexterous Hand"

ACTIVE_FINGERS = [
    "thumb",
    "index",
    "middle",
    "ring",
]

NUM_ACTIVE_FINGERS = len(ACTIVE_FINGERS)

# Human finger curl convention:
# 0.0 = fully open
# 1.0 = fully curled

MIN_CURL = 0.0
MAX_CURL = 1.0

# Initial perception settings
HAND_DETECTION_CONFIDENCE = 0.5
OBJECT_DETECTION_CONFIDENCE = 0.5
