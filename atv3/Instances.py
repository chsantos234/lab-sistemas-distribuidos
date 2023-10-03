class Instances:
    def sup_fibonacci(self,n: int) -> int:
        if n <= 1:
            return n
        else:
            return(self.sup_fibonacci(n-1) + self.sup_fibonacci(n-2))
    
    def fibonacci(self,n: int) -> str:
        """encontra nésimo número da sequência de fibonacci"""
        answer = ''
        for i in range(n+1):
            answer += f"{str(self.sup_fibonacci(i))}"
            if i != n: answer += " - "
        return answer
    
    def prime(self,n:int) -> str:
        """encontra os números primos até o nésimo número"""
        answer = ''
        for num in range(2,n+1):
            if all(num%i!=0 for i in range(2,num)):
                answer += f"{str(num)} - "
        return answer.removesuffix(' - ')
    
    def sum(self,a,b):
        """soma números"""
        return a+b
