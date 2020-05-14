'''
Imports
'''
from src.include.includes import *


def printDict(xdict: dict):
    '''
    Prints the dictionary 'xdict'.
    '''
    if not xdict:
        return
    for k, v in xdict.items():
        print(str(k) + "\t" + str(v));
    return


def clear(astring: str):
    '''
    Trims the string 'astr'.
    '''
    astring = astring.strip()

    astring.replace("\n", "");
    astring.replace("\t", "");
    astring.replace("\r", "");
    return


def printList(alist: list):
    '''
    Print list 'alist'.
    '''
    if not alist:
        return
    for item in alist:
        print(item)
    return


def toDict(alist: list):
    '''
    Convert list 'alist' to dictionary.
    '''
    xdict = {}
    for i in range(0, len(alist)):
        s = str(i)
        xdict[s] = alist[i]
    return xdict


def randomString(size=10):
    '''
    Returns a random string of length 'size'.
    '''
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(size))


def hasDuplicates(alist: list):
    '''
    Checks whether the list 'alist' has any duplicates.
    '''
    for i in range(0, len(alist)):
        for j in range(0, len(alist)):
            if i != j:
                if alist[i] == alist[j]:
                    return True
    return False


def isSublistOf(alist: list, blist: list):
    '''
    Checks whether 'alist' is a sublist of 'blist'.
    '''
    for item in alist:
        if item not in blist:
            return False
    return True


def intersection(a: list, b: list):
    '''
    Returns the intersection of the lists 'a' and 'b'.
    '''
    return set.intersection(set(a), set(b))


def difference(a: list, b: list):
    '''
    Returns the difference of the lists 'a' and 'b'.
    '''
    s = set(b)
    return [x for x in a if x not in s]


def parseTags(astr: str):
    '''
    Returns a tag list from the tag string 'astr'.
    '''
    return astr.rstrip().split(SEMIC_SPLIT)


def parseAlignment(astr: str):
    '''
    Returns an alignment list from the alignment string 'astr'.
    '''
    return astr.rstrip().split(MINUS_SPLIT)


def parseFeatures(astr: str):
    '''
    Returns a feature list from the feature string 'astr'.
    '''
    return astr.rstrip().split(SPACE_SPLIT)


def parseMarkers(arg: str):
    '''
    Returns a markers list from the markers string 'astr'.
    '''
    return arg.rstrip().split(MINUS_SPLIT)


def getFileWithoutExtension(file: str):
    '''
    Removes the extension from the file 'file'.
    e.g. path/to/test.txt --> path/to/test
    '''
    name, _ = os.path.splitext(file)
    return name


def getFileExtension(file: str):
    '''
    Returns the extension from the file 'file'.
    e.g. path/to/test.txt --> .txt
    '''
    _, ext = os.path.splitext(file)
    if ext:
        return ext
    return ""


def getNameFromFile(file: str):
    '''
    Returns the name of the file 'file'.
    e.g. path/to/test.txt --> test
    '''
    name = os.path.basename(file)
    fullname = getFileWithoutExtension(name)
    return fullname


def getPathFromFile(file: str):
    '''
    Returns the path to the file 'file'.
    e.g. path/to/test.txt --> path/to/
    '''
    return os.path.dirname(file) + "/"


def renameDataFile(file: str):
    '''
    Renames the file using the pattern:
    e.g. path/to/file.xxx --> path/to/file/project.txt
    '''
    fnx = getFileWithoutExtension(file)
    pro = "/project" + PRO_EXT
    return fnx + pro


def renameConfigFile(file: str):
    '''
    TODO: Documentation
    '''
    return file


def getProjectFolder():
    '''
    Returns the path to the project folder.
    '''
    return HOME_DIR + PRO_FOLDER


def writeFile(file: str, out: str):
    '''
    Writes the string 'out' to 'file'.
    If 'file' does not exist, it will be created.
    '''
    path = ""
    if file:
        path = getPathFromFile(file)
        if not os.path.exists(path):
            os.mkdir(path)
        fout = open(file, "w")
        if fout:
            fout.write(out)
            fout.close()
        else:
            print("Failed opening file: %s", file)
    return path


def readFile(file: str):
    '''
    Returns the content of the file 'file'.
    '''
    if file:
        fp = open(file, "r", encoding='utf8')
        if fp:
            fc = fp.read()
            if fc:
                return fc
            else:
                print("File could not be read!")
            fp.close()
        else:
            print("File could not be opened!")
    else:
        print("File does not exist!")
    return None


def readFileAsList(file: str, maxvalue=1000000):
    '''
    Returns a list representation of the file 'file'.
    Reads at most 'maxvalue' lines.
    '''
    ctr = 0
    parts = []
    if file:
        fp = open(file, 'r', encoding='utf8')
        if fp:
            for line in fp.readlines():
                if ctr == maxvalue:
                    break
                part = line.rstrip().split("\t")
                parts.append(part)
        fp.close()
        return parts
    return None


def showMessage(message: str, details=""):
    '''
    Open a message box with message 'message' and details 'details'.
    '''
    mb = QMessageBox()
    mb.setText(message)
    mb.setDetailedText(details)
    return mb.exec_()


def initNumList(number: int, count: int):
    '''
    Returns a list of size 'count' initialised with number 'number'.
    '''
    xlist = []
    for i in range(count):
        xlist.append(number)
    return xlist
