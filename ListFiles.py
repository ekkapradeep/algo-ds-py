import os

def list_files(startpath):
    total_files = 0
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level) + '* '
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1) + '* '
        for f in files:
            print('{}{}'.format(subindent, f))
            total_files += 1
    print('')
    print(f'Total Problem Solved: {total_files}')

list_files("./src")