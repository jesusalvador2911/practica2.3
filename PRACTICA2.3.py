import random
#Empieo declarando varaiables que utilizare en un futuro
#Los grupos los he separado de la A a la F
#Y EN SEGUIDA HE PUESTO SUS DESCUENTOS CORRRESPONDIENTES
A = (0)
Ades = (.30)
B = (0)
Bdes = (.10)
C = (0)
Cdes = (.15)
D = (0)
Ddes = (.25)
F = (0)
Fdes = (.35)
#Despues definimos el contador de nuestro ciclo
asistente = (0)
#Y el gurpo de elecciones que tendra 
categorias = [1,2,3,4,5,6]
#Definimos el precio de los boletos
precio = (200)
#Y las varaibales para cada uan de las recaudaciones
recaudacion = (0)
recaudacion_des = (0)
#Nuestro ciclo ira desde el 0 al 10000
while asistente < 1000000:
    #Se seleccianara alaeatoriamente una de las opciones y caso de se hara lo siguiente:
    asistencia = random.choice(categorias)
    if asistencia == 1:
        #Se suamara 1 a la catageoria elegida
        A = (A+1)
        #Se sumara uno mas a la cantidad de asistente, esto hara avanzar nuestro ciclo
        asistente = (asistente+1)
        #cada categoria tiene un descuento, se contabilizara las ganancias con este desvuento y las ganancias sin el mismo
        precio_des = (precio-(precio*Ades))
        recaudacion = (recaudacion+precio)
        recaudacion_des = (precio_des + recaudacion_des)

    elif asistencia == 2:
        B = (B+1)
        asistente = (asistente+1)
        precio_des = (precio-(precio*Bdes))
        recaudacion = (recaudacion+precio)
        recaudacion_des = (precio_des + recaudacion_des)
    elif asistencia == 3:
        C = (C+1)
        asistente = (asistente+1)
        precio_des = (precio-(precio*Cdes))
        recaudacion = (recaudacion+precio)
        recaudacion_des = (precio_des + recaudacion_des)
    elif asistencia == 4:
        D = (D+1)
        asistente = (asistente+1)
        precio_des = (precio-(precio*Cdes))
        recaudacion = (recaudacion+precio)
        recaudacion_des = (precio_des + recaudacion_des)
    elif asistencia == 5:
        F = (F+1)
        asistente = (asistente+1)
        precio_des = (precio-(precio*Fdes))
        recaudacion = (recaudacion+precio)
        recaudacion_des = (precio_des + recaudacion_des)
#Una vez termiando el ciclo se mostararn lso resultados
print("En el evento se ha recuadado un total de: ", recaudacion_des, " de pesos" )
print("Usted ha tenido perdidas por los descuentos de un total de: ", (recaudacion-recaudacion_des), "de pesos")
#Para sacar el porcentaje utilizaremos una regla de 3 simple
print("Que se contabiliza como perdiadas del :",((recaudacion_des*100)/recaudacion)," %")
print("Usted pudo haber recibido sin los descuentos un total de: ", recaudacion, "de pesos")
print(" ")
print("TOTAL DE ASISTENTES ",(asistente), " personas")

#A_porc = ((A*100)/asistente)
#Luego utilizaremos una funcion para cada una de las barras, que incluye una serie de decisisones que sera definida por otra regla de 3 para simular la barra de porcentaje
def A_porc():
    A_porc = ((A*100)/asistente)
    if A_porc >= 100:
        print("5-14 *********", (A_porc), " %")
    elif A_porc >= 90:
        print("5-14 *********", (A_porc), " %")
    elif A_porc >= 80:
        print("5-14 ********", (A_porc), " %")
    elif A_porc >= 70:
        print("5-14 *******", (A_porc), " %")
    elif A_porc >= 60:
        print("5-14 ******", (A_porc), " %")
    elif A_porc >= 50:
        print("5-14 *****", (A_porc), " %")
    elif A_porc >= 40:
        print("5-14 ****", (A_porc), " %")
    elif A_porc >= 30:
        print("5-14 ***", (A_porc), " %")
    elif A_porc >= 20:
        print("5-14 **", (A_porc), " %")
    elif A_porc >= 10:
        print("5-14 *", (A_porc), " %")
