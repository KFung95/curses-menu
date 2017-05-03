Feature: Change text color

	Scenario: Successful Change in Text Color
		Given Curses Menu is installed
		When User makes a menu item with the parameter <color>
		Then the menu's color field should be <color pair number>
		
		Examples:
		|   color  |  color pair number  |
		| "RED"    | 2                   |
		| "GREEN"  | 3                   |
		| "YELLOW" | 4                   |
		| "BLUE"   | 5                   |
		| "MAGENTA"| 6                   |
		| "CYAN"   | 7                   |
		| "WHITE"  | 8                   |

	Scenario: Unsuccessful Change in Text Color
		Given Curses Menu is installed
		When User makes a menu item with an incorrect color parameter
		Then the menu's color field should be 8

		