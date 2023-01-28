#"x + 2 = 4"

class Algebra:
    def __init__(self):
        pass
        
    def BasicSolution(self, question):
        answer = int(question.split("=")[1])
        products = question.split(" =")[0].split(" ")
        for i in products:
            try:
                products[products.index(i)] = int(i)
            except Exception as e:
                pass
        products.reverse()
        while products != ['x']:
            for i in products:
                n = products.index(i)
                try:
                    if products[n+1] in ["+", "-", "/", "*"] and i != "x":
                        if products[n+1] == "+":
                            answer -= i
                        if products[n+1] == "-":
                            answer += i
                        if products[n+1] == "/":
                            answer *= i
                        if products[n+1] == "*":
                            answer /= i
                        products[n] = ''
                        products[n+1] = ''
                except Exception as e:
                    pass
            products.remove('')
        return answer
        
if __name__ == "__main__":
    pass