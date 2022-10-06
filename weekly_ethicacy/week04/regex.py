import re


def find_name(line):
    pattern ="[a-l]|\ADr.[^e]|\Mr."
    result = re.findall(pattern,line)

    return result


f = open("names.txt")
for line in f.readlines():
    print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)


# other patterns
# FirstName and LastName
  # pattern = r"(\w+) (\w+)[^\.]"

# FirstName MiddleName LastName
  # pattern=r'(\w+) (\w+) (\w+)'

# FirstName M. LastName
  # pattern=r'(\w+) (\w+\.) (\w+)'
  # result = result + re.findall(pattern,line)