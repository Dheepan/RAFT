import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_My_Companion_Tab(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_My_Companion_Tab tests..")

#Feature testcases

    def test_t001_MyCompanion_Tab_Intro(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_MyCompanion_Tab_Intro.png")
            raise


    def test_t002_MyCompanion_Tab_InviteFriends_Button(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_MyCompanion_Tab_InviteFriends_Button.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_My_Companion_Tab class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
