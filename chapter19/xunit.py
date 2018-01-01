#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

        
class WasRun(TestCase):
    def testMethod(self):
        self.wasRun = True

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = True
        


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasRun)

    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)
    
if __name__ == "__main__":
    TestCaseTest("testRunning").run()
    TestCaseTest("testSetUp").run()
