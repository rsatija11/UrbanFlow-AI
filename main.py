import json
from urbanflow.vision_engine import VisionEngine
from urbanflow.priority_logic import PriorityOrchestrator
from urbanflow.hardware_bridge import HardwareBridge

# This logic is moved to urbanflow/priority_logic.py in the previous turn by mistake, 
# I will fix the import in this main script and use the correct structure.

def run_simulation():
    print("===========================================")
    print(" ðŸš¦ UrbanFlow-AI: Autonomous Traffic System")
    print("===========================================")

    # Initialize components
    vision = VisionEngine()
    brain = PriorityOrchestrator()
    hw = HardwareBridge(protocol="SPI")

    print("\n--- Processing Live Urban Intersection Feed ---")
    
    # Simulate a single detection cycle
    frame_data = vision.process_frame()
    decision = brain.calculate_priority(frame_data)

    print(f"Vision Data: {json.dumps(frame_data)}")
    print(f"AI Decision: {json.dumps(decision, indent=2)}")
    print("-------------------------------------------")

    # Final Hardware Command
    hw.transmit_to_lights(decision["signal_command"])

if __name__ == "__main__":
    run_simulation()
