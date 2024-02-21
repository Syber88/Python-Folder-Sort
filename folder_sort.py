import os
import sys
import shutil #allows us to delete a directory that is not empty
from pprint import pprint

def get_username():
    """Get the username of the current user.
    This function retrieves the username of the current user by extracting it
    from the current working directory path.
    Returns:
        str: The username of the current user.
    Raises:
        Exception: If the current working directory is not within the
        home directory.
    """
    
    pwd = os.getcwd() 
    dir_split = pwd.split("/")
    home = dir_split.index("home")
    try:  
        return dir_split[home+1]
    except:
        print("currently in the home directory")


def get_target_path(profile):
    """Get the target path for a user's Downloads folder.
    Args:
        profile (str): The username or profile name of the user.
    Returns:
        str: The target path for the user's Downloads folder, formatted as
        "/home/{profile}/Downloads".
    """
    return f"/home/{profile}/Downloads"


def change_directory(directory):
    """Change the current working directory to the specified directory.
    Args:
        directory (str): The path of the directory to change to.
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If the user does not have permission to access 
        the specified directory.
    """
    os.chdir(directory)


def modified_ext_directory2(extension)-> str:
    """Determine the category of a file based on its extension.
    Args:
        extension (str): The file extension to categorize.
    Returns:
        str: The category of the file based on its extension.
    """
    
    categories = {
    "videos" : ["mp4","mkv"],
    "images" : ["jpeg","jpg","png","gif"],
    "docs"   : ["pdf","txt","doc", "docx", "odt","rtf","wpd"," wps"] ,  
    "compression" : ["zip","rar","7s","gz","tar"],
    "executables" : ["app", "bat", "bin", "cmd", "com", "exe", "vbs", "x86"],
    "programming files":  ["c", "cpp", "cs", "java", "js", "json", "py",\
                           "sql", "swift", "vb"]
    }

    for category, extension_raw in categories.items():
        if extension in extension_raw:
            return category
    

def modified_ext_directory1(extensions_list)-> set:
    """Determine the categories of multiple file extensions.
    Args:
        extensions_list (list): A list of file extensions to categorize.
    Returns:
        set: A set containing the categories of the file extensions.
    Raises:
        KeyError: If any extension in the list is not found in any category.
    """
    
    ext_modded = set
    for extension in extensions_list:
        extension_extract = modified_ext_directory2(extension)
        ext_modded.add(extension_extract)
    return ext_modded


def create_directory(extensions):
    """Create directories for each extension if they don't already exist.
    Args:
        extensions (list): A list of directory names to create.
    Raises:
        FileExistsError: If a directory with the same name already exists.
    """
    
    for extension_dir in extensions:
        if os.path.exists(extension_dir):
            print(f"Direcory {extension_dir} already exists" )
            return
        else:
            os.mkdir(f"{extension_dir}")
            print("i shoulda be making a directory", extension_dir)


def files_id() -> list[str]:
    """function to identify all the files in a directory
    return: list of all the available files in the directoroy"""
    dir_list = os.listdir()
    return [file for file in dir_list if os.path.isfile(file)]


def extension_id(file_list) -> list[str]:
    """Extract the file extensions from a list of filenames.
    Args:
        file_list (list): A list of filenames.
    Returns:
        list[str]: A list containing the file extensions extracted
        from the filenames.
    """
    return [os.path.splitext(file)[1][1:] for file in file_list]


def location(profile, files):
    for file in files:
        ext = os.path.splitext(file)[1][1:]
        ext_hai = modified_ext_directory2(ext)
        source = f"/home/{profile}/Downloads/{file}"
        destination = f"/home/{profile}/Downloads/{ext_hai}/{file}"
        return source, destination
    

# def 
        
    
#create a function for renaming existing files
#create a function for source and destination
#how will we get the new extension directory
def move_files(profile):
    os.chdir(f"/home/{profile}/Downloads")
    files = files_id()
    source_dir = f"/home/{profile}/Downloads/"
    # source, destination = location(profile, files)
    for file in files:
        ext = os.path.splitext(file)[1][1:]
        ext_hai = modified_ext_directory2(ext)
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(source_dir, ext_hai, file)
        
        try:
            os.makedirs(os.path.join(source_dir,ext_hai), exist_ok=True)
            shutil.move(source_path, destination_path)
            print(f"Moved {file} to {destination_path}")
        except Exception as e:
            print(f"Error moving '{file}': {e}")
    # dotfind = file.rfind(".")
    # if os.path.exists(destination):
    #     rename = file[:dotfind] + "_new"
    #     shutil.move(source_path, f"/home/{profile}/Downloads/{ext_hai}/{rename}")
    # else:
    #     shutil.move(source, destination)

# move_files(profile=get_username())

            # print(i)
        
        #use rfind to find the last occurence of something 
        
        
        
# print(os.getcwd())
# dirlist = 
# os.mkdir("awepls")
# os.rename("awepls","anotherone") 
# os.remove("test.txt") 
# try:
#     os.rmdir("awe")
# except:
#     print("the directory is not empty")
    
# shutil.rmtree("awe")
# pprint(dir(os))

# pprint(check)