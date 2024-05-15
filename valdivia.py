import random
import numpy as np

def replace_to_dot(number): 
    try:
        return float(number.replace(",","."));
    except: None;


#FUNCTION THAT CONVERT 
def conversor(value):
    if(value == None):
        return None;
    if(("GB" not in value) and ("MB" not in value)):
        return replace_to_dot(value);
    if("GB"  in value):
        res = value[:-3];
        gb = replace_to_dot(res);
        return gb * 1000;
    else:
        res = value [:-3];
        gb = replace_to_dot(res);
        return gb;

def convert_arry(arry):
    res_arry = list(map(conversor,arry))
    return res_arry


vetor = []
for i in range(1, 11):
    if i % 2 == 0:
        vetor.append(f"{i} GB")
    else:
        vetor.append(f"{i} MB")

new_arry = []




print(vetor)
print(convert_arry(vetor))




