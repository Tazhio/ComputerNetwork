import math
if __name__=='__main__':

    def find_prime(start: int, end: int) -> list:#只是提示该函数 输入参数 和 返回值 的数据类型方便程序员阅读代码的。
        result=[]
        for i in range(start,end+1):
            isPrime:bool=True
            if(i>2):
                num_sqrt=math.sqrt(i+1)
                num_sqrt=int(num_sqrt)
                for j in range(2,num_sqrt+1):
                    if(i%j==0):
                        isPrime=False
                        break
            else:
                if(i==2):
                    isPrime=True
                else:isPrime=False
            if(isPrime):result.append(i)
        return result

    print(find_prime(1,100))
