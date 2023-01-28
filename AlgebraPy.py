import re
class Algebra:
    def __init__(self):
        self.answer = 0
        self.reactants = []
        self.var = []
        self.finalvar = []
    
    def splitQuestion(self):
        self.answer = int(self.question.split("=")[1])
        try:
            self.reactants = re.split('(\W+)', self.question.split("=")[0].replace(" ", ""))
        except Exception:
            pass
        for i in self.reactants:
            try:
                self.reactants[self.reactants.index(i)] = int(i)
            except Exception:
                if i not in ['+', '-', '/', '*']:
                    self.var.append(i)
        self.reactants.reverse()
        
    def Equation(self, question):
        self.question = question
        self.splitQuestion()
        print(self.reactants)
        while self.reactants[0] not in self.var:
            for i in self.reactants:
                n = self.reactants.index(i)
                try:
                    if self.reactants[n+1] in ["+", "-", "/", "*"] and i not in self.var:
                        if self.reactants[n+1] == "+":
                            self.answer -= i
                        if self.reactants[n+1] == "-":
                            self.answer += i
                        if self.reactants[n+1] == "/":
                            self.answer *= i
                        if self.reactants[n+1] == "*":
                            self.answer /= i
                        self.reactants[n] = ''
                        self.reactants[n+1] = ''
                except Exception:
                    pass
            try:
                self.reactants.remove('')
            except Exception:
                pass
        try:
            self.finalvar = re.split('(\d+)', self.reactants[0])
            self.finalvar.remove('')
            self.finalvar.remove('')
            print(self.finalvar)
            if self.finalvar[0].isalpha() == False:
                print('a')
                self.answer *= int(self.finalvar[0])
                self.reactants[0] = self.reactants[0].replace(self.finalvar[0], '')
            if self.finalvar[1].isalpha() == False:
                print('b') 
                self.answer **= 1/int(self.finalvar[1])
                self.reactants[0] = self.reactants[0].replace(self.finalvar[1], '')
            if self.finalvar[2].isalpha() == False:
                print('c')
                self.answer **= 1/int(self.finalvar[2])
                self.reactants[0] = self.reactants[0].replace(self.finalvar[2], '')
        except Exception as e:
            print(e)
        return "".join(self.reactants) + "=" + str(self.answer)
        
if __name__ == "__main__":
    pass
