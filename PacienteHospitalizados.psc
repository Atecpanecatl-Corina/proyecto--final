Algoritmo sin_titulo
	Definir opcion, subopcion, opcionArea, opcionCamilla Como Entero
    Definir nombre, apellidoP, apellidoM, idPaciente, area, camilla Como Cadena
	
    Dimension pacientes[100, 6]
    contador <- 1
	
    Repetir
        Escribir ""
        Escribir "MENU PRINCIPAL"
        Escribir "1. registrar pacientes"
        Escribir "2. ver pacientes ya registrados"
        Escribir "3. salir"
        Escribir "seleccione una opcion: "
        Leer opcion
		
        Segun opcion Hacer
            1: 
                Escribir "ingrese nombre del paciente: "
                Leer nombre
                Escribir "ingrese apellido paterno: "
                Leer apellidoP
                Escribir "ingrese apellido materno:"
                Leer apellidoM
                idPaciente <- "P" + ConvertirATexto(contador)
				
                Escribir "seleccione un area medica:"
                Escribir "1. urgencia"
                Escribir "2. hospitalizacion"
                Escribir "3. cuidados intensivos"
                Escribir "4. pediatria"
                Escribir "5. fisioterapia"
                Escribir "6. radiologia"
                Escribir "7. neurologia"
                Escribir "8. medico familiar"
                Leer opcionArea
				
                Segun opcionArea Hacer
                    1: area <- "urgencia"
                    2: area <- "hospitalizacion"
                    3: area <- "cuidados intensivos"
                    4: area <- "pediatría"
                    5: area <- "fisioterapia"
                    6: area <- "radiologia"
                    7: area <- "neurologia"
                    8: area <- "medico familiar"
                    De Otro Modo:
                        area <- "area desconocida"
                FinSegun
				
                Escribir "Seleccione una camilla (1 a 10):"
                Leer opcionCamilla
                camilla <- "C" + ConvertirATexto(opcionCamilla)
				
                pacientes[contador, 1] <- idPaciente
                pacientes[contador, 2] <- nombre
                pacientes[contador, 3] <- apellidoP
                pacientes[contador, 4] <- apellidoM
                pacientes[contador, 5] <- area
                pacientes[contador, 6] <- camilla
				
                Escribir "paciente registrado exitosamente con ID ", idPaciente
                contador <- contador + 1
				
            2:
                Escribir ""
                Escribir "LISTA DE PACIENTES:"
                Para i <- 1 Hasta contador - 1 Con Paso 1
                    Escribir "ID: ", pacientes[i,1] 
					Escribir "nombre: ", pacientes[i,2], " ", pacientes[i,3], " ", pacientes[i,4] 
					Escribir "area: ", pacientes[i,5]
					Escribir "camilla: ", pacientes[i,6]
                FinPara
				
            3:
                Escribir "salir del sistema..."
				
            De Otro Modo:
                Escribir "la opcion no es validad"
        FinSegun
		
    Hasta Que opcion = 3
FinAlgoritmo