A_porc()
def B_porc():
    B_porc = ((B*100)/asistente)

    if B_porc >= 100:
        print("15-19 *********", (B_porc), " %")
    elif B_porc >= 90:
        print("15-19 *********", (B_porc), " %")
    elif B_porc >= 80:
        print("15-19 ********", (B_porc), " %")
    elif B_porc >= 70:
        print("15-19 *******", (B_porc), " %")
    elif B_porc >= 60:
        print("15-19 ******", (B_porc), " %")
    elif B_porc >= 50:
        print("15-19 *****", (B_porc), " %")
    elif B_porc >= 40:
        print("15-19 ****", (B_porc), " %")
    elif B_porc >= 30:
        print("15-19 ***", (B_porc), " %")
    elif B_porc >= 20:
        print("15-19 **", (B_porc), " %")
    elif B_porc >= 10:
        print("15-19 *", (B_porc), " %")
B_porc()

def C_porc():
    C_porc = ((C*100)/asistente)

    if C_porc >= 100:
        print("20-45 *********", (C_porc), " %")
    elif C_porc >= 90:
        print("20-45 *********", (C_porc), " %")
    elif C_porc >= 80:
        print("20-45 ********", (C_porc), " %")
    elif C_porc >= 70:
        print("20-45 *******", (C_porc), " %")
    elif C_porc >= 60:
        print("20-45 ******", (C_porc), " %")
    elif C_porc >= 50:
        print("20-45 *****", (C_porc), " %")
    elif C_porc >= 40:
        print("20-45 ****", (C_porc), " %")
    elif C_porc >= 30:
        print("20-45 ***", (C_porc), " %")
    elif C_porc >= 20:
        print("20-45 **", (C_porc), " %")
    elif C_porc >= 10:
        print("20-45 *", (C_porc), " %")
C_porc()

def D_porc():

    D_porc = ((D*100)/asistente)

    if D_porc >= 100:
        print("46-65 *********", (D_porc), " %")
    elif D_porc >= 90:
        print("46-65 *********", (D_porc), " %")
    elif D_porc >= 80:
        print("46-65 ********", (D_porc), " %")
    elif D_porc >= 70:
        print("46-65 *******", (D_porc), " %")
    elif D_porc >= 60:
        print("46-65 ******", (D_porc), " %")
    elif D_porc >= 50:
        print("46-65 *****", (D_porc), " %")
    elif D_porc >= 40:
        print("46-65 ****", (D_porc), " %")
    elif D_porc >= 30:
        print("46-65 ***", (D_porc), " %")
    elif D_porc >= 20:
        print("46-65 **", (D_porc), " %")
    elif D_porc >= 10:
        print("46-65 *", (D_porc), " %")
D_porc()

def F_porc():
    F_porc = ((F*100)/asistente)

    if F_porc >= 100:
        print("46-65 *********", (F_porc), " %")
    elif F_porc >= 90:
        print("46-65 *********", (F_porc), " %")
    elif F_porc >= 80:
        print("46-65 ********", (F_porc), " %")
    elif F_porc >= 70:
        print("46-65 *******", (F_porc), " %")
    elif F_porc >= 60:
        print("46-65 ******", (F_porc), " %")
    elif F_porc >= 50:
        print("46-65 *****", (F_porc), " %")
    elif F_porc >= 40:
        print("46-65 ****", (F_porc), " %")
    elif F_porc >= 30:
        print("46-65 ***", (F_porc), " %")
    elif F_porc >= 20:
        print("46-65 **", (F_porc), " %")
    elif F_porc >= 10:
        print("46-65 *", (F_porc), " %")
F_porc()
    

    