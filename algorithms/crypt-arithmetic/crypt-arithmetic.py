class CryptarithmeticProblem:
    def __init__(self, words, result):
        self.words = words  
        self.result = result 
        self.variables = set(''.join(words + [result])) 
        self.domain = range(10)  
        self.assignment = {} 

    def is_complete(self):
        return len(self.variables) == len(self.assignment)

    def select_unassigned_variable(self):
        unassigned = self.variables.difference(self.assignment.keys())
        return min(unassigned, key=lambda var: len(self.possible_assignments(var)))

    def possible_assignments(self, var):
        return [digit for digit in self.domain if self.is_consistent(var, digit)]

    def is_consistent(self, var, digit):
        if digit in self.assignment.values():
            return False

        self.assignment[var] = digit
        for word in self.words:
            if len(str(self.assignment[var])) > 1 and str(self.assignment[var])[0] == '0':
                return False
            word_value = self.word_to_value(word)
            if word_value == -1:
                return True
            if self.result.isdigit() and word_value > int(self.result):
                return False
        return True

    def word_to_value(self, word):
        value = ''
        for char in word:
            value += str(self.assignment.get(char, ''))
        if value == '':
            return -1
        return int(value)

    def solve_cryptarithmetic(self):
        return self.backtrack()

    def backtrack(self):
        if self.is_complete():
            return self.assignment

        var = self.select_unassigned_variable()
        for value in self.possible_assignments(var):
            self.assignment[var] = value
            result = self.backtrack()
            if result:
                return result
            del self.assignment[var]
        return None


words = ['CAKE', 'BAKE']
result = 'BREAD'

cryptarithmetic = CryptarithmeticProblem(words, result)
solution = cryptarithmetic.solve_cryptarithmetic()

if solution:
    print("Solution:")
    for var, value in solution.items():
        print(var, "=", value)
else:
    print("No solution found.")
