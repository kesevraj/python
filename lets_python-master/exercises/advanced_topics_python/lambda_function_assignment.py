from functools import reduce
def main():
   
  input_list= [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
	       ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]  
#   order=40
#   print_=list(map(lambda x: (x[0],x[2] * x[3]), orders)) 
#   usage=list(map(lambda x: x if x[3] >= order else (x[0], x[3] + 10),orders))
#   print(usage)
#   print(print_)
  minimumorder=100
  print_tuples = list(map(lambda x: x if x[1] >= minimumorder else (x[0], x[1] + 10),map(lambda x: (x[0],x[2] * x[3]), input_list)))
  print(print_tuples)


  values=[ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
	       [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
	       [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
  
  value= list(map(lambda y:[y[0], reduce(lambda a ,b: a+b,list(map(lambda x: x[1]*x[2],y[1:])))],values))
#   output =list(map(lambda x:(x[0],reduce(lambda a,b:a+b,list(map(lambda y:y[1]*y[2] ,x[1:])))),values))
 
#   result = [list(i)for i in output]

  
  print(value)
 
if __name__ =="__main__":
  main()