# -*- coding: utf-8 -*-

# pyskel.py
#
# This is a utility for generating python skeleton code based on commonly
# occuring scripting needs (database connections, file handling, etc.)
# This will help save time from having to go to ebooks, google or stack
# overflow everytime you need to recall how something is done in python.
#
# Running the script from the command line, you will be prompted with different
# questions about your scripting requirements. The script will generate a 
# skeleton python file based on those needs. If you have needs for a config
# file loader, a configuration file will also be generated.

import os
from snippets import *

def check_permissions(output_path):
    '''Checks the read permissions of the specified file'''
    path_status = False
    try:
        path_status = os.access(output_path, os.W_OK) # Find the permissions using os.access
    except IOError as e:
        print(os.strerror(e)) # Print the error message from errno as a string
    return path_status

def generate_skeleton(configs):
    # Placeholders for the skeleton imports and code body:
    skel_imports = []
    skel_body = []

    if configs['use_cfg'] == 'y':
        skel_imports.append(config_import)
        skel_body.append(config_body)
        # TODO: Add code to write

    if configs['use_files'] == 'y':
        skel_body.append(file_body)

    if configs['use_pd'] == 'y':
        skel_imports.append(pd_import)
        skel_body.append(pd_body)

    if configs['use_mpl'] == 'y':
        skel_imports.append(mpl_import)
        skel_body.append(mpl_body)

    if configs['use_mysql'] == 'y':
        skel_imports.append(mysql_import)
        skel_body.append(mysql_body)

    if configs['use_mongo'] == 'y':
        skel_imports.append(mongo_import)
        skel_body.append(mongo_body)

    # Convert lists into single strings:
    skel_imports = ''.join(skel_imports)
    skel_body = ''.join(skel_body)
    skel_code = skel_imports + skel_body + function_stub + main_stub
    return skel_code

def main():
    print("pyskel.py - skeleton code generator")
    configs = {}
    path_status = False
    while path_status == False:
        output_path = input("Output path: (Press enter for current directory.): ")
        # Handle output path if cwd:
        if output_path == '':
            output_path = os.getcwd()
        path_status = check_permissions(output_path)
    configs['use_cfg'] = str.lower(input("Use ConfigParser? [y/n]: "))
    configs['use_files'] = str.lower(input("Use file loader/writer? [y/n]: "))
    configs['use_pd'] = str.lower(input("Include pandas and Excel writer? [y/n]: "))
    configs['use_mpl'] = str.lower(input("Use matplotlib? [y/n]: "))
    configs['use_mysql'] = str.lower(input("Use MySQL? [y/n]: "))
    configs['use_mongo'] = str.lower(input("Use MongoDB? [y/n]: "))
    #configs['use_arango'] = str.lower(input("Use ArangoDB? [y/n]: "))
    python_code = generate_skeleton(configs)
    #print(python_code)

    # Save skeleton code and
    # make sure possible to write to path:
    output_file = "skeleton.py"

    try:
        text_file = open(output_path + "/" + output_file, "w")
        text_file.write(python_code)
        text_file.close()
    except Exception as e:
        print("Exception caught:\n", str(e))    

    text_file = open(output_path + "/" + output_file, "w")
    text_file.write(python_code)
    text_file.close()

    # Save config file, if needed:
    if configs['use_cfg'] == 'y':
        config_file = open(output_path + "/" + "app.config", "w")
        config_file.write(config_file_text)
        config_file.close()

    # Save a readme file:
    readme_file = open(output_path + "/" + "readme.MD", "w")
    readme_file.write(readme_text)
    readme_file.close()
    
    print("\nPython skeleton code saved to: %s" % output_path)
    return

if __name__ == "__main__":
    main()