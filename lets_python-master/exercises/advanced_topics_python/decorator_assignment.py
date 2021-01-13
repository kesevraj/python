def main():
 
 def logged(func):
    
    def inner(*args,**kwargs):
        print("you called func",args)
        print ("it returned",func(**kwargs)*2)
        return func(*args)

    return inner
    
    
 @logged
 def func(*args,**kwargs):
  return 3 + len(args)
 
 print(func(4,4,4))
if __name__=="__main__":
 main()    