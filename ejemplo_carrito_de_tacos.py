def muestra():
    entrada = None
    menu = {}
    transacciones = []
    vendidos = 0
    ingresos = 0
    print("Surtir tacos")
    while True:
        entrada = int(input("""
        1 = Pastor
        2 = Bistek
        3 = Chorizo
        4 = Salir

        """))
        if entrada == 4:
            break
        else:
            cantidad = int(input("""
        Cantidad: """))
            precio = float(input("""
        Precio: """))
            if entrada == 1:
                if "Pastor" in menu:              
                    menu['Pastor']['Cantidad'] = menu['Pastor']['Cantidad'] + cantidad
                else:
                    menu['Pastor'] = {}
                    menu["Pastor"]['Cantidad'] = cantidad
                    menu["Pastor"]['Precio'] = precio
            elif entrada == 2:
                if "Bistek" in menu:
                    menu['Bistek']['Cantidad'] = menu['Bistek']['Cantidad'] + cantidad
                else:
                    menu['Bistek'] = {}
                    menu['Bistek']['Cantidad'] = cantidad
                    menu["Bistek"]['Precio'] = precio
            else:
                if "Chorizo" in menu:
                    menu['Chorizo']['Cantidad'] = menu['Chorizo']['Cantidad'] + cantidad
                else:
                    menu['Chorizo'] = {}
                    menu["Chorizo"]['Cantidad'] = cantidad
                    menu['Chorizo']['Precio'] = precio

    print("\nHora de vender tacos")

    while True:
        entrada = int(input("""
        1 = Pastor
        2 = Bistek
        3 = Chorizo
        4 = Salir

        """))
        if entrada == 4:
            print(f"""
        Transacciones: {transacciones}, Ingresos: {ingresos}, Vendidos: {vendidos}
            """)
            break
        else:
            cantidad = int(input("""
        Cantidad: """))
            if entrada == 1:
                if menu['Pastor']['Cantidad'] < cantidad:
                    total_vendidos = menu['Pastor']['Cantidad']
                    total_ingresos = total_vendidos * menu['Pastor']['Precio']
                    transacciones.append({"Tipo": "Pastor", "Cantidad": total_vendidos, "Ingresos": total_ingresos})
                    menu['Pastor']['Cantidad'] = 0
                    print("\nYa no hay tacos al pastor")
                else:
                    total_vendidos = cantidad
                    total_ingresos = total_vendidos * menu['Pastor']['Precio']
                    transacciones.append({"Tipo": "Pastor", "Cantidad": total_vendidos, "Ingresos": total_ingresos})
                    menu['Pastor']['Cantidad'] = menu['Pastor']['Cantidad'] - cantidad
            elif entrada == 2:
                if menu['Bistek']['Cantidad'] < cantidad:
                    total_vendidos = menu['Bistek']['Cantidad']
                    total_ingresos = total_vendidos * menu['Bistek']['Precio']
                    transacciones.append({"Tipo": "Bistek", "Cantidad": total_vendidos, "Ingresos": total_ingresos})
                    menu['Bistek']['Cantidad'] = 0
                    print("\nYa no hay tacos de Bistek")
                else:
                    total_vendidos = cantidad
                    total_ingresos = total_vendidos * menu['Bistek']['Precio']
                    transacciones.append({"Tipo": "Bistek", "Cantidad": total_vendidos, "Ingresos": total_ingresos})
                    menu['Bistek']['Cantidad'] = menu['Bistek']['Cantidad'] - cantidad
            elif entrada == 3:
                if menu['Chorizo']['Cantidad'] < cantidad:
                    total_vendidos = menu['Chorizo']['Cantidad']
                    total_ingresos = total_vendidos * menu['Chorizo']['Precio']
                    transacciones.append({"Tipo": "Chorizo", "Cantidad": total_vendidos, "Ingresos": total_ingresos})
                    menu['Chorizo']['Cantidad'] = 0
                    print("\nYa no hay tacos de Chorizo")
                else:
                    total_vendidos = cantidad
                    total_ingresos = total_vendidos * menu['Chorizo']['Precio']
                    transacciones.append({"Tipo": "Chorizo", "Cantidad": total_vendidos, "Ingresos": total_ingresos})
                    menu['Chorizo']['Cantidad'] = menu['Chorizo']['Cantidad'] - cantidad
            ingresos = ingresos + total_ingresos
            vendidos = vendidos + total_vendidos