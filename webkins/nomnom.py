import re

class Nomnom:
    def __init__(self,lexicon_luther):
        self.lex = lexicon_luther
    
    def validate(self):
        alpha = str.find(self.lex, "==Napkin==")
        omega = str.find(self.lex, "==/Napkin==")
        if alpha and omega:
            return word[:omega]

word = """#==Napkin==
#@blah blah
#@foo  bar 
#==/Napkin=="""

x = Nomnom(word)
print x.validate()
        
