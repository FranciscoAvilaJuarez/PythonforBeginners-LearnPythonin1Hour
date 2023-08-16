
#excecise 
#enter weight, tell it if is in Kg or Lbs, shoud take in caps or lc, then give you weight in opposite type

convert = 0.450

Weight = float( input("Please, Enter your Weight : ") ) 
Unit = input("Is this in (K)g or (L)bs?") 

if Unit.upper() == "L" : #input Kg      
    Kilos = float(Weight)//float(convert)   
    print("Your Weight in Kilos is : ", Kilos)

elif Unit.upper() == "K" : #input Lbs     
    Pounds = float(Weight)*float(convert) 
    print("Your Weight in Pounds is : ", Pounds)

#given ex 
i = 1 
while i <= 1_0 : 
    print(i)
    i = i + 1 

e = 1   
while e <= 1_0 :
    print(e * "*")
    e = e + 1 





    