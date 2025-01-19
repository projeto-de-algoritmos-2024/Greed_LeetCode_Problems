from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Ordenar os cursos pelo prazo final (lastDay)
        courses.sort(key=lambda x: x[1])
        
        # Usar um heap para armazenar as durações dos cursos escolhidos
        max_heap = []

        # Variável que vai ir armazenando o tempo gasto até o momento
        total_time = 0

        for duration, last_day in courses:
            # Adicionar o curso atual ao total e à heap
            heapq.heappush(max_heap, -duration)  # Usar valores negativos para simular uma heap máxima
            total_time += duration

            # Se o total exceder o prazo do curso atual, remover o curso mais longo
            if total_time > last_day:
                total_time += heapq.heappop(max_heap)  # Remover o maior valor (negativo)

        # O tamanho da heap é o número máximo de cursos que podemos fazer
        return len(max_heap)

# Exemplo
solucao = Solution()

s1 = solucao.scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]])
print(f"Número de cursos que conseguiria fazer: {s1}")
s2 = solucao.scheduleCourse([[1,2]])
print(f"Número de cursos que conseguiria fazer: {s2}")
s3 = solucao.scheduleCourse([[3,2],[4,3]])
print(f"Número de cursos que conseguiria fazer: {s3}")