def dfs_n_queens(n):
    res = []
    
    # current_solution: egy lista, ahol az i-edik elem az i-edik oszlopban lévő királynő sora
    def backtrack(current_solution, cols_used, pos_diags, neg_diags):
        col = len(current_solution)
        
        # Ha elértük az N-edik oszlopot, találtunk egy megoldást
        if col == n:
            res.append(list(current_solution))
            return

        # Végigmegyünk az összes lehetséges soron az adott oszlopban
        for row in range(n):
            # Ellenőrizzük az ütéseket
            # Pozitív átló: row + col | Negatív átló: row - col
            if row in cols_used or (row + col) in pos_diags or (row - col) in neg_diags:
                continue
            
            # Lépés (DFS mélyítés)
            current_solution.append(row)
            cols_used.add(row)
            pos_diags.add(row + col)
            neg_diags.add(row - col)
            
            backtrack(current_solution, cols_used, pos_diags, neg_diags)
            
            # Visszalépés (Backtracking)
            current_solution.pop()
            cols_used.remove(row)
            pos_diags.remove(row + col)
            neg_diags.remove(row - col)

    backtrack([], set(), set(), set())
    return res

# Tesztelés
print(f"n=4: {dfs_n_queens(4)}")
print(f"n=5: {dfs_n_queens(5)}")

