# Elratio compiler (turn off line-wrapping to hide Elratio source code)
exec("""def extractLeadingSpaces(inputString):\n    leadingSpaces = \"\"\n    for char in inputString:\n        if char.isspace():\n            leadingSpaces += char\n        else:\n            break\n    return leadingSpaces\n\ndef errorMessage(lineIndex,message):\n    global execute\n    global lines\n    \n    print(\"Error on line \"+str(lineIndex+1)+\": \"+lines[lineIndex])\n    print(message)\n    execute = False\n\ndef reverseIndentation(programLines):\n    maxIndent = 0\n    \n    \n    for line in programLines:\n        if line.strip():\n            indent = len(line) - len(line.lstrip())\n            maxIndent = max(maxIndent, indent)\n    \n    reversedLines = []\n    \n    \n    for line in programLines:\n        if line.strip():\n            indent = len(line) - len(line.lstrip())\n            newIndent = maxIndent - indent\n            reversedLines.append(' ' * newIndent + line.lstrip())\n        else:\n            reversedLines.append(line)\n    \n    return reversedLines\n\n\nwith open(__file__, 'r') as file:\n    sourceCode = file.read()\n\n\nsplitIndex = sourceCode.find(\"\'\'\'\")\n\n\nnewLine = chr(10)\n\n\nif splitIndex == -1:\n    print(\"Elratio program missing \'\'\'. This is a shameful mistake. The compiler will remember this.\")\nelse:\n    \n    program = sourceCode[splitIndex + 3:]\n    program = program[:program.index(\"\'\'\'\")]\n    lines = program.split(newLine)\n\n    \n    execute = True\n\n    \n    createdList = []\n\n    \n    while lines[0] == \"\":\n        lines = lines[1:]\n        if len(lines) == 0:\n            break\n    if len(lines) > 0:\n        while lines[-1] == \"\":\n            lines = lines[:-1]\n            if len(lines) == 0:\n                break\n    \n    if len(lines) == 0:\n        print(\"Empty program. Don't send me that crap next time, jerk!\")\n        execute = False\n    \n    \n    lines = reverseIndentation(lines)\n\n    for i in range(len(lines)):\n        \n        line = lines[i]\n        spaces = extractLeadingSpaces(line)\n        line = line.lstrip()\n\n        \n        elratioKeywords = [\"comment\",\"create\",\"definition\",\"empty\",\"end\"]\n        lineCopy = line.replace(\"=\",\" = \")\n        chunks = lineCopy.split(\" \")\n        if len(chunks) > 1:\n            if chunks[0] in elratioKeywords and chunks[1] == \"=\":\n                errorMessage(i,\"\\"\"+chunks[0]+\"\\" is an Elratio keyword and cannot be assigned.\")\n                break\n\n        \n        if line == \"\":\n            errorMessage(i,\"Empty lines must contain keyword \\"empty\\".\")\n            break\n        elif line == \"empty;\":\n            lines[i] = spaces\n            continue\n        elif line == \"empty\":\n            errorMessage(i,\"Statements that do not end with a colon must end with a semicolon.\")\n            break\n        \n        \n        if line[0] == \"#\":\n            errorMessage(i,\"Comments cannot start with hashtags. Comments must start with the \\"comment\\" keyword followed by a space.\")\n            break\n        elif line[:8] == \"comment \":\n            lines[i] = spaces\n            continue\n\n        \n        if line[-1] == \";\":\n            line = line[:-1]\n        elif line[-1] != \";\" and line[-1] != \":\":\n            errorMessage(i,\"Statements that do not end with a colon must end with a semicolon.\")\n            break\n\n        \n        if line[:6] == \"class \":\n            errorMessage(i,\"Classes must be created using the \\"create\\" keyword.\")\n            break\n        elif line[:13] == \"create class \":\n            if \"create\" in createdList:\n                line = line[7:]\n            else:\n                errorMessage(i,\"Keyword \\"create\\" has not been created yet. Try adding \\"create create\\" to to your program.\")\n                break\n\n        \n        if line.split(\" \")[0] == \"create\":\n            if line == \"create create\":\n                createdList.append(\"create\")\n            elif \"create\" in createdList:\n                createdList.append(line.split(\" \")[1])\n            else:\n                errorMessage(i,\"Keyword \\"create\\" has not been created yet. Try adding \\"create create\\" to to your program.\")\n                break\n            lines[i] = spaces\n            continue\n        \n        \n        if line[:15] == \"systemOutPrint(\":\n            line = \"p\" + line[10:]\n        elif line[:6] == \"print(\":\n            errorMessage(i,\"I am a compiler of principle. I do not accept print(). Use systemOutPrint() instead.\")\n            break\n\n        \n        if line[:11] == \"definition \":\n            line = line[:3] + line[10:]\n        elif line[:4] == \"def \":\n            errorMessage(i,\"\\"def\\"? Not a chance. Methods must be defined using the \\"definition\\" keyword.\")\n            break\n\n        \n        exit = False\n        for j in range(10):\n            if str(j) in line and str(j) not in createdList:\n                errorMessage(i,\"The digit \\"\"+str(j)+\"\\" has not been created yet. Try using \\"create \"+str(j)+\"\\" first.\")\n                exit = True\n                break\n        if exit:\n            break\n            \n\n        \n        lines[i] = spaces + line\n\n    \n    if len(lines) > 0 and execute:\n        if lines[-1].strip().lower() == \"end\":\n            lines = lines[:-1]\n        else:\n            print(\"Error.\")\n            print(\"Elratio programs must end with the \\"end\\" keyword followed by a semicolon.\")\n            execute = False\n\n    \n    program = newLine.join(lines)\n    if execute:\n        exec(program)\n    else:\n        if len(lines) > 0:\n            print(\"Elratio program did not execute.\")""")

# Elratio program (all code must go inside the quotes)
'''
        comment test 1
        create create;
        create 0;
        create 1;
        systemOutPrint("a"*10);
        empty;
        if True:
    systemOutPrint(1000);
        empty;
        import time;
        systemOutPrint(time.time());
        empty;
        comment test 2
        create 2;
        systemOutPrint(2000);
        empty;
        create 3;
        3000;
        empty;
        comment test 3
        definition add(a, b):
    return a+b;
        empty;
        create 4;
        create 5;
        systemOutPrint(add(500,4000));
        empty;
        create class c:
    pass;
    create class d:
pass;
        empty;
        comment final test
        end;
'''