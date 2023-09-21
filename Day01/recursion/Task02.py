import os
def list_files_and_dir(dir):
    #get the list of files and dir in the dir in argument
    try: 
        elements = os.listdir(dir)
    #we check for permission error
    except PermissionError:
        print(f"Permision denied : {dir}")
        return
    # for each element in our list elements
    for element in elements:
        # we stock in a var the path of each element by adding the name of the element at the end of the dir path
        path_element = os.path.join(dir, element)
        # we specify if the elemnt is a loink, a dir or a file
        try:
            if os.path.isLink(path_element):
                print(f"Link : {path_element}")
            elif os.path.isdir(path_element):
                print(f"Dir : {path_element}")
            else:
                print(f"File : {path_element}")
        #we check of exceptions
        except Exception as e:
            print(f"Error trying to access {path_element} : {e}")

# we define a principal function in which we define the current directory where the code is executed using "."
def principal():
    current_dir = "."
    list_files_and_dir(current_dir)

if __name__ == "__main__":
    principal()



