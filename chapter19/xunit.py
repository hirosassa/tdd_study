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
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = True

    def testMethod(self):
        self.wasRun = True        


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
        
    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)
    
if __name__ == "__main__":
    TestCaseTest("testRunning").run()
    TestCaseTest("testSetUp").run()
