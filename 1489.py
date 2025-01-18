class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):

        # Estrutura de dados Union-Find
        class UnionFind:
            # Inicializa o pai e o nível (na árvore) de cada nó
            def __init__(self, n):
                self.pai = list(range(n))
                self.nivel = [0] * n

            # Find(x) é a função que vai localizar o elemento x e retornar a qual árvore ele pertence
            def find(self, x):
                # Vai subindo na árvore enquanto o pai não for igual ao elemento x
                if self.pai[x] != x: 
                    self.pai[x] = self.find(self.pai[x]) 
                # Retorna exatamente a árvore a qual x
                return self.pai[x] 

            # Union(x, y) é a função que vai "unir" duas árvores diferentes
            def union(self, x, y):
                raizX = self.find(x) # retorna a que árvore pertence x
                raizY = self.find(y) # retorna a que árvore pertence y
                # Vendo se as raízes (árvores) são diferentes
                if raizX != raizY:
                    # Aqui faz a verificação de qual árvore tem o menor nível, e assim sempre tentar mantê-lo
                    if self.nivel[raizX] > self.nivel[raizY]: 
                        self.pai[raizY] = raizX 
                    elif self.nivel[raizX] < self.nivel[raizY]:
                        self.pai[raizX] = raizY
                    # A árvore que tiver o maior nível será aquela que entrará debaixo da de menor nível

                    # Aqui incrementamos o nível quando necessário
                    else:
                        self.pai[raizY] = raizX
                        self.nivel[raizX] += 1
                    return True
                return False

        # Algoritmo de Kruskal modificado para retornar apenas o peso da MST
        def Kruskal(n, edges, descard_edge=-1, use_edge=-1):
                        
            union_find = UnionFind(n) # Crio minha estrutura de Union-Find para os n nós
            peso_MST = 0  # Peso total da MST
            edges_MST = 0    # Contador de arestas usadas na MST

            # Fazer caso haja uma aresta obrigatória
            if use_edge != -1:
                a, b, p, _ = edges[use_edge] # a = primeiro vértice, b = segundo vértice e p = peso da aresta
                if union_find.union(a, b):
                    peso_MST += p
                    edges_MST += 1

            # Processa as outras arestas
            for i, (a, b, p, _) in enumerate(edges):

                # Ignora a aresta excluída e continua
                if i == descard_edge:  
                    continue

                # Quando o Union for feito, incrementamos o peso dessa aresta e o número de arestas da MST
                if union_find.union(a, b):  
                    peso_MST += p
                    edges_MST += 1

            # Verifica se todas as n-1 arestas foram usadas e retorna seu peso
            return peso_MST if edges_MST == n - 1 else float('inf')

        # Para ajudar posteriormente na análise se é crítica ou pseudo-crítica, daremos um índice i para cada aresta
        index_edges = [(a, b, p, i) for i, (a, b, p) in enumerate(edges)]
        
        # Ordena as arestas pelo seu peso, do menor para o maior (1º passo do Kruskal como um todo)
        index_edges.sort(key=lambda x: x[2])

        # Calcula o peso da MST original
        peso_MST_original = Kruskal(n, index_edges)

        # Inicializa as listas de arestas críticas e pseudo-críticas
        critical_edges = []      
        pseudo_critical_edges = []

        # Verifica cada aresta
        for i, (a, b, p, index) in enumerate(index_edges):
            # Testa se a aresta é crítica vendo se o peso ao retirá-la é maior que o peso original da MST
            if Kruskal(n, index_edges, descard_edge=i) > peso_MST_original:
                # Se sim, adiciona na lista de críticas
                critical_edges.append(index)

            # Testa se a aresta é pseudo-crítica cendo se o peso não muda se ela for retirada
            elif Kruskal(n, index_edges, use_edge=i) == peso_MST_original:
                # Se sim, adiciona na lista de pseudo-críticas
                pseudo_critical_edges.append(index)

        # Retorna as listas de arestas críticas e pseudo-críticas
        return [critical_edges, pseudo_critical_edges]

# Exemplo
solucao = Solution()

s1 = solucao.findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]])
print(s1)
s2 = solucao.findCriticalAndPseudoCriticalEdges(4, [[0,1,1],[1,2,1],[2,3,1],[0,3,1]])
print(s2)