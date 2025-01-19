class Solution(object):
    def numRescueBoats(self, people, limit):
        # Ordena os pesos em ordem crescente
        people.sort()
        
        # Inicializa dois ponteiros: um no início e outro no final do array
        left, right = 0, len(people) - 1
        
        # Conta o número de barcos necessários
        boats = 0
        
        while left <= right:
            # Sempre tenta colocar a pessoa mais leve com a mais pesada
            if people[left] + people[right] <= limit:
                left += 1  # Move o ponteiro do mais leve
            
            # Sempre move o ponteiro do mais pesado
            right -= 1
            
            # Incrementa o número de barcos
            boats += 1
        
        return boats

# Exemplo
solucao = Solution()

s1 = solucao.numRescueBoats([1,2], 3)
print(f"Número de barcos: {s1}")
s2 = solucao.numRescueBoats([3,2,2,1], 3)
print(f"Número de barcos: {s2}")
s3 = solucao.numRescueBoats([3,5,3,4], 5)
print(f"Número de barcos: {s3}")