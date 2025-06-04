# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	opcion = int()
	subopcion = int()
	opcionarea = int()
	opcioncamilla = int()
	nombre = str()
	apellidop = str()
	apellidom = str()
	idpaciente = str()
	area = str()
	camilla = str()
	pacientes = [[str() for ind0 in range(6)] for ind1 in range(100)]
	contador = 1
	while True:
		print("")
		print("MENU PRINCIPAL")
		print("1. registrar pacientes")
		print("2. ver pacientes ya registrados")
		print("3. salir")
		print("seleccione una opcion: ")
		opcion = int(input())
		if opcion==1:
			print("ingrese nombre del paciente: ")
			nombre = input()
			print("ingrese apellido paterno: ")
			apellidop = input()
			print("ingrese apellido materno:")
			apellidom = input()
			idpaciente = "P"+str(contador)
			print("seleccione un area medica:")
			print("1. urgencia")
			print("2. hospitalizacion")
			print("3. cuidados intensivos")
			print("4. pediatria")
			print("5. fisioterapia")
			print("6. radiologia")
			print("7. neurologia")
			print("8. medico familiar")
			opcionarea = int(input())
			if opcionarea==1:
				area = "urgencia"
			elif opcionarea==2:
				area = "hospitalizacion"
			elif opcionarea==3:
				area = "cuidados intensivos"
			elif opcionarea==4:
				area = "pediatria"
			elif opcionarea==5:
				area = "fisioterapia"
			elif opcionarea==6:
				area = "radiologia"
			elif opcionarea==7:
				area = "neurologia"
			elif opcionarea==8:
				area = "medico familiar"
			else:
				area = "area desconocida"
			print("Seleccione una camilla (1 a 10):")
			opcioncamilla = int(input())
			camilla = "C"+str(opcioncamilla)
			pacientes[contador-1][0] = idpaciente
			pacientes[contador-1][1] = nombre
			pacientes[contador-1][2] = apellidop
			pacientes[contador-1][3] = apellidom
			pacientes[contador-1][4] = area
			pacientes[contador-1][5] = camilla
			print("paciente registrado exitosamente con ID ",idpaciente)
			contador = contador+1
		elif opcion==2:
			print("")
			print("LISTA DE PACIENTES:")
			for i in range(1,contador):
				print("ID: ",pacientes[i-1][0])
				print("nombre: ",pacientes[i-1][1]," ",pacientes[i-1][2]," ",pacientes[i-1][3])
				print("area: ",pacientes[i-1][4])
				print("camilla: ",pacientes[i-1][5])
		elif opcion==3:
			print("salir del sistema...")
		else:
			print("la opcion no es validad")
		if opcion==3: break