class Heart:
    def __init__(self, usage):
        self.usage = usage
    @property
    def state(self):
        if self.usage>70:
            return "high blood pressure"
        else: 
            return "feeling good"
class Brain:
    def __init__(self, usage):
        self.usage = usage

    @property
    def state(self):
        if self.usage>90:
            return "tired"
        else: 
            return "rested"

class Leg:
    def __init__(self, person, moving_speed):
        self.person = person
        self.moving_speed = moving_speed
       
    
    @property
    def motion(self):
        if self.moving_speed>10:
            return "running"
        else:
            return "walking"

class Person:
    def __init__(self, usage):
        self.heart = Heart(usage)
        self.brain = Brain(usage)


