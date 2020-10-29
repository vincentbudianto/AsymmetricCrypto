import json

def readFile(path):
    """
    Reads file as an array.

    Keyword Arguments:
    path -- Path to file.
    """
    with open(path, "rb") as f:
        arr = bytearray(f.read())
        A = list(arr)
        return (A)

def writeFile(path, arr):
    """
    Writes array to file.

    Keyword Arguments:
    path -- Path to file.
    arr -- the array, each value must be >= 0 and < 256.
    """
    with open(path, "wb") as f:
        A = bytearray(arr)
        f.write(A)

def readFromJson(path):
    """
    Reads from json file.
    """
    with open(path, "r") as f:
        data = json.load(f)
        return data