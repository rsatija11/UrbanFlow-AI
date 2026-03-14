import json

class PriorityOrchestrator:
    """
    The Decision Engine that calculates traffic light priority based on AI vision data.
    """
    def __init__(self):
        self.active_corridor = False

    def calculate_priority(self, vision_data):
        """Calculates the Green Corridor sequence if an emergency vehicle is detected."""
        if vision_data["is_emergency"] and vision_data["confidence"] > 0.9:
            self.active_corridor = True
            return {
                "signal_command": "GREEN_CORRIDOR_ACTIVATE",
                "priority_level": "LEVEL_1_CRITICAL",
                "duration_sec": 30
            }
        else:
            self.active_corridor = False
            return {
                "signal_command": "NORMAL_TRAFFIC_SEQUENCE",
                "priority_level": "LEVEL_0",
                "duration_sec": 60
            }
