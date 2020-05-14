# pathlib was introduced in python 3.4 to replace the old os.path
import shelve
from pathlib import Path
import os


print("-------------------- BUILD A PATH --------------------")
# mac uses /, while windows uses \ for paths. If you want your program to work on both, you'll have to use the above pathlib library
# its safer this way. if you directly type any / or \, then you risk your script not working on a different platform
# any of below works, as long as one of first 2 objects is a Path object
p = Path('/Users/ilja/Dropbox/ATBS/')
p = Path('/Users') / Path('ilja/Dropbox/ATBS')
p = Path('/Users') / Path('ilja') / 'Dropbox/ATBS'
print(p)
# OS VERSION: os.path.join()

# path can tell you if the provided path is absolute or not
cwd = Path.cwd()
print(cwd.is_absolute())
print(Path('spam/bacon/eggs').is_absolute())

# we can use the above to get an absolute path from a relative path
rel_path = Path('../Corey')
print(Path.cwd()/rel_path)


print("-------------------- LIST DIR, CONTENTS --------------------")
# get cwd
print(Path.cwd())
# OS VERSION: os.getcwd

# get an environmental variable
h = os.environ.get('HOME')
print(h)

# change dir - HAVE TO USE OS
os.chdir('dir1')
print(Path.cwd())
os.chdir('..')
print(Path.cwd())

# get home dir
print(Path.home())

# get filesize
print(os.path.getsize(p))

# see contents - simple
print(os.listdir())  # lists cwd
print(os.listdir('/'))  # lists in root

# see content - REGEX
r = list(p.glob('*'))  # only works with /, does not work with ~
# can create complex expressions
r = list(p.glob('*.py'))
# although the syntax is different eg ? is used to indicate any single character
r = list(p.glob('?_practice.py'))
print(r)


print("-------------------- MAKE, RENAME, DELETE --------------------")
# create dirs - HAVE TO USE OS
# os.mkdir('dir2/mkdir_folder')  # only creates top level
# os.makedirs('dir2/dir3/dir4/makedirs_folder')  # creates all the intermediate ones

# create files -
# new_file = p/'file.txt'
# new_file.touch()

# rename
# os.rename('dir2/dir2_file.txt', 'dir2/new_renamed_file.txt')

# delete dirs
# os.rmdir()
# os.removedirs()

# delete files
# os.remove('file.txt')


print("-------------------- TRAVERSE A TREE --------------------")
# HAVE TO USE OS
# for dirpath, dirnames, filenames in os.walk('/Users/ilja/Dropbox/Corey/'):
#     print(f'current path is {dirpath}')
#     print(f'folders inside are {dirnames}')
#     print(f'files inside are {filenames}')
#     print('')


print("-------------------- DISECT A PATH --------------------")
p = Path('di1/di2/di3/file.txt')
print(p.anchor)  # the little slash upfront
print(p.parent)  # evaluates to another path object
print(p.name)  # folder
print(p.stem)  # file without extention
print(p.suffix)  # extention
print(p.drive)  # only works on windows C://
# OS VERSIONS: os.dirname, os.basename, os.split, os.splitext


print("-------------------- CHECK VALIDITY --------------------")
print(p.exists())  # checks if path real
print(p.is_file())
print(p.is_dir())
# OS VERSIONS: os.path.exist(), os.path.isfile(), os.path.isdir()


print("-------------------- SHELVE --------------------")
# shelve module can be used to save variables to a binary file
# NOTE: plaintext files are useful when you're planning to read them yourself - but for any content accessed by your program you should use shelve
# shelfFile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats  # shelve files behave like dictionaries
# shelfFile.close()

with shelve.open('mydata') as f:
    cats = ['Zophie', 'Pooka', 'Simon']
    f['cats'] = cats  # shelve files behave like dictionaries
    print(f['cats'])  # can read and write at the same time!

# because shelve behaves like a dict, it has .keys() and .values() methods
# NOTE: we do need to convert them to List object types though
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
