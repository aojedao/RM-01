import rospy
from geometry_msgs.msg import Point
from std_msgs.msg import String
import numpy as np

def Init():

    global pub

    # Define Publisher
    pub = rospy.Publisher()

    # Subscribe to detectObject
    rospy.Subscriber()

    # Subscribe to Lidar information
    rospy.Subscriber()

    # Initialize node
    rospy.init_node('object_range', anonymous=True)

if __name__ == '__main__':
    try:
        Init()
    except rospy.ROSInterruptException:
        pass

rate = rospy.Rate(50)

while not rospy.is_shutdown():