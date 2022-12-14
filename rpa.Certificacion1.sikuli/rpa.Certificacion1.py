import datetime
import os 
import glob

desde = datetime.datetime.now() + datetime.timedelta(days=-3)
hasta = datetime.datetime.now()
user_cms = "ADELAC13" 
pass_cms = "Abel02202" 
user_inguz = "74590179"
pass_inguz = "jarvis"
link_inguz = "http://www.anovo.pe/inguz"
link_carga = "http://www.anovo.pe/inguz/formRutinas/frmCargaCertificacion.aspx"
rutinas = r'\\10.120.15.50\cmsFiles\rutinas'
averias = r'\\10.120.15.50\cmsFiles\averias'
altas = r'\\10.120.15.50\cmsFiles\altas'
altas2 = r'\\10.120.15.50\cmsFiles2\altas'
componentes_lima = r'\\10.120.15.50\cmsFiles\componentes_lim_det'
contrata445 = r'\\10.120.15.50\cmsFiles\contrata445'
componentes445_lim_det = r'\\10.120.15.50\cmsFiles\componentes445_lim_det'
altas_are = r'\\10.120.15.50\cmsFiles\altas_are'
altas_are2 = r'\\10.120.15.50\cmsFiles2\altas_are'
componentes_are_det = r'\\10.120.15.50\cmsFiles\componentes_are_det'
componentes_are_det2 = r'\\10.120.15.50\cmsFiles2\componentes_are_det'
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

wait(Pattern("1555191558075.png").similar(0.80),1800)
sleep(2)
type(Key.ENTER)
sleep(2)
click("1555191587121.png")
sleep(2)
click(Pattern("1555191605081.png").targetOffset(6,11))
sleep(2)
click("1555191630786.png")
sleep(2)
wait(Pattern("1555191646245.png").similar(0.80),1800)
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

print("abrir modulo")
doubleClick(Pattern("1555191664304.png").targetOffset(-68,2))
sleep(10)
click(Pattern("1555191664304.png").targetOffset(-68,2))
sleep(2)
wait(Pattern("1555191780299.png").similar(0.80),120)
sleep(2)
print("salio en proceso")
click(Pattern("1555191795518.png").targetOffset(-59,0))
sleep(2)
click(Pattern("1555191829565.png").targetOffset(-113,0))
sleep(2)

