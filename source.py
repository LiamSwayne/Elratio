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

    # should program execute?
    execute = True

    while lines[-1] == "":
        lines = lines[:-1]

    firstLine = 0
    for i in range(len(lines)):
        if lines[i] != "":
            firstLine = i
            break
    
    lines = lines[firstLine:]

    for i in range(len(lines)):
        # remove indentation and get line
        line = lines[i]
        spaces = extractLeadingSpaces(line)
        line = line.lstrip()

        # compile empty lines
        if line == "":
            print("Error on line "+str(i+1))
            print("Empty lines must contain keyword \"empty\".")
            execute = False
            break
        elif line == "empty":
            line = ""
            lines[i] = spaces + line
            continue
        
        # compile comments
        if line[0] == "#":
            print("Error on line "+str(i+1))
            print("Comments cannot start with hashtags. Comments must start with the \"comment\" keyword followed by a space.")
            execute = False
            break
        elif line[:8] == "comment ":
            line = ""
            lines[i] = spaces + line
            continue
        
        # compile print statement syntax
        if line[:15] == "systemOutPrint(":
            line = "p" + line[10:]
        elif line[:6] == "print(":
            print("Error on line "+str(i+1))
            print("I am a compiler of principle. I do not accept print(). Use systemOutPrint() instead.")
            execute = False
            break
            
        # non-empty lines must end in semicolons
        if line[-1] == ";":
            line = line[:-1]
        elif line[-1] != ";" and line[-1] != ":":
            print("Error on line "+str(i)+": "+lines[i])
            print("Statements that do not end with a colon must end with a semicolon.")
            execute = False
            break

        # reinsert indentation into line
        lines[i] = spaces + line

    # Execute Elratio program
    program = newLine.join(lines)
    if execute:
        exec(program)
    else:
        print("Elratio program did not execute.")

# Elratio program (test case)
'''
comment test 1
systemOutPrint("a"*10+"\n\n");
empty
comment test 2
if True:
    systemOutPrint(1000);
empty
comment test 3
import time;
systemOutPrint(time.time());
empty
comment test 4
systemOutPrint(2000);
empty
comment test 5
3000;
empty
comment test 6
def add(a, b):
    return a+b;
empty
comment test 7
systemOutPrint(add(500,4000));
'''
