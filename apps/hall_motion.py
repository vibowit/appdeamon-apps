import hassapi as hass

MOTION = "binary_sensor.hall_occupancy"
LIGHT = "light.hall"
SWITCH = ""


class HallMotion(hass.Hass):

    def initialize(self):
        self.listen_state(self.motion, MOTION, new="on")
        self.manual_switch = False

    def motion(self, entity, attribute, old, new, kwargs):
        self.log("Hall motion detected")
        if self.self.sun_down():
            self.turn_on(LIGHT)
            self.run_in(self.light_off, 60)

    def light_off(self, kwargs):
        self.turn_off(LIGHT)
