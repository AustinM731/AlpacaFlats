import RPi.GPIO as GPIO

class CoverCalibratorDevice:
    """
    A device class for a cover calibrator, used in astronomical setups.
    """

    def __init__(self):
        self.connected = False
        self.calibrator_state = 1  # 0 for disabled, 1 for Off, 2 for CoolingDown, 3 for Ready, 4 for Unknown
        self.brightness = 0
        self.max_brightness = 100
        self.cover_state = 0  # 0 for absent, 1 for closed, 2 for moving, 3 for open, 4 for Unknown, 5 for Error
        self.pwm_pin = 12
        self.pwm_frequency = 100  # PWM frequency in Hz (100 Hz is a good starting point, bump this value if you see flickering)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm_device = GPIO.PWM(self.pwm_pin, self.pwm_frequency)

    def connect(self):
        """
        Connects to Flats Panel.
        """
        self.connected = True
        self.pwm_device.start(0)  # Initialize PWM with 0% duty cycle

    def disconnect(self):
        """
        Disconnects from Flats Panel.
        """
        if self.connected:
            self.pwm_device.stop()
            GPIO.cleanup()
            self.connected = False

    def turn_on(self, brightness):
        """
        Turns on the Flats Panel with the specified brightness level.
        """
        if self.connected:
            self.calibrator_state = 3
            self.brightness = brightness
            self.pwm_device.ChangeDutyCycle(brightness)
        else:
            raise Exception("Device not connected")

    def turn_off(self):
        """
        Turns off the Flats Panel.
        """
        if self.connected:
            self.brightness = 0
            self.calibrator_state = 1
            self.pwm_device.ChangeDutyCycle(0)
        else:
            raise Exception("Device not connected")

    def close_cover(self):
        """
        Closes the cover of the calibrator.
        """
        if self.connected:
            self.cover_state = 1
        else:
            raise Exception("Device not connected")

    def open_cover(self):
        """
        Opens the cover of the calibrator.
        """
        if self.connected:
            self.cover_state = 3
        else:
            raise Exception("Device not connected")

    def halt_cover(self):
        """
        Halts movement of the cover of the calibrator.
        """
        if self.connected:
            self.cover_state = 4
        else:
            raise Exception("Device not connected")

