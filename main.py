from helpers import *
import numpy as np

# in this code we will use integer based arithmatic code insted of the infinte presciosn version 

stream = [1,2,3,4,5,7,85,4,5,7,-5,516,8,1,68,1,313,-5,18,9,7,351,32,15,6,84,13,20,56,85,4,55,6,7,85,4,5,7,4,5,6,7,86,7,8,8,7,6,85,7,4,5,6,7]
stream=stream*20

precision=32
stream_size=len(stream)+1 # add the end of  file symbol

code =Arithmatic_encode(stream,precision)
print (code)
print (len(code))



code_size=len(code)
# those numbers will be used later in the scaling and emitting step of the binary bits
full =2**precision
half=full//2
quarter=half//2

L=0 # the lower limit of the range
H=full # the upper limit of the range

val=0 # a variable to trace how deep i entered at the corner case of which the low and high limits are lying in the middle of the range
indx=1

dic=getfreqs(stream) #output the the dictionary that contains the probabilities of  all ymbols
message=[]

while indx <= precision and indx <= code_size:# first get the exact amount of values that can be held in the precsion available , the rest will be used during the code
    if code[indx-1]==1:
        val=val+2**(precision-indx)
    indx+=1
flag=1
iterrr=0

while flag:
    iterrr+=1   
    for symbol in dic:  
        
        freqSym=dic[symbol]    # get the frequency of the symbol
        S_high=Cumfreq(symbol,dic)   # get the higher limit of this symbol
        S_low=S_high-freqSym             # get the lower limit of this symbol
        
        Range=H-L                   # get the range of the code  
        
        H0 = L + Range * S_high//stream_size 
        L0 = L + Range * S_low //stream_size 
        
        if  L0 <=val and val<H0:
            message.extend([symbol])
            L=L0
            H=H0 
            if symbol == '!':
                flag=0
            break    
                
    while True:
        if H < half : # if the range is in the lower half
            L*=2
            H*=2
            val*=2
            if indx<= code_size:
                val+=code[indx-1]
                indx+=1 
        elif L >= half : # if the range is in the upper half
            L=2*(L-half)
            H=2*(H-half)
            val=2*(val-half)
            if indx<= code_size:
                val+=code[indx-1]
                indx+=1 
        elif L>=quarter and H < 3*quarter:
            L=2*(L-quarter)
            H=2*(H-quarter)
            val=2*(val-quarter)
            
            if indx<= code_size:
                val+=code[indx-1]
                indx+=1 
        else:
            break
print(stream)     
print (message)
print(stream == message)
        
######################################################33

# ###################################3

# while flag:
#     iterrr+=1
#     for symbol in dic:  
        
#         freqSym=dic[symbol]    # get the frequency of the symbol
#         S_high=Cumfreq(symbol,dic)   # get the higher limit of this symbol
#         S_low=S_high-freqSym             # get the lower limit of this symbol
        
#         Range=H-L +1                 # get the range of the code  
        
#         H0 = L + Range * S_high//stream_size -1
#         L0 = L + Range * S_low //stream_size 
        
#         if  L0 <=val and val<H0:
#             message.extend([symbol])
#             L=L0
#             H=H0 
#             if symbol == '!':
#                 flag=0
#     while True:
#         if L >= half : # if the range is in the upper half
#             L-=half
#             H-=half
#             val-=half
#         elif L>=quarter and H < 3*quarter:
#             L-=quarter
#             H-=quarter
#             val-=quarter
#         else:
#             break
#         L=2*L
#         H=2*H   
#         val=2*val
#         if indx<=code_size:
#             val+=code[indx]
#         indx+=1         
        