print("inicio exportar rutinas")
doubleClick(Pattern("1555191865361.png").targetOffset(-82,1))
sleep(2)
wait(Pattern("1558198815444.png").similar(0.80),120)
click(Pattern("1558198815444.png").targetOffset(17,-20))
sleep(2)
type(Pattern("1555185386377-1.png").targetOffset(20,0), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1555185427297-1.png").targetOffset(19,0), hasta.strftime("%d%m%Y"))
sleep(2)

print("ingresaron las fechas")
click(Pattern("1555185513046.png").targetOffset(43,-2))
sleep(2)
click(Pattern("1555185564402.png").targetOffset(3,8))
sleep(2)
print("selecciona liquidación")
sleep(3)
type(Pattern("1555190912611.png").targetOffset(-1,-4), "333")

print("Ingresa la contrata")
sleep(2)
click(Pattern("1555185700153.png").targetOffset(-4,-1))
sleep(3)
click(Pattern("1572386647144.png").targetOffset(-2,-27))
sleep(2)
click(Pattern("1555187030635.png").targetOffset(-2,-1))
sleep(2)

print("listo para exportar rutinas")
click("1555185858713.png")
wait(Pattern("1556122391965.png").similar(0.80),1800)
sleep(2)

print("Data Lista")
click("1555186118138.png")
sleep(2)
click("1555186135652.png")
sleep(2)
click(Pattern("1555452968577.png").targetOffset(122,0))
sleep(2)
click(Pattern("1555356997978.png").targetOffset(-4,0))
sleep(2)
doubleClick("1555357292814.png")
sleep(2)
type(Pattern("1555186343019.png").targetOffset(-2,0), "rutinas")
sleep(2)
click("1555186584481.png")

print("guardamos el archivo rutinas")
sleep(5)
click("1555186711113.png")
sleep(2)
click(Pattern("1555186639167.png").targetOffset(0,-2))
sleep(2)

print("inicio exportar altas")

doubleClick(Pattern("1555191865361.png").targetOffset(-82,1))
wait(Pattern("1558198815444.png").similar(0.80),3600)
sleep(2)
click(Pattern("1558198815444.png").targetOffset(17,-20))
sleep(2)
type(Pattern("1555185386377-1.png").targetOffset(20,0), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1555185427297-1.png").targetOffset(19,0), hasta.strftime("%d%m%Y"))
sleep(2)
print("ingresaron las fechas")
click(Pattern("1555185513046.png").targetOffset(43,-2))
sleep(2)
click(Pattern("1555185564402.png").targetOffset(3,8))
sleep(2)
print("selecciona liquidación")
sleep(2)
click(Pattern("1555192475837.png").targetOffset(11,1))
sleep(2)
click(Pattern("1555192543295.png").targetOffset(16,2))
sleep(3)
type(Pattern("1555190912611.png").targetOffset(-1,-4), "333")
sleep(3)

print("Ingresa la contrata")
click(Pattern("1555185700153.png").targetOffset(-4,-1))
sleep(3)
click(Pattern("1555192730228.png").targetOffset(-5,-4))
sleep(2)
click("1555192808973.png")
sleep(3)

print("listo para exportar altas")
click("1555185858713.png")
sleep(2)
wait(Pattern("1556122962824.png").similar(0.80),3600)
sleep(2)
click(Pattern("1555193051854-2.png").targetOffset(-3,-7))
sleep(3)

if not exists("1562102064284.png"):
   click(Pattern("1555186639167-2.png").targetOffset(0,-2))
   sleep(2)

else:
    click(Pattern("1555186135652-2.png").targetOffset(0,2))
    sleep(2)
    click(Pattern("1555452968577-1.png").targetOffset(122,0))
    sleep(2)
    click(Pattern("1555356997978-1.png").targetOffset(-4,0))
    sleep(2)
    doubleClick("1555357410972-1.png")
    sleep(2)
    type(Pattern("1555186343019-2.png").targetOffset(-2,0), "altas")
    sleep(2)
    click("1555186584481-2.png")
    sleep(5)
    type(Key.ENTER)
    sleep(2)
    click(Pattern("1555186639167-2.png").targetOffset(0,-2))
    sleep(2)

print("inicio exportar altas_arq")
doubleClick("1555441777530.png")
wait(Pattern("1558198815444.png").similar(0.80),3600)
sleep(2)
click(Pattern("1558198815444.png").targetOffset(17,-20))
sleep(2)
click("1555442501848.png")
sleep(2)
click(Pattern("1555442587776.png").targetOffset(73,50))
sleep(2)
click(Pattern("1555442651607.png").targetOffset(-1,0))
sleep(2)
type(Pattern("1555185386377-5.png").targetOffset(20,0), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1555185427297-5.png").targetOffset(19,0), hasta.strftime("%d%m%Y"))
sleep(2)
print("ingresaron las fechas")
click(Pattern("1555185513046-4.png").targetOffset(43,-2))
sleep(2)
click(Pattern("1555185564402-4.png").targetOffset(3,8))

print("selecciona liquidación")
sleep(2)
click(Pattern("1555192475837-2.png").targetOffset(11,1))
sleep(2)
click(Pattern("1555192543295-2.png").targetOffset(16,2))
sleep(2)
type(Pattern("1555190912611-3.png").targetOffset(-1,-4), "333")
sleep(3)

print("Ingresa la contrata")
click(Pattern("1555185700153-3.png").targetOffset(-4,-1))
sleep(3)
click(Pattern("1555192730228-2.png").targetOffset(-5,-4))
sleep(2)
click("1555192808973-2.png")
sleep(3)

print("listo para exportar altas_arq")
click("1555185858713-3.png")
wait(Pattern("1556122962824.png").similar(0.80),3600)

print("Data Lista")
sleep(2)
click(Pattern("1556038340313-1.png").targetOffset(-4,-7))
sleep(3)
if not exists("1562102064284-1.png"):
   click(Pattern("1555186639167-3.png").targetOffset(0,-2))
   sleep(2)

else:
    wait(Pattern("1556037779854-1.png").similar(0.80),3600)
    sleep(2)
    click("1556037779854-1.png")
    sleep(2)
    click(Pattern("1555452968577-2.png").targetOffset(122,0))
    sleep(2)
    click(Pattern("1555356997978-4.png").targetOffset(-4,0))
    sleep(2)
    doubleClick("1555435879259-2.png")
    sleep(2)
    type(Pattern("1555186343019-5.png").targetOffset(-2,0), "altas_are")
    sleep(2)
    click("1555186584481-5.png")
    
    print("guardamos el archivo altas_arq")
    
    sleep(1)
    click("1555186711113-5.png")
    sleep(2)
    click(Pattern("1555186639167-5.png").targetOffset(0,-2))
    sleep(2)


print("inicio exportar averias")

doubleClick(Pattern("1555202418791-1.png").targetOffset(-88,1))
wait(Pattern("1558207117399.png").similar(0.80),3600)
click(Pattern("1558207117399.png").targetOffset(19,-20))
sleep(2)
type(Pattern("1555185386377-2.png").targetOffset(20,0), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1555185427297-2.png").targetOffset(19,0), hasta.strftime("%d%m%Y"))
sleep(2)
print("filtro de fecha registrada")
click(Pattern("1555185513046-1.png").targetOffset(43,-2))
sleep(2)
click(Pattern("1555185564402-1.png").targetOffset(3,8))

print("selecciona liquidacion")
click(Pattern("1555202828168-1.png").targetOffset(-42,-14))
sleep(2)
click("1555202968280-1.png")
sleep(2)
type(Pattern("1555203538887.png").targetOffset(-9,-3), "333")
sleep(2)
click("1555203656089.png")
wait(Pattern("1555393314794.png").similar(0.80),3600)
sleep(3)

print("Data Lista averias")
click(Pattern("1555193051854-1.png").targetOffset(-3,-7))
click("1555186135652-1.png")
click(Pattern("1555452968577.png").targetOffset(122,0))
sleep(2)
click(Pattern("1555356997978.png").targetOffset(-4,0))
sleep(2)
doubleClick("1555385330060.png")
sleep(2)
type(Pattern("1555186343019-1.png").targetOffset(-16,1), "averias")
sleep(2)
click("1555186584481-1.png")

print("guardamos el archivo averias")
sleep(7)
click("1555186711113-1.png")
sleep(2)
click(Pattern("1555186639167-1.png").targetOffset(0,-2))

print("inicio exportar componentes")
click(Pattern("1555255918222.png").targetOffset(-99,1))
doubleClick(Pattern("1555256045974.png").targetOffset(-6,-1))
sleep(2)
wait(Pattern("1555428464587.png").similar(0.80),3600)
click(Pattern("1555256165165.png").targetOffset(-32,0))
sleep(2)
print("opcion liquidado listo")
type(Pattern("1555256288407.png").targetOffset(24,1), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1555256331718.png").targetOffset(23,2), hasta.strftime("%d%m%Y"))
sleep(2)
print("filtro de fechas listo")
click(Pattern("1555256765228.png").targetOffset(-30,1))
sleep(2)
doubleClick(Pattern("1555256825014.png").targetOffset(70,17))
sleep(2)
click(Pattern("1555256907797.png").targetOffset(23,0))
sleep(2)
click(Pattern("1555256946356.png").targetOffset(-4,-1))
sleep(2)
click(Pattern("1555257015257.png").targetOffset(-5,1))
sleep(2)
click(Pattern("1555257092579.png").targetOffset(9,9))
sleep(3)

print("guardar componentes")
click("1555257442889.png")
sleep(2)
click(Pattern("1555393629717.png").targetOffset(121,0))
sleep(2)
click(Pattern("1555356997978.png").targetOffset(-4,0))
sleep(2)
doubleClick("1555358083538.png")
sleep(2)
type(Pattern("1555257510985.png").targetOffset(-2,-1), "componentes")
sleep(2)
click("1555257235791.png")
sleep(2)
click(Pattern("1555257275331.png").targetOffset(-16,15))
sleep(2)
click(Pattern("1555257588791.png").targetOffset(1,3))

print("guardamos el archivo componentes")
wait(Pattern("1555257843883.png").similar(0.80),3600)
sleep(2)
click(Pattern("1555257843883.png").targetOffset(35,51))
sleep(2)
click(Pattern("1555257927914.png").targetOffset(43,9))

print("fin exportar componentes")
sleep(2)

print("inicio exportar componentes_arq")
doubleClick(Pattern("1555431072546.png").targetOffset(-90,0))
wait(Pattern("1555427859674.png").similar(0.80),3600)
click(Pattern("1555256165165.png").targetOffset(-32,0))
sleep(2)
print("opcion liquidado listo")
type(Pattern("1555256288407.png").targetOffset(24,1), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1555256331718.png").targetOffset(23,2), hasta.strftime("%d%m%Y"))
sleep(2)
print("filtro de fechas listo")
click(Pattern("1555256765228.png").targetOffset(-30,1))
sleep(2)
doubleClick(Pattern("1555396128621.png").targetOffset(67,22))
sleep(2)
click(Pattern("1555396128621.png").targetOffset(67,22))
click(Pattern("1555256907797.png").targetOffset(23,0))
sleep(2)
click(Pattern("1555396223301.png").targetOffset(-1,0))
sleep(2)
click(Pattern("1555257015257.png").targetOffset(-5,1))
sleep(2)
click(Pattern("1555257092579.png").targetOffset(9,9))
sleep(2)

print("guardar componentes_arq")
click(Pattern("1555443217554.png").targetOffset(0,-7))
sleep(2)
click("1555393629717.png")
sleep(2)
click(Pattern("1555356997978.png").targetOffset(-4,0))
sleep(2)
doubleClick("1555443641543.png")
sleep(2)
type(Pattern("1555257510985.png").targetOffset(-2,-1), "componentes")
sleep(2)
click("1555257235791.png")
sleep(2)
click(Pattern("1555257275331.png").targetOffset(-16,15))
sleep(2)
click(Pattern("1555257588791.png").targetOffset(1,3))
sleep(2)

print("guardamos el archivo componentes_arq")
if exists(Pattern("1565016452970.png").similar(0.80),20):
    click(Pattern("1565016452970.png").similar(0.80).targetOffset(82,37))
    click(Pattern("1565016585868.png").targetOffset(43,38))

else:
    wait(Pattern("1555257843883.png").similar(0.80),120)
    click(Pattern("1555257843883.png").targetOffset(35,51))

sleep(2)
click(Pattern("1555257927914.png").targetOffset(43,9))

print("fin exportar componentes_arq")
sleep(2)
click(Pattern("1555389366717.png").targetOffset(110,2))
sleep(2)
wait(Pattern("1555389401450.png").similar(0.80),120)
sleep(2)
click(Pattern("1555389401450.png").targetOffset(25,52))
sleep(5)

#/*****************************FIREFOX******************************************/
App.open("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
sleep(20)

print("Ingresamos login")
paste(Pattern("1578350736328.png").targetOffset(-221,-30), user_inguz)
sleep(2)
type(Key.TAB)
sleep(5)
paste(pass_inguz)
sleep(5)
type(Key.ENTER)
sleep(2)
wait("1571938664492.png",120)
sleep(3)

print("ingresamos link de carga")
type("l",KEY_CTRL)
sleep(2)
paste(link_carga)
sleep(2)
type(Key.ENTER)
sleep(30)

#/*******************RUTINAS*************************************/
print("busca rutinas")
click(Pattern("1578674520498.png").similar(0.80).targetOffset(-231,-36))
sleep(5)
type("l",KEY_CTRL)
sleep(2)
paste(rutinas)
sleep(3)
type(Key.ENTER)
sleep(4)
click("1557955882339-9.png")
sleep(2)
type(Key.ENTER)
sleep(2)

#/*******************AVERIAS*************************************/
print("Busca Averias")
click(Pattern("1560613724615-1.png").similar(0.80).targetOffset(-43,-7))
sleep(3)
type("l",KEY_CTRL)
sleep(2)
paste(averias)
sleep(2)
type(Key.ENTER)
sleep(2)
wait(Pattern("1557957753205-9.png").similar(0.80),120)
click("1557957753205-9.png")
sleep(2)
type(Key.ENTER)
sleep(2)

#/*******************ALTAS*************************************/
print("busca altas")
click(Pattern("1560613862202-1.png").similar(0.90).targetOffset(-34,16))
sleep(3)
type("l",KEY_CTRL)
sleep(2)
paste(altas)
sleep(2)
type(Key.ENTER)
sleep(3)
if not exists ("1562103026497-1.png"):
    type("l",KEY_CTRL)
    sleep(1)
    paste(altas2)
    sleep(1)
    type(Key.ENTER)
    sleep(2)
    click(Pattern("1562103125400-1.png").targetOffset(-26,2))
    type(Key.ENTER)
    sleep(2)
else:
    click("1558024049493-9.png")
    type(Key.ENTER)
    sleep(3)

#/*******************COMPONENTES LIMA*************************************/
print("busca componentes lima")
click(Pattern("1560613988980-1.png").similar(0.90).targetOffset(-55,-7))
sleep(3)
type("l",KEY_CTRL)
sleep(2)
paste(componentes_lima)
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("1571687968868.png").similar(0.90).targetOffset(-73,3))
sleep(2)
type(Key.ENTER)
sleep(3)

#/*******************ALTAS AREQUIPA*************************************/
print("busca altas arequipa")
click(Pattern("1560614072201-1.png").similar(0.80).targetOffset(-36,14))
sleep(3)
type("l",KEY_CTRL)
sleep(2)
paste(altas_are)
sleep(2)
type(Key.ENTER)
sleep(3)
if not exists (Pattern("1565018813510-1.png").similar(0.80)):
    sleep(1)
    type("l",KEY_CTRL)
    sleep(1)
    paste(altas_are2)
    sleep(1)
    type(Key.ENTER)
    sleep(2)
    click(Pattern("1562103241168-1.png").targetOffset(-35,2))
    type(Key.ENTER)
    sleep(2)
else:
    click("1558036861655-9.png")
    type(Key.ENTER)
    sleep(3)

#/*******************COMPONENTES AREQUIPA*************************************/
print("busca componentes altas arequipa")
click(Pattern("1560614206978-2.png").similar(0.80).targetOffset(-103,27))
sleep(3)
type("l",KEY_CTRL)
sleep(1)
paste(componentes_are_det)
sleep(1)
type(Key.ENTER)
sleep(3)
if not exists (Pattern("1565017479575-1.png").similar(0.90)):
    sleep(1)
    type("l",KEY_CTRL)
    sleep(1)
    paste(componentes_are_det2)
    sleep(1)
    type(Key.ENTER)
    sleep(2)
    click(Pattern("1565017395728-1.png").targetOffset(-74,1))
    type(Key.ENTER)
    sleep(2)
else:
    wait(Pattern("1558037123333-10.png").similar(0.80))
    click("1558037123333-10.png")
    type(Key.ENTER)
    sleep(3)


print("procesar")
click(Pattern("1560615886789-1.png").similar(0.90).targetOffset(-12,40))
sleep(2)
wait(Pattern(Pattern("1560614596957-1.png").targetOffset(0,-1)).similar(0.8),1800)
sleep(3)
type("w",KEY_CTRL)
sleep(5)