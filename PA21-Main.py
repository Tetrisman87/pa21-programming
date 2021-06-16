variable_CelebrationTimer = 0
variable_V = 130
variable_R = 2

def user_defined_celebrationDance():

    global variable_CelebrationTimer
    global variable_V
    global variable_R
    
    #Rotate right for 10 seconds
    #chassis_ctrl.rotate_with_time(rm_define.clockwise, 10) --Blocking execution of the next command until over
    chassis_ctrl.rotate(rm_define.clockwise) #Should continue until stopped; May stop at each wait command
    
    #Loops 10 times
    variable_CelebrationTimer = 0
    while not variable_CelebrationTimer >= 10:
    
        # (255, 0, 0) = Red
        # (255, 0, 150) = Pink
        # (224, 0, 255) = Violet
        # (100, 0, 100) = Purple
        # (36, 103, 255) = Blue
        # (69, 215, 255) = Cyan
        # (0, 127, 70) = Good Green
        # (0, 255, 0) = Better Green
        # (161, 255, 69) = Lime Green
        # (255, 193, 0) = Yellow
        # (255, 50, 0) = Orange
        # (255, 255, 255) = White
        # (0, 0, 0) = Black
        
        #One full loop: 2.9 seconds
        #Total Time: 29 Seconds
        
        #Progress the loop
        variable_CelebrationTimer = variable_CelebrationTimer + 1
        
        #Moves robot in circle
        while True:
            variable_V = 130
            variable_R = 2
            chassis_ctrl.set_wheel_speed(variable_V - variable_V / variable_R,variable_V + variable_V / variable_R,variable_V - variable_V / variable_R,variable_V + variable_V / variable_R)
            time.sleep(0.5)
        
        # Red
        led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 255, 0, 0, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 255, 0, 0, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 255, 0, 0, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 255, 0, 0, rm_define.effect_always_on)
        time.sleep(0.1)

        # Pink
        led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 255, 0, 150, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 255, 0, 150, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 255, 0, 150, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 255, 0, 150, rm_define.effect_always_on)
        time.sleep(0.1)

        # Violet
        led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 224, 0, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 224, 0, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 224, 0, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 224, 0, 255, rm_define.effect_always_on)
        time.sleep(0.1)

        # Purple
        led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 100, 0, 100, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 100, 0, 100, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 100, 0, 100, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 100, 0, 100, rm_define.effect_always_on)
        time.sleep(0.1)

        # Blue
        led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 36, 103, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 36, 103, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 36, 103, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 36, 103, 255, rm_define.effect_always_on)
        time.sleep(0.1)

        # Cyan
        led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 69, 215, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 69, 215, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 69, 215, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 69, 215, 255, rm_define.effect_always_on)
        time.sleep(0.1)

        # Green
        led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 0, 255, 0, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 0, 255, 0, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 0, 255, 0, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 0, 255, 0, rm_define.effect_always_on)
        time.sleep(0.1)

        # Lime Green
        led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 161, 255, 69, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 161, 255, 69, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 161, 255, 69, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 161, 255, 69, rm_define.effect_always_on)
        time.sleep(0.1)

        # Yellow
        led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 255, 193, 0, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 255, 193, 0, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 255, 193, 0, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 255, 193, 0, rm_define.effect_always_on)
        time.sleep(0.1)

        # Orange
        led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 255, 50, 0, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 255, 50, 0, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 255, 50, 0, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 255, 50, 0, rm_define.effect_always_on)
        time.sleep(0.1)

        # White
        led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 255, 255, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 255, 255, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 255, 255, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 255, 255, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        
        # Blue
        led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 36, 103, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 36, 103, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 36, 103, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 36, 103, 255, rm_define.effect_always_on)
        time.sleep(0.1)
        
        #Quick succession of 5 random colors
        for count in range(5):
            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, random.randint(0,255), random.randint(0,255), random.randint(0,255), rm_define.effect_always_on)
            time.sleep(0.5)


