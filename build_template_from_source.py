def removeComments(code):
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
                    allSPaces = False
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

cleanedCode = removeComments(sourceCode)
cleanedCode = cleanedCode.replace('\n', '\\n').replace('\"', '\\\"')
wrappedCode = "# Elratio compiler (turn off line-wrapping to hide Elratio source code)\nexec(\"\"\"" + cleanedCode + "\"\"\")\n\n# Elratio program\n\'\'\'\n\n\'\'\'"

compilerFile = open('template.py', 'w')
compilerFile.write(wrappedCode)
compilerFile.close()
