#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 #importa mensajes de ROS tipo String y Int32
from sensor_msgs.msg import Joy # impor mensaje tipo Joy
from geometry_msgs.msg import Twist, Point # importar mensajes de ROS tipo geometry / Twist
from duckietown_msgs.msg import Twist2DStamped 
import message_filters

class Template(object):
    def __init__(self, args):
        super(Template, self).__init__()
        self.args = args
        #sucribir a joy 
        self.joy = message_filters.Subscriber("/duckiebot/joy" , Joy)
	self.dist = self.Sub_dist = message_filters.Subscriber("duckiebot/distancia", Point)
        #publicar la intrucciones del control en possible_cmd
        self.publi = rospy.Publisher("/duckiebot/wheels_driver_node/car_cmd", Twist2DStamped, queue_size = 8)
        self.twist = Twist2DStamped()
	ts = message_filters.TimeSynchronizer([self.joy, self.dist], 10)
	ts.registerCallback(self.callback)


    #def publicar(self, msg):
        #self.publi.publish(msg)

    def callback(self,msg_joy,msg_dist):
        rt = msg_joy.axes[5]
        lt = msg_joy.axes[2]
        l = msg_joy.axes[0]
        
        x = msg_joy.buttons[2]
	print(msg_joy)

#        print(y, x, z)
#        self.twist.omega = 
#        self.twist.v = 

#        if rt in range(-1,1):
#           self.twist.omega =
#            self.twist.v = -rt + 1
            
#        if lt in range(-1,1):
#            self.twist.v = lt - 1

        if msg_dist.z < 5:
	     rt  = 0



	self.twist.v = -lt + rt
	    
	
	if abs(l) >= 0.8:
	    self.twist.omega = - 10 * l 
	    
	
	if x == 1:
	    self.twist.omega = 0
	    self.twist.v = 0    
	    
        self.publi.publish(self.twist)
        




def main():
    rospy.init_node('test') #creacion y registro del nodo!

    obj = Template('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

    #objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

    rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
    main()
