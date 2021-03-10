#the purpose of this code is to read input from the subscriber

#import necessary arguments
import rospy
from std_msgs.msg import String #this is for the publisher/subscriber

#This prints out the information
def reference(message):
    print(message) 

#This sends the argument
def print_out():
    rospy.init_node('message', anonymous=True) #anonoymous True makes sure that same names can be run at the same timeme
    rospy.Subscriber('print_out', String, reference)
    rospy.spin() #do not exit the node

if __name__ == '__main__':
    print_out()
    
