import re

def validate(lex):
    alpha = str.find(lex, "==Napkin==")
    omega = str.find(lex, "==/Napkin==")
    if alpha and omega:
        lex_luther = word[alpha+len("==Napkin=="):omega-1].strip()
        lex_luther = re.sub(re.compile("#.*?"), "", lex_luther)
        return lex_luther
    else:
        return "Stick to the Napkin guidelines please"
    
def ampersat(find):
    trooper = find[str.find(find, "@@")+2:].strip().splitlines()
    amp = trooper.pop(0)
    html = '\n'.join(trooper)
    return amp, html
        
