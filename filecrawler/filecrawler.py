import os


# Receives an input by the user and starts application.
def start_application(current):
    string = input("Type word to search: ")
    search_for(string=string, current=current)


# This functions gets the current directory, searches for text files and then for strings within these text files.
def search_for(string: str, current):
    directory_contents = os.listdir(current)


    # Loop for searching within the directory, its files and folders.
    for content in directory_contents:
        

        # This defines the absolute path to the file or directory.
        absolute_path = os.path.join(current, content)


        # If the absolute path is a directory, start another search within that directory.
        if os.path.isdir(absolute_path):
            search_for(string=string, current=absolute_path) # Start all over again within the new current directory.
        

        # If the absolute path is a file.
        else:


            # If the absolute path is a text file, search for the string defined in the call.
            if ".txt" in absolute_path:
                try:
                    with open(absolute_path, 'r') as f:
                        for index, line in enumerate(f):


                            # Search string
                            if string in line:
                                print(f'Word was found at path {absolute_path}.')
                            

                                # Stop looking for next lines
                                break
                        else:
                            

                            # This else clause is executed if the for loop completes without a 'break'
                            pass
                

                except FileNotFoundError:
                    print(f"The file {content} could not be found within {absolute_path}.")
                

                except Exception as e:
                    print(f"An error occured at {absolute_path}: {e}")


current_directory = os.path.dirname(os.path.realpath(__file__))

start_application(current=current_directory)
