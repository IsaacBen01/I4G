def read_file_content (filename):
    with open("story.txt", "r") as openfile:
        readfile = openfile.read()
        return readfile

def countwords ():
    text = read_file_content("story.txt")
    splitwords = text.split()
    #print(splitwords)

    count = {}
    for i in splitwords:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
