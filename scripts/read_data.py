#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_srvs.srv import Empty
import time
import csv

# rospy.init_node('scan_result_node')

def callback(msg):
    # print(len(msg.ranges))
    # values at 0 degree
    print('\n' + str(msg.ranges[0]))
    # values at 90 degree
    print('\n' + str(msg.ranges[360]))
    # values at 180 degree
    print('\n' + str(msg.ranges[719]))


def callService(service_name,type_srv):
    rospy.wait_for_service(service_name)
    try:
        call_service = rospy.ServiceProxy(service_name,type_srv)
        call_service()
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    # call_service = rospy.ServiceProxy(service_name,type_srv)
    # call_service()


def main():
    # intialise node
    rospy.init_node('scan_result_node')
    
    # call start motor service
    callService('start_motor',Empty)
    
    # sleep for 5 seconds
    time.sleep(5)

    #loop with rate r Hz
    count = 0
    r = rospy.Rate(20)
    while not rospy.is_shutdown() :
        if count  < 50:
            sub = rospy.Subscriber('/scan', LaserScan, callback)
            # rospy.spin()
            count = count + 1
        else:
            callService('stop_motor',Empty)
            break

        r.sleep()


if __name__ == "__main__":
    main()




