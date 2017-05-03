Feature: Implementing wxWidget

	Scenario: Successful Implementation of wxWidget
		Given Curses Menu is installed
		When User makes a menu item launching a wxWidget app
		And User exits the wxWidget app
		Then Curses Menu should not exit