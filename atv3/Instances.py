class Instances:
    def sup_fibonacci(self,n: int) -> int:
        if n <= 1:
            return n
        else:
            return(self.sup_fibonacci(n-1) + self.sup_fibonacci(n-2))
    
    def fibonacci(self,n: int) -> str:
        """
        Encontra nésimo número da sequência de fibonacci.
        Parâmetros:
        n: número inteiro
        """
        answer = ''
        for i in range(n+1):
            answer += f"{str(self.sup_fibonacci(i))}"
            if i != n: answer += " - "
        return answer
    
    def prime(self,n:int) -> str:
        if n == 0 or n == 1: return "- "
        """
        Encontra os números primos até o nésimo número.
        Parâmetros: 
        n: número inteiro
        """
        answer = ''
        for num in range(2,n+1):
            if all(num%i!=0 for i in range(2,num)):
                answer += f"{str(num)} - "
        return answer.removesuffix(' - ')
    
    def sum(self,a,b):
        """
        Soma dois números.
        Parâmetros:
        a,b: números inteiros ou flutuantes
        """
        return a+b
