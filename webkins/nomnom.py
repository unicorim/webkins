import re

def validate(self):
    alpha = str.find(self.lex, "==Napkin==")
    omega = str.find(self.lex, "==/Napkin==")
    if alpha and omega:
        lex_luther = word[alpha+len("==Napkin=="):omega-1].strip()
        lex_luther = re.sub(re.compile("#.*?"), "", lex_luther)
        return lex_luther
    else:
        return "Stick to the Napkin guidelines please"
    
def failsafe(self):
    var, keywords = {}, validate(self.lex)
        
        
