#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()

        
class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)        
        
    def testMethod(self):
        self.wasRun = True

if __name__ == "__main__":
    test = WasRun("testMethod")
    print(test.wasRun)
    test.run()
    print(test.wasRun)

