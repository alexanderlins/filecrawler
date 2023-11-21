import os

# This function gets the current directory, searches for text files and then for strings within these text files.
def start_application(current):
    string = input("Skriv sökordet: ")
    print(f"Sök ordet är {string}. Nu börjar vi")
    press_to_continue = input("Tryck på valfri knapp för att fortsätta.")

    search_for(string=string, current=current)

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
                                print(f'Ordet hittades i filen som ligger i {absolute_path}.')
                                # Stop looking for next lines
                                break
                        else:
                            # This else clause is executed if the for loop completes without a 'break'
                            pass
                except FileNotFoundError:
                    print(f"Filen {content} kunde inte hittas.")
                except Exception as e:
                    print(f"Ett fel hände: {e}")


current_directory = os.path.dirname(os.path.realpath(__file__))

start_application(current=current_directory)

# search_for("Koffein", current_directory)