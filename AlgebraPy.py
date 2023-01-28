class Algebra:
    def __init__(self):
        self.answer = 0
        self.reactants = []
        self.vars = []
    
    def splitQuestion(self):
        self.var = []
        self.answer = int(self.question.split("=")[1])
        self.reactants = [i for i in self.question.split("=")[0]]
        for i in self.reactants:
            try:
                self.reactants[self.reactants.index(i)] = int(i)
            except Exception:
                if i.isalpha() == True:
                    self.var.append(i)
        self.reactants.reverse()
        
    def Equation(self, question):
        self.question = question
        self.splitQuestion()
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
        return "".join(self.reactants) + "=" + str(self.answer)
        
if __name__ == "__main__":
    pass
