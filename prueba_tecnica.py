PAISES = {"Brasil": 0.2, "Alemania": 0.35, "Turquia": 0.30} # Paises de ejemplo 

LOCALIDADES = {"Chascomus": 0.20, "Mar del plata": 0.40, "Bariloche": 0.1} # localidades de ejemplo 


class facturacion:

	def __init__(self, idCliente, consumoMensual):
		self.mensualidad = consumoMensual
		self.id = idCliente
		self.llamadas = []
	# Generador
	def agregar_llamada(self, llamada):
		(self.llamadas).append(llamada)
	# como enseñarlo por pantalla
	def datosFactura(self):
		print("\nTipoLlamada, Duracion, Destino, Dia, Hora, Consumo:\n" )
		ans = 0
		for call in self.llamadas:
			call.show()
			ans += call.calculoConsumo()
		print(f"El consumo de este mes en llamadas es {ans} y la mensualidad {self.mensualidad}\n")
		print(f"Total factura {ans+self.mensualidad}")


class llamadas:
	DIAS_HABILES = 5
	INICIO_RANGO = 800
	FIN_RANGO = 2000

	def __init__(self, duracion):
		self.min = duracion ## cuanto duro
		

class locales(llamadas):
	#horario expresado como un entero decimal de 4 digitos. 


	def __init__(self, duracion, horario, diaSemana): 
		super().__init__(duracion)
		self.hora = horario 
		self.dia = diaSemana 

	def calculoConsumo(self):
		ans = 0
		if (self.dia <= llamadas.DIAS_HABILES):
			if( llamadas.INICIO_RANGO <= self.hora <=llamadas.FIN_RANGO):
				ans += self.min * 0.20
			else:
				ans += self.min * 0.10
		else:
			ans += self.min * 0.10

		return ans

	def sem(self):
		switcher = {1:"Lunes",2:"Martes",3:"Miercoles",4:"Jueves",5:"Viernes",6:"Sabado",7:"Domingo"}
		return switcher[self.dia]


	def show(self):
		print(f"Local, {self.min}, Local , {self.sem()}, {self.hora}, {self.calculoConsumo()} ")

class nacional(llamadas):
	def __init__(self, duracion, localidad):
		super().__init__(duracion)
		self.localidad = localidad

	def calculoConsumo(self):
		ans = self.min * LOCALIDADES[self.localidad]
		return ans

	def show(self):
		print(f"Nacional, {self.min}, {self.localidad}, NA , NA , {self.calculoConsumo()} ")

class exterior(llamadas):
	def __init__(self, duracion, pais):
		super().__init__(duracion)
		self.pais = pais 


	def calculoConsumo(self):
		ans = self.min * PAISES[self.pais]
		return ans

	def show(self):
		print(f"Exterior, {self.min}, {self.pais}, NA , NA , {self.calculoConsumo()} ")

