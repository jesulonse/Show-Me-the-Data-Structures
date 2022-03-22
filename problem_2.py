import os
def find_files(suffix, path):
    new_directory = []
    if suffix == '':# or not '.c':
        return []
    if len(os.listdir(path)) == 0:
        return []
    if os.path.isfile(path):
        if path.endswith(suffix):
            return path
    else:
        new_path = os.listdir(path)
        for every_item in new_path:
            new_directory.extend(find_files(suffix, "{0}\{1}".format(path,every_item)))
            return new_directory



pathy = os.getcwd()
print(pathy)
folder_name = 'testdir'
print(find_files(".c", pathy))
            