def user_defined_initialStartup():

    global variable_CelebrationTimer
    global variable_V
    global variable_R
    
    #Set Movement Mode
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    
    #Enable smart vision detection
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.enable_detection(rm_define.vision_detection_pose)
    
    #Set max distance for vision detection
    vision_ctrl.set_marker_detection_distance(2)
    
    #Set color of markers to detect
    vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_red)
    
    #Enable Joy-Stick
    chassis_ctrl.enable_stick_overlay()
    
    #Set Armor Sensitivity (LAB ONLY -- Doesn't work in solo play)
    armor_ctrl.set_hit_sensitivity(8)
    
    #Set Rotational & Directional Speed
    chassis_ctrl.set_rotate_speed(180) # 180 degrees per second
    chassis_ctrl.set_trans_speed(2.5)  # 2.5 meteres per second
    
    #Set LED Blinking Speed
    led_ctrl.set_flash(rm_define.armor_all, 8)
    time.sleep(0.5)
    
    #Set all LEDs to red to signify setup in progress
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_breath)
    
    #Test Rotations NOTE: Rotate with time doesn't seem very accurate to it's degrees per second
    chassis_ctrl.rotate_with_time(rm_define.clockwise, 1)
    time.sleep(0.3)
    chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 1)
    time.sleep(0.3)
    chassis_ctrl.rotate_with_time(rm_define.clockwise, 2)
    time.sleep(0.3)
    chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 2)
    time.sleep(2)
    
    #Test Movement
    chassis_ctrl.move_with_distance(0,1)
    time.sleep(0.3)
    chassis_ctrl.move_with_distance(180,1)
    time.sleep(0.3)
    chassis_ctrl.move_with_distance(90,1)
    time.sleep(0.3)
    chassis_ctrl.move_with_distance(-90,1)
    time.sleep(2)
    
    #Test Arm Movement & Reset Position
    robotic_arm_ctrl.recenter(wait_for_complete=True)
    for count in range(3):
        while not (gripper_ctrl.is_open()):
            robotic_arm_ctrl.moveto(-200, -50, wait_for_complete=False)
            gripper_ctrl.open()
        gripper_ctrl.stop()
        while not (gripper_ctrl.is_closed()):
            robotic_arm_ctrl.moveto(50, 200, wait_for_complete=False)
            gripper_ctrl.close()
        gripper_ctrl.stop()
    robotic_arm_ctrl.recenter(wait_for_complete=True)
    

    
    #Set all LEDs to green to signify setup complete
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_always_on)
    time.sleep(3)
    rmexit()

#def ir_distance_1_ge_10_event(msg): -- Infared distance sensor not installed, causes program to break
#    global variable_CelebrationTimer
#    global variable_V
#    global variable_R
#    chassis_ctrl.stop()
#    chassis_ctrl.rotate_with_time(rm_define.clockwise, 0.5)
#    chassis_ctrl.move(0)

#Main looping function
def start():

    global variable_CelebrationTimer
    global variable_V
    global variable_R
    
    #Enable Joy-Stick
    chassis_ctrl.enable_stick_overlay()
    
    #Enable infared sensor detection
    #ir_distance_sensor_ctrl.enable_measure(1) -- Breaks program
    
    #Play countdown sound
    media_ctrl.play_sound(rm_define.media_sound_count_down,wait_for_complete_flag=True)
    time.sleep(0.5)
    
    #Begin initial startup
    user_defined_initialStartup()

    #Set LEDs to team color
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 36, 103, 255, rm_define.effect_always_on)
    
    #Keep program running with infinite loop
    while True:
        time.sleep(1)

#Detect back armor being hit to start celebration dance function
def armor_hit_detection_bottom_back(msg):

    global variable_CelebrationTimer
    global variable_V
    global variable_R

    #Stop all movement
    chassis_ctrl.stop()
    time.sleep(0.5)
    
    #Play countdown sound
    media_ctrl.play_sound(rm_define.media_sound_count_down,wait_for_complete_flag=True)
    
    #Start Celebration Dance Function
    user_defined_celebrationDance()

#Detect the chassis impacting obstacles -- Doesn't appear to be working
def chassis_impact_detection(msg):
    
    global variable_CelebrationTimer
    global variable_V
    global variable_R
    
    #Play hit sound
    media_ctrl.play_sound(rm_define.media_sound_attacked)
    
    #Set LEDs to blink red
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)
    
    #Reverse for .5 seconds
    chassis_ctrl.move_with_time(180,0.5)
    time.sleep(3)
    
    #Set LEDs to normal
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 36, 103, 255, rm_define.effect_always_on)
    

#Detects when someone uses a V pose    
def vision_recognized_pose_victory(msg):
    
    chassis_ctrl.stop()
    
    led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 0, 127, 70, rm_define.effect_flash)
    
    while not (chassis_ctrl.is_impact()):
        
        chassis_ctrl.move(0)
        
        for count in range(6):
        
            robotic_arm_ctrl.moveto(50, 200, wait_for_complete=True)
            robotic_arm_ctrl.moveto(-50, -200, wait_for_complete=True)
            robotic_arm_ctrl.moveto(200, 50, wait_for_complete=True)
            robotic_arm_ctrl.moveto(-200, -50, wait_for_complete=True)
        
    chassis_ctrl.stop()
    chassis_ctrl.rotate_with_time(rm_define.clockwise, 0.5)
    
    
    