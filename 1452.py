import math

rank=["1","2","3","4"]
print(rank)
print("1-rank 1")
print("2-rank 2")
print("3-rank 3")
print("4-rank 4")

item=input("pleas chooes rank:")
i=100
for i in item:

    if item=="1":
    
        number_1=eval(input("pleas enter the number_1:" ))
        print(number_1)
        X1=(math.sin(math.radians((number_1)))+1)
        X2=(math.sin(math.radians((number_1)))+2)
        print(X1)
        print(X1)
        print(X2)
        X=X1/X2
        print(X)
        Y=((number_1-X)/number_1)*100
        print(Y)
        print(f"b0={number_1} beacas rank 1")
        print(f"error is{Y}")
    elif item=="2":
        number_1=eval(input("pleas enter the number_1:" ))
        print(number_1)
        number_2=eval(input("pleas enter the number_2:" ))
        print(number_2)

        X1=(math.sin(math.radians((number_1)))+1)
        X2=(math.sin(math.radians((number_1)))+2)
        print(X1)
        print(X2)
        X=X1/X2
        print(X) 
        X3=(math.sin(math.radians((number_2)))+1)
        X4=(math.sin(math.radians((number_2)))+2)
        print(X3)
        print(X4)
        G=X3/X4
        print(G) 
        T=(G-X)/(number_2-number_1)
        print(f"b1 is {T} and b0 is {number_1}")
        total=number_1+T*(number_1-number_1)
        print(total)
        error=((total-X)/total)*100
        print(f"error is{error}")
        
    elif item=="3":
        number_1=eval(input("pleas enter the number_1:" ))
        print(number_1)
        number_2=eval(input("pleas enter the number_2:" ))
        print(number_2)
        number_3=eval(input("pleas enter the number_3:" ))
        print(number_3)

        X1=(math.sin(math.radians((number_1)))+1)
        X2=(math.sin(math.radians((number_1)))+2)
        print(X1)
        print(X2)
        X=X1/X2
        print(X) 
        X3=(math.sin(math.radians((number_2)))+1)
        X4=(math.sin(math.radians((number_2)))+2)
        print(X3)
        print(X4)
        G=X3/X4
        print(G) 
        X5=(math.sin(math.radians((number_3)))+1)
        X6=(math.sin(math.radians((number_3)))+2)
        print(X5)
        print(X6)
        H=X5/X6
        print(H) 
        T=(G-X)/(number_2-number_1)
        print(f"b1 is {T} and b0 is {number_1}")
        T1=(H-G)/(number_3-number_2)
        b2=(T1-T)/(number_3-number_1)
        print(f"b0 is {number_1} and b1 is {T} and b2 is {b2}")
        total_2=number_1+T*(number_1-number_1)+b2*(number_1-number_1)*(number_1-number_2)
        error_2=((total_2-H)/total_2)*100
        print(f"error is {error_2}")

    elif item=="4":
        number_1=eval(input("pleas enter the number_1:" ))
        print(number_1)
        number_2=eval(input("pleas enter the number_2:" ))
        print(number_2)
        number_3=eval(input("pleas enter the number_3:" ))
        print(number_3)
        number_4=eval(input("pleas enter the number_4:" ))
        print(number_4)
        number_5=eval(input("pleas enter the number_5:" ))
        print(number_5)
        X1=(math.sin(math.radians((number_1)))+1)
        X2=(math.sin(math.radians((number_1)))+2)
        print(X1)
        print(X2)
        X=X1/X2
        print(X) 
        X3=(math.sin(math.radians((number_2)))+1)
        X4=(math.sin(math.radians((number_2)))+2)
        print(X3)
        print(X4)
        G=X3/X4
        print(G) 
        X5=(math.sin(math.radians((number_3)))+1)
        X6=(math.sin(math.radians((number_3)))+2)
        print(X5)
        print(X6)
        H=X5/X6
        print(H) 
        X7=(math.sin(math.radians((number_4)))+1)
        X8=(math.sin(math.radians((number_4)))+2)
        print(X7)
        print(X8)
        J=X7/X8
        print(J) 
        T=(G-X)/(number_2-number_1)
        print(f"b1 is {T} and b0 is {number_1}")
        T1=(H-G)/(number_3-number_2)
        b2=(T1-T)/(number_3-number_1)
        print(f"b0 is {number_1} and b1 is {T} and b2 is {b2}")
        total_2=number_1+T*(number_1-number_1)+b2*(number_1-number_1)(number_1-number_2)
        T2=(J-H)/(number_4-number_3)
        b3=(T2-T1)/(number_4-number_1)
        print(f"b0 is {number_1} and b1 is {T} and b2 is {b2} and b3 is {b3}")
        total_3=number_1+T*(number_1-number_1)+b2*(number_1-number_1)*(number_1-number_2)+b3*(number_1-number_1)*(number_1-number_2)*(number_1-number_3)
        error_3=(total_3-J)/total_3
        print(error_3)
else:
    print("ERROR")    