Piezas= int(input("ingrese el numero de piezas a comprar"))
Precio= float(input("ingrese el precio unitario de la pieza"))
Montototal= Piezas * Precio
if Montototal > 500000:
    Inversion= (Montototal * 0.55)
    Prestamo= (Montototal * 0.30)
    Credito= (Montototal - Inversion - Prestamo)
    Intereses= (Credito * 0.20)
    print("El monto total de la compra es:",Montototal)
    print("La inversión de la empresa es: ", Inversion)
    print("El préstamo al banco es: ", Prestamo)
    print("El crédito al fabricante es: ", Credito + Intereses)
else:
    Inversion= (Montototal * 0.70)
    Credito= (Montototal - Inversion)
    Intereses= (Credito * 0.20)
    print("El monto total de la compra es: ", Montototal)
    print("La inversión de la empresa es: ", Inversion)
    print("El préstamo al banco es: ", 0)
    print("El crédito al fabricante es: ", Credito + Intereses)
    