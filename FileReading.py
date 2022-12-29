with open("Hello.txt") as line_doc:
    first_line = line_doc.readline()
    second_line = line_doc.readline()
    print(second_line)