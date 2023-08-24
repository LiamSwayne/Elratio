# DO NOT use triple single quote, triple double quote or the python newline character

def extractLeadingSpaces(inputString):
    leadingSpaces = ""
    for char in inputString:
        if char.isspace():
            leadingSpaces += char
        else:
            break
    return leadingSpaces

def errorMessage(lineIndex,message):
    global execute
    global lines
    
    print("Error on line "+str(lineIndex+1)+": "+lines[lineIndex])
    print(message)
    execute = False

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

    # remove empty lines from beggining and end
    while lines[0] == "":
        lines = lines[1:]
    while lines[-1] == "":
        lines = lines[:-1]

    for i in range(len(lines)):
        # remove indentation and get line
        line = lines[i]
        spaces = extractLeadingSpaces(line)
        line = line.lstrip()

        # disallow variables from having keyword names
        elratioKeywords = ["comment","create","definition","empty","end"]
        lineCopy = line.replace("="," = ")
        chunks = lineCopy.split(" ")
        if len(chunks) > 1:
            if chunks[0] in elratioKeywords and chunks[1] == "=":
                errorMessage(i,"\""+chunks[0]+"\" is an Elratio keyword and cannot be assigned.")
                break

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

        # compile class creation
        if line[:13] == "create class ":
            line = line[7:]
        elif line[:6] == "class ":
            print("Error on line "+str(i+1))
            print("Classes must be created using the \"create\" keyword.")
            execute = False
            break

        # compile method definitions
        if line[:11] == "definition ":
            line = line[:3] + line[10:]
        elif line[:4] == "def ":
            print("Error on line "+str(i+1))
            print("\"def\"? Not a chance. Methods must be defined using the \"definition\" keyword.")
            execute = False
            break

        # reinsert indentation into line
        lines[i] = spaces + line

    # last line must be keyword "end"
    if lines[-1].lower() == "end":
        lines = lines[:-1]
    else:
        print("Error.")
        print("Elratio programs must end with the \"end\" keyword followed by a semicolon.")
        execute = False

    # Execute Elratio program
    program = newLine.join(lines)
    if execute:
        exec(program)
    else:
        print("Elratio program did not execute.")

# Elratio program (test case)
'''
comment test 1
systemOutPrint("a"*10+"\n");
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
definition add(a, b):
    return a+b;
empty
comment test 7
systemOutPrint(add(500,4000));
empty
comment test 8
commenter=5;
empty
empty
comment final test
end;
'''
