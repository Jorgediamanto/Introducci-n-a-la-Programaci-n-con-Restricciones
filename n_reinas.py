from ortools.sat.python import cp_model

def n_reinas(n):
    # Crear el modelo
    model = cp_model.CpModel()

    # Variables
    reinas = [model.NewIntVar(0, n - 1, f'reina_{i}') for i in range(n)]

    # Restricciones
    model.AddAllDifferent(reinas)
    for i in range(n):
        for j in range(i + 1, n):
            model.AddAbs(reinas[i] - reinas[j]) != j - i

    # Resolver el modelo
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Imprimir la solución
    if status == cp_model.FEASIBLE:
        for i in range(n):
            print(f'Reina {i}: Columna {solver.Value(reinas[i])}')

if __name__ == '__main__':
    n_reinas(8)  # Cambia el valor para un tablero de tamaño diferente
