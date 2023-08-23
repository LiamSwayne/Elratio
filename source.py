# DO NOT use triple single quote, triple double quote or the python newline character

def extractLeadingSpaces(inputString):
    leadingSpaces = ""
    for char in inputString:
        if char.isspace():
            leadingSpaces += char
        else:
            break
    return leadingSpaces

# Read the source code of this program
with open(__file__, 'r') as file:
    sourceCode = file.read()

# Find the index of the first occurrence of three quotes
splitIndex = sourceCode.find("\'\'\'")

# Define newline character so it isn't modified during compiler build
newLine = chr(10)

# Split the source code at the first occurrence of three quotes
if splitIndex == -1:
    print("Elratio program missing \'\'\'. This is a shameful mistake. The compiler will remember this.")
else:
    # Extract Elratio program
    program = sourceCode[splitIndex + 3:]
    program = program[:program.index("\'\'\'")]
    lines = program.split(newLine)

    for i in range(len(lines)):
        # remove indentation and get line
        line = lines[i]
        spaces = extractLeadingSpaces(line)
        line = line.lstrip()

        # compile print statement syntax
        if line[:15] == "systemOutPrint(":
            line = "p" + line[10:]
        elif line[:6] == "print(":
            print("I am a compiler of principle. I do not accept print(). Use systemOutPrint() instead.")

        # reinsert back indentation and line
        lines[i] = spaces + line

    # Execute Elratio program
    program = newLine.join(lines)
    exec(program)

# Elratio program (test case)
'''
# test 1
systemOutPrint("a"*10)

# test 2
if True:
    systemOutPrint(1000)

# test 3
import time
systemOutPrint(time.time())
'''
