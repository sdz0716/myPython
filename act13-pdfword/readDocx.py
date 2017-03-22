# python3

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

#可以调整输出的格式。例如fullText.append(' ' + para.text),或return '\n\n'.join(fullText)
