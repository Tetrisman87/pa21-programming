variable_X = 0
variable_Y = 0
variable_Z = 0
variable_V = 0
variable_R = 0

def start():
  global variable_X
  global variable_Y
  global variable_Z
  global variable_V
  global variable_R
  tools.timer_ctrl(rmdefine.timer_start)
  x = 0
  
  while True:
    time.sleep(1)
    x += 1
    
  
  while x <= 30:
    variable_V = 130
    variable_R = 2
    chassis_ctrl.set_wheel_speed(variable_V - variable_V / variable_R,variable_V + variable_V / variable_R,variable_V - variable_V / variable_R,variable_V + variable_V / variable_R)
    time.sleep(0.5)
        
  led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 255, 0, 0, rm_define.effect_always_on)  
 
