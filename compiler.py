# Elratio compiler (turn off line-wrapping or you'll see the entire Elratio source code)
exec("""\n\ndef extractLeadingSpaces(inputString):\n    leadingSpaces = \"\"\n    for char in inputString:\n        if char.isspace():\n            leadingSpaces += char\n        else:\n            break\n    return leadingSpaces\n\n\nwith open(__file__, 'r') as file:\n    sourceCode = file.read()\n\n\nsplitIndex = sourceCode.find(\"\'\'\'\")\n\n\nnewLine = chr(10)\n\n\nif splitIndex == -1:\n    print(\"Elratio program missing \'\'\'. This is a shameful mistake. The compiler will remember this.\")\nelse:\n    \n    program = sourceCode[splitIndex + 3:]\n    program = program[:program.index(\"\'\'\'\")]\n    lines = program.split(newLine)\n\n    for i in range(len(lines)):\n        \n        line = lines[i]\n        spaces = extractLeadingSpaces(line)\n        line = line.lstrip()\n\n        \n        if line[:15] == \"systemOutPrint(\":\n            line = \"p\" + line[10:]\n        elif line[:6] == \"print(\":\n            print(\"I am a compiler of principle. I do not accept print(). Use systemOutPrint() instead.\")\n\n        \n        lines[i] = spaces + line\n\n    \n    program = newLine.join(lines)\n    exec(program)\n\n""")

# Elratio program
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