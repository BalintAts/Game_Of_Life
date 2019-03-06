def make_content_from_file(filename):
    file = open(filename,"r")
    content = [line.rstrip('\n') for line in file]
    return content


