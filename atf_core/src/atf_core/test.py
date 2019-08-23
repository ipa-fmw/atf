#!/usr/bin/env python

from atf_msgs.msg import TestResult

class Test:
    def __init__(self):
        self.package_name = None
        self.name = None
        self.testsuite = None
        self.testsuite_name = None
        self.test_config = None
        self.test_config_name = None
        self.robot_config = None
        self.robot_name = None
        self.robot_env_config = None
        self.robot_env_name = None
        self.generation_config = None

        # testblocks with metrics
        metrics_handle = None
        self.testblocks = []
    
    def get_result(self):
        test_result = TestResult()
        test_result.name = self.name
        test_result.groundtruth_result = None
        for testblock in self.testblocks:
            # get result
            testblock_result = testblock.get_result()

            # append result
            test_result.results.append(testblock_result)

            # aggregate result
            if testblock_result.groundtruth_result != None and not testblock_result.groundtruth_result:
                test_result.groundtruth_result = False
                test_result.groundtruth_error_message += "\n   - testblock '%s': %s"%(testblock_result.name, testblock_result.groundtruth_error_message)
                #print test_result.groundtruth_error_message

        if len(test_result.results) == 0:
            raise ATFAnalyserError("Analysing failed, no test result available for test '%s'."%test_result.name)

        #print "\ntest_result:\n", test_result
        return test_result
