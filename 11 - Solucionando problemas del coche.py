
on = input('¿Arranca?')
if on == "si":

    click= input('Suena un click click ')
    click.lower()
    if click=="si":
        print('Reemplaza la bateria ')
    else:
        not_run= input('¿Se enciende el coche pero no arranca? ')
        not_run.lower()
        if not_run== "si":
            print('Revisa las bujias ')
        else:
            run_calado = input('¿Arranca el coche y luego se cala? ')
            fuel_injecction = input('¿Tiene inyeccion de combustible? ')
            fuel_injecction.lower()
            if fuel_injecction == "si":
                print('Lleve el coche al taller ')
            else:
                print('Abre y cierra el starter' )
        
else :
    bornes_battery = input("Estan los bornes de la bateria corroidos? ")
    bornes_battery.lower()
    if bornes_battery=="si":
        print("Limpia los bornes y arranca de nuevo ")
    else:
        print('Reemplaza los cables y arranca de nuevo' )

