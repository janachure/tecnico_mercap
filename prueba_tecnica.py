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

	def __init__(self, duracion, horario, diaSemana):
		self.min = duracion ## cuanto duro
		self.hora = horario 
		self.dia = diaSemana 
		

	def sem(self):
		switcher = {1:"Lunes",2:"Martes",3:"Miercoles",4:"Jueves",5:"Viernes",6:"Sabado",7:"Domingo"}
		return switcher[self.dia]

## Clase de llamadas locales
class locales(llamadas):
	#horario expresado como un entero decimal de 4 digitos. 


	def __init__(self, duracion, horario, diaSemana): 
		super().__init__(duracion, horario, diaSemana)


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

	def show(self):
		print(f"Local, {self.min} min , Local , {super().sem()} , {self.hora} , {self.calculoConsumo()} ")

## Clase de llamadas nacional
class nacional(llamadas):
	def __init__(self, duracion, horario, diaSemana, localidad):
		super().__init__(duracion, horario, diaSemana)
		self.localidad = localidad


	def calculoConsumo(self):
		ans = self.min * LOCALIDADES[self.localidad]
		return ans

	def show(self):
		print(f"Nacional, {self.min} min , {self.localidad} , {super().sem()} , {self.hora} , {self.calculoConsumo()} ")

## Clase de llamadas exterior
class exterior(llamadas):
	def __init__(self, duracion, horario, diaSemana, pais):
		super().__init__(duracion, horario, diaSemana)
		self.pais = pais 


	def calculoConsumo(self):
		ans = self.min * PAISES[self.pais]
		return ans

	def show(self):
		print(f"Exterior, {self.min} min , {self.pais} , {super().sem()} , {self.hora} , {self.calculoConsumo()} ")

## Test muy chico.

a = facturacion(1410, 1400)
## Agrego una nacional.
b = nacional(10, 1930, 1, "Chascomus")
a.agregar_llamada(b)

## Agrego una del exterior.
c = exterior(10,1530,2,"Brasil")
a.agregar_llamada(c)

## Agrego una local.
d = locales(10, 700, 3) ## Duro 10 min, a las 19:30, el dia de la semana jueves.
a.agregar_llamada(d)
a.datosFactura()

