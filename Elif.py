ingreso_mensual = 10000
gasto_mensual= 6000

#if anidados y else-if (elif)

if ingreso_mensual >= 10000:
    if ingreso_mensual - gasto_mensual <0:
        print("estas en numeoros rojos")
    elif ingreso_mensual - gasto_mensual >3000:
         print("estas bien")
    else:
        print("gasta demasido")
    
elif ingreso_mensual >= 1000:
    print("estás regular")
    
elif ingreso_mensual >= 500:
    print("estás bien en latinoamérica")
    
elif ingreso_mensual >= 200:
    print("te da para chicles")
else:
    print("eres pobre")