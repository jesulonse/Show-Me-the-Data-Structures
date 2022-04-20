import os
def find_files(suffix, path):

    if suffix == "":

        return []

    new_directory = []

    if os.path.isdir(path):

        for sub_dir in os.listdir(path):

            new_path = find_files(suffix, path + "/" + sub_dir)

            new_directory = new_directory + new_path

    else:

        if path.endswith(suffix):
            
                return [path]

    return new_directory

pathy = os.getcwd()
print(find_files(".c", pathy))