import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Invite_Friends_Popup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Invite_friends_popup tests..")

#Feature testcases

    def test_t001_Invite_Friends_Popup(self):
        h=self._h
        try:
            h.click("#invite_friends_menu")
            state=h.is_displayed("#invite-popup")
            self.assertTrue(state)
        except:
            h.screenshot("test_t041_Invite_friends_Popup.png")
            raise


    def t002_Invite_Friends_Popup_Select(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t042_Invite_friends_Popup_Select.png")
            raise


    def test_t003_Invite_Friends_Popup_Close(self):
        h=self._h
        try:
            h.click("#invite_friends_menu")
	    h.click(".ui-dialog-titlebar-close")	
	    state = h.is_displayed("#invite-popup")
	    self.assertFalse(state)
        except:
            h.screenshot("test_t043_Invite_friends_Popup_Close.png")
            raise


    def test_t004_Invite_Friends_Popup_UncleTom(self):
        h=self._h
        try:
	    h.click("#invite_friends_menu")
	    text = h.execute_script("return $('#invite-popup').find('.board').html()")
	    if text == "Add your friends as companions, and unlock unexplored islands.":	
		state = "True"
	    else:    
    		state  = "False"
	    self.assertTrue(state)
	    h.click(".ui-dialog-titlebar-close")    
        except:
            h.screenshot("test_t044_Invite_friends_Popup_UncleTom.png")
            raise
    
    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Add_Gold_Popup class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
