import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Pending_Requests_Panel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Pending_Requests_Panel tests..")

#Feature testcases

    def test_t001_Pending_Requests(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_Pending_Requests.png")
            raise


    def test_t002_Pending_Requests_User(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_Pending_Requests_User.png")
            raise


    def test_t003_Pending_Requests_Cancel_Request(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t003_Pending_Requests_Cancel_Request.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Pending_Requests_Panel class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
