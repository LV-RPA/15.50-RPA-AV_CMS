import datetime
import os 
import glob

desde = datetime.datetime.now() + datetime.timedelta(days=-30)
hasta = datetime.datetime.now()
user_cms = "ADELAC13" 
pass_cms = "Abel02202" 
user_inguz = ("74590179")
pass_inguz = ("jarvis")
link_inguz = ("www.anovo.pe/inguz")
link_carga = ("http://www.anovo.pe/inguz/formRutinas/frmCargarOrdenes.aspx")
ruta = (r'\\10.120.15.50\cmsFiles')
delete_files = r'del /S /Q C:\cmsFiles\*'

print("cerrar procesos")
os.system('taskkill /f /im cms.exe')
os.system('taskkill /f /im te_envot.exe')
os.system('taskkill /f /im te_alav.exe')
os.system('taskkill /f /im te_manot.exe')
os.system('taskkill /f /im te_rreot.exe')
os.system('taskkill /f /im firefox.exe')
sleep(2)

print("Eliminar Archivos")
os.system(delete_files)
sleep(2)

print("Abrir CMS")
App.open("C:\\Gescab\\cms.exe")
sleep(10)
wait(Pattern("1555385646469.png").similar(0.80),1800)
sleep(2)

print("modulo encontrado")
paste("1555191515556.png", user_cms)
sleep(2)
type(Key.TAB)
sleep(2)
paste(pass_cms)
sleep(2)
type(Key.ENTER)

wait(Pattern("1555191558075-1.png").similar(0.80),1800)
sleep(2)
type(Key.ENTER)
sleep(2)
click("1555191587121-1.png")
sleep(2)
click(Pattern("1555191605081-1.png").targetOffset(6,11))
sleep(2)
click("1555191630786-1.png")
sleep(2)
wait(Pattern("1555191646245-1.png").similar(0.80),1800)
sleep(2)

print("listo, cable mágico")
def cambiarusuario():
    type("u",KEY_ALT)
    sleep(1)
    type("s",KEY_ALT)
    sleep(1)

cambiarusuario()
cambiarusuario()
cambiarusuario()
cambiarusuario()
cambiarusuario()
sleep(10)

print("buscar modulo")
doubleClick(Pattern("1555191664304.png").targetOffset(-68,2))
sleep(10)
click(Pattern("1555191664304.png").targetOffset(-68,2))
sleep(2)
wait("1555191780299.png")
sleep(2)

