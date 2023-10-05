class Instances:
    def sup_fibonacci(self,n: int) -> int:
        if n <= 1:
            return n
        else:
            return(self.sup_fibonacci(n-1) + self.sup_fibonacci(n-2))
    
    def fibonacci(self,*args: int) -> str:
        """
        Encontra n-ésimo número da sequência de fibonacci.
        Parâmetros:
        n: número inteiro
        """
        n = int(args[0])
        answer = ''
        for i in range(n+1):
            answer += f"{str(self.sup_fibonacci(i))}"
            if i != n: answer += " - "
        return answer
    
    def prime(self,*args: float) -> str:
        """
        Encontra os números primos até o n-ésimo número.
        Parâmetros: 
        n: número inteiro
        """
        n = int(args[0])
        if n == 0 or n == 1: return "- "
        answer = ''
        for num in range(2,n+1):
            if all(num%i!=0 for i in range(2,num)):
                answer += f"{str(num)} - "
        return answer.removesuffix(' - ')
    
    def sum(self,*args: float) -> float:
        """
        Retorna a soma de todos os números.
        Parâmetros:
        args: números inteiros ou flutuantes
        """
        s = 0
        for i in args:
            s += float(i)
        return s
    
    def mean(self,*args: float) -> float:
        """
        Retorma a média aritmética dos valores recebidos.
        Parâmetros:
        args: números inteiros ou flutuantes
        """

        return self.sum(*args)/len(args)
