import mraa
import time

class Stepper:
    def __init__(self, number_of_steps,pin1,pin2,pin3=0,pin4=0):
        self.step_number = 0      # which step the motor is on
        self.speed = 0        # the motor speed, in revolutions per minute
        self.direction = 0      # motor direction
        self.last_step_time = 0    # time stamp in ms of the last step taken
        self.number_of_steps = number_of_steps    # total number of steps for this motor

        # setup the pins on the microcontroller:
        self.motor_pin_1 = mraa.Gpio(pin1)
        self.motor_pin_2 = mraa.Gpio(pin2)
        if not pin3 ==0: 
            self.motor_pin_3 = mraa.Gpio(pin3)
        if not pin4 ==0:
            self.motor_pin_4 = mraa.Gpio(pin4)
        
        self.motor_pin_1.dir(mraa.DIR_OUT)
        self.motor_pin_2.dir(mraa.DIR_OUT)

        if not pin3 ==0:
            self.motor_pin_3.dir(mraa.DIR_OUT)
        if not pin4 ==0:
            self.motor_pin_4.dir(mraa.DIR_OUT)


        self.pin_count = 4


    # Sets the speed in revs per minute   
    def setSpeed(self, whatSpeed):
        self.step_delay = 60L*1000L / self.number_of_steps /  whatSpeed
        
    # Moves the motor steps_to_move steps.  If the number is negative, 
    # the motor moves in the reverse direction.
    def step (self, steps_to_move):
        steps_left = abs(steps_to_move)
        if (steps_to_move > 0):
            self.direction = 1
        if (steps_to_move < 0):
            self.direction = 0

        # decrement the number of steps, moving one step each time:
        
        while(steps_left > 0):

            # move only if the appropriate delay has passed:
            if (long(time.time() * 1000) - self.last_step_time >= self.step_delay):
                # get the timeStamp of when you stepped:
                self.last_step_time = long(time.time() * 1000)
                # increment or decrement the step number,
                # depending on direction:
                if (self.direction == 1):
                    self.step_number = self.step_number + 1    
                    if (self.step_number == self.number_of_steps):
                        self.step_number = 0
                else:
                    if (self.step_number == 0) :
                        self.step_number = self.number_of_steps
        
                    self.step_number = self.step_number - 1
      
            # decrement the steps left:
            steps_left = steps_left - 1
            # step the motor to step number 0, 1, 2, or 3:
            self.stepMotor(self.step_number % 4)
      
    # Moves the motor forward or backwards.
    def stepMotor(self, thisStep):
        m = []

        if (thisStep == 0) : # 1010
            m = [1,0,1,0]
        elif (thisStep == 1) : # 0110
            m = [0,1,1,0]
        elif (thisStep ==  2):    # 0101
            m = [0,1,0,1]
        elif (thisStep == 3):   # 1001
            m = [1,0,0,1]

        self.motor_pin_1.write(m[0])
        self.motor_pin_2.write(m[1])
        self.motor_pin_3.write(m[2])
        self.motor_pin_4.write(m[3])



    def version(self):
    
        return 6
       
