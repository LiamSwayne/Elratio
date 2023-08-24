def transform(code):
    lines = code.split('\n')
    inBlockComment = False
    result = []

    for line in lines:
        if inBlockComment:
            if line.rstrip().endswith("'''") or line.rstrip().endswith('"""'):
                inBlockComment = False
            continue
        elif line.lstrip().startswith("'''") or line.lstrip().startswith('"""'):
            if line.rstrip().endswith("'''") or line.rstrip().endswith('"""'):
                continue
            else:
                inBlockComment = True
                continue
        
        if '#' in line:
            allSpaces = True
            for i in range(line.index("#")):
                if line[i] != " ":
                    allSpaces = False
            if allSpaces:
                line = line[:line.index('#')]
        
        result.append(line)
    
    return '\n'.join(result)

sourceFile = open('source.py', 'r')
sourceCode = ""
for line in sourceFile:
    if "# Elratio program" in line:
        break
    sourceCode += line
sourceFile.close()

cleanedCode = transform(sourceCode)
cleanedCode = cleanedCode.replace('\n', '\\n').replace('\"', '\\\"')

# remove leading \n's
while cleanedCode[0] == "\\" and cleanedCode[1] == "n":
    cleanedCode = cleanedCode[2:]

# remove trailing \n's
while cleanedCode[-2] == "\\" and cleanedCode[-1] == "n":
    cleanedCode = cleanedCode[:-2]

wrappedCode = "# Elratio compiler (turn off line-wrapping to hide Elratio source code)\nexec(\"\"\"" + cleanedCode + "\"\"\")\n\n# Elratio program\n\'\'\'\n\n\'\'\'"

compilerFile = open('template.py', 'w')
compilerFile.write(wrappedCode)
compilerFile.close()
