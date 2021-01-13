import os
def main():
 def printalldir():
   files_path = [os.path.abspath(x) for x in os.listdir()]
   return files_path
   
 def list_exluding_dir(folder):
    return [
        d for d in (os.path.abspath(d1) for d1 in os.listdir(folder))
        if not (os.path.isdir(d))
    ]

    
 def endswith(folder):
    filelist= [file for file in os.listdir(folder) if file.endswith('.png') or file.endswith('.jpg')  ] 
    return filelist

 def no_of_spaces(strs):
    spaces = [s for s in strs if s == ' ']
    return len(spaces)

 def remove_vowels(strs):
    return "".join([char for char in strs if char not in "aeiouAEIOU"])

 def print_words(sentence):
    #  words=[]
    #  words=sentence.split()
     word= [char for char in list(sentence.split())  if len(char)<=4] 
     return word

 def len_words(sentence):
    print ("length of words")
    [print(char, ":" ,len(char)) for char in list(sentence.split())] 
     
     

#   function calls
 print()
 print("print all dirctory : ",printalldir())

 print()
 print("list excluding directory : ",list_exluding_dir("F:\idealistic\lets_python-master"))

 print()
 print("endswith .jpg &.png :" ,endswith("images"))

 print()
 print("no of spaces in string : "
 ,no_of_spaces("a b fa eafaeg dsafAW"))

 print()
 print("string after vowels removed : " ,remove_vowels("there should not be vowel"))

 print()
 print("words less than 4 : ",print_words("print the words less than 4 words"))

 print()
 len_words("print the length of words in a sentences")


if __name__ =="__main__":
  main()
