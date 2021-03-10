#The purpose of this code is to publish the country name to print_out from country capital

#Import necessary arguments
import rospy 
from std_msgs.msg import String

#this function returns the capital based on the country
def country_capital(country):
    if country == 'France' or country == 'france':
        return 'Paris'
    elif country == 'Japan' or country == 'japan':
        return 'Tokyo'
    elif country == 'Malaysia' or country == 'malaysia':
        return 'Kuala Lumpur'
    elif country == 'Indonesia' or country == 'indonesia':
        return 'Jakarta'
    else:
        return 'invlaid input'

#this function takes the country name as input and outputs the capital
def call_capital():
    rospy.init_node('message')
    pub = rospy.Publisher('print_out', String, queue_size=10)
    #get the keyboard input for the countries
    while not rospy.is_shutdown():
        print 'Input a country please: '
        country = raw_input()
        #send country input to recieve the capital
        capital = country_capital(country)
        #publish capital
        pub.publish(capital)

if __name__ == '__main__':
    call_capital()
