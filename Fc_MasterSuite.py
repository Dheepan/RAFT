import unittest
from unittest import TestSuite,defaultTestLoader,TextTestRunner
import xmlrunner
import StringIO
from Singleton import HashCubeAutomation
from string import maketrans



if __name__=='__main__':

# create a test suite
    suite=TestSuite()
    

    runner=xmlrunner.XMLTestRunner(output='reports')
    runner.run(suite)

## cleaning up the Webdriver Object
    h=HashCubeAutomation("cleaningUp..")
    h.cleanUp()