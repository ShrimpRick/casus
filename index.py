from hub import port
import runloop
import distance_sensor
import color_sensor
import motor
import motor_pair
import force_sensor

async def main():
    speed = -100 # the riding speed
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.E) # this pairs both wheels to eachother

    def forward():
        motor_pair.move(motor_pair.PAIR_1, 0, velocity=speed) # ride forward in a straight line

    def leftturn():
        motor_pair.move_tank(motor_pair.PAIR_1, -10, -100) # ride to the left, because the left wheel spins slower then the right

    def rightturn():
        motor_pair.move_tank(motor_pair.PAIR_1, -100, -10) # ride to the right, because the right wheel spins slower then the left

    def grijpvast(): # this function is to close the griphook
        motor.run(port.B, 1000)


    def grijplos(): # this  function is to open the griphook
        motor.run(port.B, -1000)

        

    def grijpswitch(variable): # this function is made so that the hook keeps closed, or opened when riding on other colors, but changes when it rides over blue
        if variable == 0:
            return 1
        return 0

    # this sets the standard options for the variables
    loop = True
    variable = 1
    waitbuttonpress = 1
    while loop:

        if force_sensor.pressed(port.F) == True: # this is the button, which acts as a emergency button. It stops or starts the robots loop
            if waitbuttonpress == 0:
                waitbuttonpress = 1
            else:
                waitbuttonpress = 0
            
        elif  waitbuttonpress == 0:
            motor_pair.stop(motor_pair.PAIR_1)
            continue

        colordetect = color_sensor.color(port.A) # this is a variable which uses the color sensor to know which color he is riding on
        if colordetect == 0: # 0 = black, which lets it ride forward (color has to be changed depending on the color used on the track)
            forward()
        elif colordetect == 10: # 10 = white, which lets it ride to the right (color has to be changed depending on the colors and direction of the track)
            rightturn()
        elif colordetect == 9: # 9 = red, which lets him ride to the left (color has to be changed depending on the colors and direction of the track)
            leftturn()
        elif colordetect == 3: # 3 = blue, which lets him change the variable number, so it either opens or closes the griphook (color has to be changed depending on the color used on the track)
            variable = grijpswitch(variable)
        elif colordetect == 7: # 7 = yellow, which stops the loop, means it is the end (color has to be changed depending on the color used on the track)
            loop = False
            motor_pair.stop(motor_pair.PAIR_1)

        if variable == 0: # this is the variable used to know if the griphook has to be closed or opened
            grijpvast()
        else:
            grijplos()

runloop.run(main()) # this runs the robots program
