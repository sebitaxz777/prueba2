import prueba2 as p

lista_reservas = []
opcion = 0
while opcion != 6:
    p.mostrar_menu()
    opcion = p.seleccionar_opcion()
    if opcion == 1:
        p.agregar_reserva(lista_reservas)
    elif opcion == 2:
        nombre = input("ingrese el nombre del huesped a buscar:   ")
        pos = p.buscar_reservas(lista_reservas, nombre)
        if pos != -1:
            print("********** RESERVA **********")
            print(f"nombre del huesped: {lista_reservas[pos]["huesped"]}")
            print(f"numero de habitacion: {lista_reservas[pos]["habitacion"]}")
            print(f"cantidad de noches: {lista_reservas[pos]["noches"]}")
            estado = "CONFIRMADA" if lista_reservas[pos]["confirmada"] else "PENDIENTE"
            print(f"estado: {estado}")
            print("********************")
        else:
            print(f"el huesped ' {nombre}' no han sido encontrado")

    elif opcion == 3:
        nombre = input("ingrese el nombre del huesped a eliminar de reserva:   ")
        pos = p.buscar_reserva(lista_reservas, nombre)
        if pos != -1:
            lista_reservas.pop(pos)
            print("su reserva fue eliminada")
        else:
             print(f"el huesped ' {nombre}' no han sido encontrado")
    elif opcion == 4:
        p.confirmar_reservas(lista_reservas)
        print("su reserva fue actualizada")
    elif opcion == 5:
        p.confirmar_reservas(lista_reservas)
        p.mostrar_reservas(lista_reservas)
    elif opcion == 6:
        print("GRACIAS POR USAR EL SISTEMA,QUE TENGA BUEN DIA")

    
