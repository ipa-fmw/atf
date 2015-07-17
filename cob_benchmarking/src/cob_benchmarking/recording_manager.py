#!/usr/bin/env python
import rospy

from cob_benchmarking.srv import *
from atf_msgs.msg import *


class RecordingManager:
    def __init__(self, name):

        self.name = name
        self.topic = "/testing/"
        rospy.wait_for_service(self.topic + "recorder_command")
        self.recorder_command = rospy.ServiceProxy(self.topic + "recorder_command", RecorderCommand)

    def start(self):

        rospy.loginfo("Section '" + self.name + "': Start")

        result = self.recorder_command(self.name, Trigger(Trigger.ACTIVATE))
        self.recorder_command.wait_for_service()
        if not result:
            rospy.logerr("Recorder not ready!")

    def stop(self):

        rospy.loginfo("Section '" + self.name + "': Stop")

        result = self.recorder_command(self.name, Trigger(Trigger.FINISH))
        self.recorder_command.wait_for_service()
        if not result:
            rospy.logerr("Recorder not ready!")
