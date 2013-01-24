import re

class Nomnom:
    def __init__(self,lexicon_luther):
        self.lex = lexicon_luther
    
    def validate(self):
        alpha = str.find(self.lex, "==Napkin==")
        omega = str.find(self.lex, "==/Napkin==")
        if alpha and omega:
            lex_luther = word[alpha+len("==Napkin=="):omega-1].strip()
            lex_luther = re.sub(re.compile("#.*?"), "", lex_luther)
            return lex_luther
        else:
            return "Stick to the Napkin guidelines please"
    
    def alloc(self):
        var, keywords = {}, validate(self.lex)
        print keywords
        
        
word = """#==Napkin==
#@blah blah
#@foo  bar 
#==/Napkin=="""

x = Nomnom(word)
print x.validate()
        
