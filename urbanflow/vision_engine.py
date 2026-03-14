import random
import time

class VisionEngine:
    """
    Simulates a Computer Vision model identifying emergency vehicle signatures.
    (Mocking YOLO/ResNet-based detection for Urban Traffic)
    """
    def __init__(self, sensitivity=0.95):
        self.sensitivity = sensitivity
        self.vehicle_classes = ["Ambulance", "Fire_Truck", "Police_Cruiser", "Civilian_Car"]

    def process_frame(self):
        """Simulates camera data processing to detect emergency vehicle presence."""
        detected = random.choice(self.vehicle_classes)
        confidence = round(random.uniform(0.85, 0.99), 2)
        
        is_emergency = detected in ["Ambulance", "Fire_Truck", "Police_Cruiser"]
        
        return {
            "object": detected,
            "confidence": confidence,
            "is_emergency": is_emergency
        }

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
