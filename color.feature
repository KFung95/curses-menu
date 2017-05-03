Feature: Change text color

	Scenario: Successful Change in Text Color
		Given Curses Menu is installed
		When User makes a menu item with the parameter <color>
		Then the text color should have changed to <color>
		
		Examples:
		|   color  |
		| "RED"    |
		| "GREEN"  |
		| "YELLOW" |
		| "BLUE"   |
		| "MAGENTA"|
		| "CYAN"   |
		| "WHITE"  |

	Scenario: Unsuccessful Change in Text Color
		Given Curses Menu is installed
		When User makes a menu item with an incorrect color parameter
		Then the text color should have changed to "WHITE"

		