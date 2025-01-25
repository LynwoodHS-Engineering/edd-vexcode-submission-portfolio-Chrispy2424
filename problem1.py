Code:
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG_PIN = 23
ECHO_PIN = 24

MOTOR_PIN = 18

GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(MOTOR_PIN, GPIO.OUT)

pwm = GPIO.PWM(MOTOR_PIN, 1000)  
pwm.start(0)  

def measure_distance():
    GPIO.output(TRIG_PIN, GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, 
                
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        start_time = time.time()

    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        end_time = time.time()


    pulse_duration = end_time - start_time
    distance = pulse_duration * 17150  
    distance = round(distance, 2)  
    return distance

def control_motor(distance)

    if distance < 10:
        pwm.ChangeDutyCycle(100) 
    elif distance < 20:
        pwm.ChangeDutyCycle(75)   
    elif distance < 30:
        pwm.ChangeDutyCycle(50)   
    elif distance < 40:
        pwm.ChangeDutyCycle(25) 
    else:
        pwm.ChangeDutyCycle(0)   
try:
    while True:
        distance = measure_distance()
        print(f"Distance: {distance} cm")

        control_motor(distance)

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program stopped by user.")
    pwm.stop()
    GPIO.cleanup()
