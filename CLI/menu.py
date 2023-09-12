
class Menu():
    """A class for common functions the CLI will use across different menus.
    
    This class provides utility methods for obtaining and validating user input
    when navigating through diffrent menu options in CLI.
    """
    def get_user_input(message: str,valid_input: set) -> str:
        """Gets user input and validates input

        Args:
            message (str): Message to be displayed to the user.
            valid_input (set): A set of valid inputs the user can enter on the terminal.
        """
        user_input = input(message+"\n")
        
        #Incorrect user input 
        while user_input not in valid_input:
            print("Wrong input valid inputs are")
            for val_input in valid_input:
                print(val_input)
            user_input = input(message)

        return user_input
        
