# Extra Features By de/odex
# Diff File By intrnl
# Also Thanks To Modder
import logging
import os
import sys
import urllib.request

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    if "--theme" in sys.argv:
        theme = sys.argv[sys.argv.index("--theme") + 1].replace("\\", "/")
    else:
        raise Exception("No theme file!")

    if "--diff" in sys.argv:
        diff = sys.argv[sys.argv.index("--diff") + 1].replace("\\", "/")
    elif os.path.exists(".\diff.txt"):
        diff = "diff.txt"
    else:
        logging.info("Retrieving")
        r = urllib.request.urlretrieve("https://cdn.rawgit.com/intrnl/b758b9d9ed5c05e6377b27d647b11d91/raw"
                                       "/25a03b4a45a81565e29e1de04343990f796fb4db/discord-diff_20180501.txt", "diff.txt")
        diff = "diff.txt"

    data = []
    classes = [[], []]

    with open(diff) as fileObject:
        for i, line in enumerate(fileObject):
            if "||" in line:
                classes[0].append(line.split("||")[0].strip())
                classes[1].append(line.split("||")[1].strip())

    with open(theme, 'r') as fileObject2:
        logging.info("Reading")
        for line in fileObject2:
            for x, _ in enumerate(classes[0]):
                if classes[0][x] in line:
                    line = line.replace(classes[0][x], classes[1][x])
            data.append(line)

    with open(theme, 'w') as file:
        logging.info("Writing")
        file.writelines(data)
