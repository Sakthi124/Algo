def search(pat,txt): 

 m=len(pat) 

 n=len(txt) 

 for i in range(n-m+1): 

 for j in range(m): 

 if(txt[i+j]!=pat[j]): 

 break 

 if(j==m-1): 

 print("pattern found at index :",i) 

txt=input("enter the text:") 

pat=input("enter the pattern to search :") 

search(pat,txt)
