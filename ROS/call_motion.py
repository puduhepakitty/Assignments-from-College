#The purpose of this code is to read a json file and convert it's format

#import necessary arguments
import rospy
from std_msgs.msg import String
import json
import yaml

#/home/pi/Desktop/plen_ros/laughing.json
#read the json file
def Json_message(data):
    #convert the json file
    i = 0
    with open(data) as j:
        json_data = json.load(j)
        json_final = {}
        final = []
        t_t_m = {}
        #Create for loops to read at every instance 
        for k in json_data['frames']:
            final.append('{')
            for n in k['outputs']:
                json_final = str(n['device']) + ':' + str(n['value'])
                final.append(json_final)
                i += float(1)
                if (i/4)%1 ==0:
                    t_t_m = str('transition_time_ms')+ ':'+ str(k['transition_time_ms']) +'}'
                    final.append(t_t_m)
    
        return final
        
#send the json file to publisher
def json_input():
    rospy.init_node('message', anonymous=True)
    pub = rospy.Publisher('print_out', String, queue_size=10)
    while not rospy.is_shutdown():
        #get the path input
        print ('Input path: ')
        json_type  = raw_input()
        json_path = Json_message(json_type)
        #publish this json file
        pub.publish(str(json_path))

if __name__ == '__main__':
    json_input()
