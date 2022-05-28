def read_file_content(story):
    text = open("story.txt", "r")
    print ("Hello World")
     

def count_words():
    text = read_file_content("./story.txt" "r")

    d = dict()

    for line in text:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for words in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                    d[word] = 1

                    for key in list(d.keys()):
                        print(key, ":", d[key])
