from ortools.sat.python import cp_model


class CountSolutions(cp_model.CpSolverSolutionCallback):
    """Count the number of solutions."""
    def __init__(self):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__solution_count = 0

    def on_solution_callback(self): 
       self.__solution_count += 1

    def solution_count(self): # getter
        return self.__solution_count 
solution_printer = CountSolutions()

# Instantiate model and solver
model = cp_model.CpModel()
solver = cp_model.CpSolver()

# 1. Variables
capacity = 19
bread = model.NewIntVar(0, capacity, 'Bread')
meat  = model.NewIntVar(0, capacity, 'Meat')
beer  = model.NewIntVar(0, capacity, 'Beer')

# 2. Constraints
model.Add(1 * bread + 3 * meat + 7 * beer <= capacity)

# Print results
solver.parameters.enumerate_all_solutions = True
status = solver.Solve(model, solution_printer)
print(solution_printer.solution_count())
