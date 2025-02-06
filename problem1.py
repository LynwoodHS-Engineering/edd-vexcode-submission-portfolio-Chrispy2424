Code:
    while True:
        distance = measure_distance()
        print(f"Distance: {distance} cm")

        control_motor1(distance)

        time.sleep(0.5)
