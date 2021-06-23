import filecmp
import os

def list_files(directory):
    file_list = set([])
    for path, subdirs, files in os.walk(directory):
        for name in files:
            file_list.add(os.path.join(path.replace(directory,""), name))
    return file_list
    
def compare(path1,path2):
    source = list_files(path1)
    destination = list_files(path2)
    missed_files = list(source - destination)
    new_files = list(destination - source)
    identical_files, changed_files = [],[]

    for item in (source & destination):
        result = filecmp.cmp(path1 +"\\"+ item, path2 + "\\"+ item, shallow=False)
        if result:
            identical_files.append(item)
        else:
            changed_files.append(item)
    
    # print('Missed Files - {}'.format(missed_files))
    # print('New Files - {}'.format(new_files))
    # print('Identical Files - {}'.format(identical_files))
    # print('Changed Files - {}'.format(changed_files))

    report = {}
    report['Missed Files'] = missed_files
    report['New Files'] = new_files
    report['Identical Files'] = identical_files
    report['Changed Files'] = changed_files

    return report

# path1 = r"folder path 1"
# path2 = r"folder path 2"

# print(compare(path1,path2))
