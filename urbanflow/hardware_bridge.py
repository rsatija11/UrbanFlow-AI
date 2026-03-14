class HardwareBridge:
    """
    Communicates with the Traffic Light Controllers over SPI and I2C protocols.
    Inspired by Smart Traffic System (IEEE MSIT Leadership project).
    """
    def __init__(self, protocol="I2C"):
        self.protocol = protocol
        print(f"[HW_INIT] Wireless Traffic Controller Bridge using {self.protocol} is ONLINE.")

    def transmit_to_lights(self, command):
        """Simulates sending bitwise commands to microcontroller-based traffic lights."""
        if command == "GREEN_CORRIDOR_ACTIVATE":
            print(f"[{self.protocol} TX] ðŸš¨ PRIORITY OVERRIDE. Signal Phase: ALL_GREEN for Lane_A. ALL_RED for intersecting lanes.")
        else:
            print(f"[{self.protocol} TX] Signal Phase: Normal Cycling.")
