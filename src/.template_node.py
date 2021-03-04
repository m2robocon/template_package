#!/usr/bin/env python3

import rospy

# from template_package.msg import Message
# from template_package.srv import Service


class TemplateNode:
    def __init__(self):
        rospy.init_node("template_node")

        # topic = rospy.get_param("~topic", "/template_package_pub")
        # self.pub = rospy.Publisher(topic, Message, queue_size=1)

        rospy.spin()


if __name__ == "__main__":
    TemplateNode()
