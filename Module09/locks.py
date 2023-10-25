def caching_fibonacci():
    cache = {0: 0, 1: 1, 1: 1}
    def fibonacci(n):        
        if n in cache.keys():
            return cache.get(n)
        else:
            if n <= 1: 
                cache[n] = n
                return n
            else: 
                return (fibonacci(n - 1) + fibonacci(n - 2))
       
    
    return fibonacci

print(caching_fibonacci()(5))