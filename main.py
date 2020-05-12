import os
import codecs
import re
from pygments.lexers import get_lexer_by_name
from pygments.lexers import get_lexer_for_filename
from pygments.token import Token

for curDir, dirs, ReadFiles in os.walk("<codefiles_PATH>"):
    for ReadFile in ReadFiles:
        PATH = os.path.join(curDir, ReadFile)
        SourceCodeFile = codecs.open(PATH, 'r', 'utf-8', 'ignore')
        filename = os.path.basename(PATH)

        try:
            lexer = get_lexer_for_filename(filename)
        except ValueError as e:
            continue
        
        ###特定の言語を指定したい場合（To specify a specific language）###
        if lexer.name != "Python":
            continue
        ######
    
        lines = SourceCodeFile.readlines()
        code = lines
        writeFile = open('wakachi/wakachi_'+lexer.name+'.txt',mode='a')
        for line in code:
            token_it = lexer.get_tokens_unprocessed(line)
            for idx, token_type, token_string in token_it:
                if re.match(r".*\n$",token_string):
                    writeFile.write(" \n")
                elif token_type in Token.Literal or token_type in Token.Comment or token_type in Token.Text :
                    continue
                elif token_type in Token.Error or token_type in Token.Other or token_type in Token.Generic:
                    continue
                else:
                    writeFile.write(token_string + ' ')
        SourceCodeFile.close
        writeFile.close