#//********************INSTALACIONES***********
click(Pattern("1560186290181-1.png").targetOffset(-55,1))
sleep(2)
click(Pattern("1560186366857-1.png").targetOffset(-114,0))
sleep(2)
doubleClick(Pattern("1560186406961-1.png").targetOffset(-61,0))
sleep(2)
wait(Pattern("1560186482437-1.png").similar(0.80),240)
sleep(2)
click(Pattern("1560186482437-1.png").targetOffset(-24,-7))
sleep(2)
type(Pattern("1560186572236-1.png").targetOffset(24,2), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1560186615354-1.png").targetOffset(23,1), hasta.strftime("%d%m%Y"))
sleep(1)
click(Pattern("1560186698802-1.png").targetOffset(28,0))
sleep(2)
click(Pattern("1560186767973-1.png").similar(0.90).targetOffset(11,10))
sleep(2)
click(Pattern("1560186857769-1.png").similar(0.90).targetOffset(11,19))
sleep(2)
click(Pattern("1560186927069-1.png").targetOffset(-3,-2))
sleep(2)
wait(Pattern("1560980283215.png").similar(0.80),480)
sleep(2)
click(Pattern("1560187071422-1.png").targetOffset(-2,-4))
sleep(5)
click(Pattern("1578071124583.png").targetOffset(-1,2))
sleep(2)
click(Pattern("1578071175207.png").targetOffset(123,1))
sleep(2)

print("selecciona la carpeta")
click(Pattern("1578071221172.png").targetOffset(-88,2))
sleep(2)
type(Pattern("1560187180972-1.png").targetOffset(34,3), "instalaciones")
sleep(2)
type(Key.ENTER)
sleep(5)
wait(Pattern("1560980383658.png").similar(0.80),3600)
sleep(3)
type(Key.ENTER)
sleep(2)
click(Pattern("1560187286377-1.png").targetOffset(5,-8))
sleep(2)

#//********************ALTAS***********
doubleClick(Pattern("1578590795688-1.png").targetOffset(-78,0))
sleep(2)
wait(Pattern("1560186482437-2.png").similar(0.80),240)
sleep(2)
click(Pattern("1560186482437-2.png").targetOffset(-24,-7))
sleep(2)
type(Pattern("1560186572236-2.png").targetOffset(24,2), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1560186615354-2.png").targetOffset(23,1), hasta.strftime("%d%m%Y"))
sleep(2)
click(Pattern("1578591026151-1.png").targetOffset(21,-1))
sleep(2)
click(Pattern("1578591057259-1.png").targetOffset(25,8))
sleep(8)
click(Pattern("1560186698802-2.png").targetOffset(28,0))
sleep(2)
click(Pattern("1578591161962-1.png").similar(0.90).targetOffset(-43,9))
sleep(2)
click(Pattern("1578591193991-1.png").similar(0.90).targetOffset(-45,20))
sleep(2)
click(Pattern("1560186927069-2.png").targetOffset(-3,-2))
sleep(2)
wait(Pattern("1560980283215-2.png").similar(0.80),480)
sleep(2)
click(Pattern("1560187071422-2.png").targetOffset(-2,-4))
sleep(5)
click(Pattern("1578071124583-1.png").targetOffset(-1,2))
sleep(2)
click(Pattern("1578071175207-1.png").targetOffset(123,1))
sleep(2)

print("selecciona la carpeta")
click(Pattern("1578071221172-1.png").targetOffset(-88,2))
sleep(2)
type(Pattern("1560187180972-2.png").targetOffset(34,3), "filealtas")
sleep(2)
type(Key.ENTER)
sleep(5)
wait(Pattern("1560980383658-2.png").similar(0.80),3600)
sleep(3)
type(Key.ENTER)
sleep(2)
click(Pattern("1560187286377-2.png").targetOffset(5,-8))
sleep(2)

#//********************MANTENIMIENTO***********
doubleClick(Pattern("1560187366756-1.png").targetOffset(-64,1))
sleep(2)
wait(Pattern("1560187472904-1.png").similar(0.80),3600)
sleep(2)
click(Pattern("1560187472904-1.png").targetOffset(-10,-7))
sleep(2)
type(Pattern("1560187520847-1.png").similar(0.80).targetOffset(22,0), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1560187549018-1.png").similar(0.80).targetOffset(21,1), hasta.strftime("%d%m%Y"))
sleep(2)
click(Pattern("1560187620366-1.png").exact().targetOffset(-1,10))
sleep(2)
click(Pattern("1560187733905-1.png").targetOffset(4,20))
sleep(2)
click(Pattern("1560187775113-1.png").targetOffset(-3,-1))
sleep(2)
wait(Pattern("1560980283215-1.png").similar(0.80),480)
sleep(2)
click(Pattern("1560187852165-1.png").targetOffset(-4,-4))
sleep(5)
click(Pattern("1563400573094-1.png").targetOffset(2,0))
sleep(2)
click(Pattern("1563400598823-1.png").targetOffset(120,2))
sleep(2)

print("selecciona la carpeta")
click(Pattern("1577140117368.png").targetOffset(-87,1))
sleep(2)
type(Pattern("1560187888962-1.png").targetOffset(37,1), "mantenimiento")
sleep(2)
type(Key.ENTER)
sleep(5)
wait(Pattern("1560980383658-1.png").similar(0.80),1800)
sleep(3)
type(Key.ENTER)
sleep(2)
click(Pattern("1560187969347-1.png").targetOffset(5,-10))
sleep(2)

print("cerrar CMS")
click(Pattern("1555389366717-3.png").targetOffset(110,2))
sleep(2)
wait(Pattern("1555389401450-3.png").similar(0.80),600)
sleep(2)
click(Pattern("1555389401450-3.png").targetOffset(25,52))
sleep(5)

#*********************ABRIR FIREFOX********************#
print("abrir Firefox")
App.open("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
sleep(20)

print("Nos logueamos")
paste(user_inguz)
sleep(3)
type(Key.TAB)
sleep(3)
paste(pass_inguz)
sleep(2)
type(Key.ENTER)
sleep(5)
wait("1571943413464.png",120)
sleep(2)

print("ingresar el link de carga")
type("l",KEY_CTRL)
sleep(2)
paste(link_carga)
sleep(2)
type(Key.ENTER)

print("listo - Modulo de carga")
sleep(15)
click("1557348730358-6.png")
sleep(5)

print("carga instalaciones")
click(Pattern("1569699437620.png").targetOffset(-130,33))
sleep(5)
type("l",KEY_CTRL)
sleep(2)
paste(ruta)
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("1567727129961.png").targetOffset(-35,1))
sleep(2)
type(Key.ENTER)
sleep(3)

print("Listo para importar en el INGUZ")
click(Pattern("1559244690937-3.png").targetOffset(4,2))
sleep(2)
wait(Pattern("1560193987932-1.png").similar(0.80),120)
sleep(2)

print("carga altas")
type("l",KEY_CTRL)
sleep(2)
paste(link_carga)
sleep(2)
type(Key.ENTER)

print("listo - Modulo de carga")
sleep(15)
click("1557348730358-6.png")
sleep(5)

print("carga instalaciones")
click(Pattern("1569699437620.png").targetOffset(-130,33))
sleep(5)
type("l",KEY_CTRL)
sleep(2)
paste(ruta)
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("1578596969471.png").targetOffset(-35,1))
sleep(2)
type(Key.ENTER)
sleep(3)

print("Listo para importar en el INGUZ")
click(Pattern("1559244690937-3.png").targetOffset(4,2))
sleep(2)
wait(Pattern("1560193987932-1.png").similar(0.80),120)
sleep(2)

print("carga mantenimiento")
type("l",KEY_CTRL)
sleep(2)
paste(link_carga)
sleep(1)
type(Key.ENTER)
sleep(5)
click(Pattern("1564185361109.png").targetOffset(36,3))
sleep(1)

print("carga mantenimiento")
click(Pattern("1569686605606.png").similar(0.80).targetOffset(-135,-13))
sleep(5)
type("l",KEY_CTRL)
sleep(2)
paste(ruta)
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("1567727193830.png").targetOffset(-43,-1))
sleep(2)
type(Key.ENTER)
sleep(3)
click(Pattern("1559244755557-3.png").similar(0.80).targetOffset(6,2))
sleep(2)
wait(Pattern("1560194024555-1.png").similar(0.80),120)

print("fin del RPA rutinas")
sleep(3)
type("w",KEY_CTRL)
sleep(3)