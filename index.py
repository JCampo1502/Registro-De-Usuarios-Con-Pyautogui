import pyautogui
from box import Box
import json 
from time import sleep

# Configuraciones globales
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5
# Carpeta de imagenes
IMAGES_PATH = "captures"
# Ruta de los Datos
DATA_PATH = "completos.json"
# Applicacion urls
APLICATION_LOGGIN_URL ="cultura.ssiset.com/";
APLICATION_REGISTER_URL ="cultura.ssiset.com/inscriptions/create";
# Gmail usuario
GMAIL_USER = "Escribe tu gmail aqui"
GMAIL_PASSWORD = "Escribe tu contraseña aqui"
#ingresar usuario y contraseña
APP_USER = "Escribe tu usuario de la app aqui"
APP_PASSWORD = "escribe tu contraseña de la app aqui"
# Funciones de automatizacion
def tab(): pyautogui.press("tab")
def enter(): pyautogui.press("enter")
def write(text, sleepTime= 0.5): 
    pyautogui.write(text)
    sleep(sleepTime)
def click(x,y): pyautogui.click(x,y)
def doubleClick(x,y): pyautogui.doubleClick(x,y)
def rightClick(x,y): pyautogui.rightClick(x,y)

# Desplazamiento de la pantalla
def scroll(amount,sleepTime= 0.5): 
    pyautogui.scroll(amount)
    sleep(sleepTime)
# Escribir texto y presionar enter
def writeText(text,sleepTime= 1):
    write(text)
    enter()    
    sleep(sleepTime)
    
# Escribir arroba
def writeAtSymbol(): pyautogui.hotkey("ctrl", "alt", "q")
# Localizar imagen en pantalla
def locateOnScreen(imageUrl, confidence=0.8): 
    """Busca una imagen en pantalla"""
    try:
        pos = pyautogui.locateOnScreen(imageUrl, confidence=confidence)
        x,y = pyautogui.center(pos)
        return x,y
    except: 
        return None

# Acción general
def action(imageUrl, callback= None,sleepTime= 1, confidence=0.8):    
    x,y = locateOnScreen(imageUrl, confidence)
    if(x is None or y is None):
        return None
    if callable(callback):
        callback(x,y)
        sleep(sleepTime)   
# Seleccionar Si o No
def selectYesOrNo(option="No"):
    if option=="Si":
        pyautogui.press("space")
    else:
        pyautogui.press("right")

# Obtener datos del json
def getData(dataPath):
    with open(dataPath, "r", encoding="utf-8") as file:
        datos_raw = json.load(file)    
    datos = [Box(item) for item in datos_raw]
    return datos 

# Avanzar secciones
def goToNextSection():
    sleep(1)
    scroll(-500,1)
    action(f"{IMAGES_PATH}/avanzar.png", click,2)
    sleep(2)
# Next Form
def goToNextForm():
    sleep(4)
    action(f"{IMAGES_PATH}/siguienteFormulario.png", click,2)
    sleep(2)
# Enviar formulario
def submitForm():
    sleep(1)
    scroll(-500,1)
    action(f"{IMAGES_PATH}/completar.png", click,3)
# Foto de perfil
def saveProfilePhoto(user):                
        #Abrir nueva pestaña
        action(f"{IMAGES_PATH}/nuevaPagina.png", click,4)
        # Escribir url de la imagen
        writeText(user.fotoLink,5) 
        # Descargar imagen
        action(f"{IMAGES_PATH}/download.png", click,4)
        #guardar imagen
        writeText("FotoPerfil.png",1)
        # sobre escribir en la imagen
        try:
            sleep(2)
            action(f"{IMAGES_PATH}/sobrescribir.png", click,2)
        except:
            pass
        
        # Cerrar pestaña de la imagen
        pyautogui.hotkey("ctrl", "w")        
        sleep(1)
        #Regresar a la pestaña de registro
        pyautogui.hotkey("ctrl", "1")
        sleep(1)
        enter()
        try:
            sleep(1.5)
            action(f"{IMAGES_PATH}/explorerBrowser.png", click,2)
            writeText("descargas",3)
        except:
            pass
        action(f"{IMAGES_PATH}/fotoDePerfilImg.png", click,2)
        enter()
        sleep(1.5)        
# Redireccionar a la pagina de registro
def goToRegisterPage():
    # Cambiar la url a para crear inscripcion    
    action(f"{IMAGES_PATH}/barraDeBusqueda.png", click, 1.5)
    writeText(APLICATION_REGISTER_URL, 3)       
        
# Registro de usuario
def addUserSecction1(user):
    sleep(1)
    # ¿COMO SE VINCULO USTED AL PROYECTO? *
    tab()    
    writeText("Por medio de un instructor del proyecto")
    # INSTRUCTOR *    
    tab()    
    writeText("Mario Zuluaga")    
    #GRUPO *
    tab()
    writeText("EXPLOSION SALSERA")
    # NOMBRE Y APELLIDO *
    tab()
    writeText(user.nombre)
    # TIPO DE DOCUMENTO DE IDENTIDAD *
    tab()
    if user.edad >= 18 and user.tipoDocumento=="Tarjeta de identidad":
        user.tipoDocumento = "ciudadania"
    writeText(user.tipoDocumento)
    # NUMERO DE IDENTIDAD *
    tab()
    writeText(user.numeroDocumento)
    # NAC
    tab()
    writeText(user.comuna)
    # BARRIO *
    tab()
    writeText(user.barrio)
    # ZONA *
    tab()
    writeText("Urbano")
    # ESTRATO *
    tab()
    writeText(user.estrato)
    # TELÉFONO *
    tab()
    writeText(user.celular)
    # EMAIL *
    tab()    
    writeText("")
    # Guardar foto de perfil
    tab()
    saveProfilePhoto(user)
    goToNextSection()
# Registro de usuario - Seccion 2
def addUserSecction2(user):
    sleep(1)
    # Seleccionar Genero *
    action(f"{IMAGES_PATH}/genero.png", click,1, 0.6)
    writeText(user.genero,1)
    # Seleccionar Edad *
    tab()
    writeText(str(user.edad))
    # Estudia actualmente? *
    tab()
    selectYesOrNo(user.estudiaActualmente)
    sleep(2)
    # Nivel Educativo Alcanzado *
    tab()
    writeText(user.nivelDeEstudioAlcanzado)
    # Presenta Discapacidad *
    tab()
    selectYesOrNo(user.presentaDiscapacidad)
    sleep(2)
    if(user.presentaDiscapacidad=="Si"):
        # Tipo de Discapacidad *
        tab()
        writeText(user.discapacidad)
    # Tipo de Etnia *
    tab()
    writeText(user.grupoEtnico)
    # Condicion *
    tab()
    writeText(user.esUsted)
    # Avanzar a la siguiente seccion
    goToNextSection()
# Registro de usuario - Seccion 3
def addUserSecction3(user):
    sleep(1)
    # Seleccionar Regimen de Salud *
    action(f"{IMAGES_PATH}/regimenSalud.png", click,1, 0.6)
    writeText(user.regimenSalud)
    # Seleccionar EPS *
    tab()
        
    writeText(user.nombreEps)
    if user.nombreEps=="Otro":
        tab()
        writeText(user.epsCual)
    # Estado de salud *
    tab()
    writeText("Bueno")
    
# Registrar acudiente
def addAcudienteSecction1(acudiente):
    sleep(1)
    # Agregar parentezco *
    action(f"{IMAGES_PATH}/parentezco.png", click,2)
    writeText(acudiente.parentezco)
    # Agregar nombre completo *
    tab()
    writeText(acudiente.nombre)
    # Agregar tipo de documento *
    tab()
    writeText("ciudadania")
    # Agregar numero de documento *
    tab()
    writeText(str(acudiente.numeroDocumento))
    # Agregar zona
    tab()
    writeText("Urbano")
    # Agregar telefono *
    tab()
    writeText(acudiente.celular)
    # Agregar email *
    tab()
    writeText("")
    # Avanzar a la siguiente seccion
    goToNextSection()
# Registrar acudiente - Seccion 2
def addAcudienteSecction2(acudiente):
    sleep(1)
    # Seleccionar Genero *
    action(f"{IMAGES_PATH}/genero.png", click,1, 0.6)
    writeText(acudiente.genero,1)
    # Seleccionar Edad *
    tab()
    writeText(str(acudiente.edad + 1),1)
    # Estudia actualmente? *
    tab()
    selectYesOrNo(acudiente.estudiaActualmente)
    sleep(2)
    # Nivel Educativo Alcanzado *
    tab()
    writeText(acudiente.nivelDeEstudioAlcanzado)
    # Presenta Discapacidad *
    tab()
    selectYesOrNo(acudiente.presentaDiscapacidad)
    sleep(2)
    if(acudiente.presentaDiscapacidad=="Si"):
        # Tipo de Discapacidad *
        tab()
        writeText(acudiente.discapacidad)
    # Tipo de Etnia *
    tab()
    writeText(acudiente.grupoEtnico)
    # condicion *
    tab()
    writeText(acudiente.esSuAcudiente)
    # siguiente seccion
    goToNextSection()
# Registrar acudiente - Seccion 3
def addAcudienteSecction3(acudiente):
    sleep(1)
    # Seleccionar Regimen de Salud *
    action(f"{IMAGES_PATH}/regimenSalud.png", click,1, 0.6)
    writeText(acudiente.regimenSalud)
    # Seleccionar EPS *
    tab()        
    writeText(acudiente.nombreEps)
    if acudiente.nombreEps=="Otro":
        tab()
        writeText(acudiente.epsCual)
    # Estado de salud *
    tab()
    writeText("Bueno")
    # enviar formulario
    submitForm()

# Llenar las secciones del registro
def fillUserSections(user,i):    
    # Registrar Usuario
    addUserSecction1(user,i)    
    addUserSecction2(user,i)    
    addUserSecction3(user,i)
    # Validar si es mayor de edad
    if user.edad>=18:
        # enviar formulario
        submitForm()        
        goToNextForm()
        return True
    else:
        goToNextSection()
    # Registrar acudiente
    acudiente = user.acudiente
    
    addAcudienteSecction1(acudiente,i)    
    addAcudienteSecction2(acudiente,i)    
    addAcudienteSecction3(acudiente,i)    
    goToNextForm()

# llenar datos de login
def fillLoginData():
    # Abrir brave necesita tenerlo en la barra de tareas    
    action(f"{IMAGES_PATH}/brave.png", rightClick,1.5)
    # Abrir modo incognito
    action(f"{IMAGES_PATH}/incognito.png", click,2)
    
    try:
        # Escribir url
        print(APLICATION_LOGGIN_URL)
        writeText(APLICATION_LOGGIN_URL,5)
        # Ingresar usuario
        action(f"{IMAGES_PATH}/usuario.png",click,0.5)
        write(APP_USER, 1)
        # Ingresar contraseña
        tab()
        writeText(APP_PASSWORD, 1)
    except:
        print("Error al llenar los datos de login")

# Inicio del proceso
def main():  
    # Optener datos del json
    datos = getData(DATA_PATH)
        
    # Abrir navegador e iniciar sesion
    fillLoginData()
   
    # Inscribir usuarios        
    numeroDeRegistros = len (datos)
    totalInscritos = 0
    for i, user in enumerate (datos):
        # incrementar edad del usuario en 1
        user.edad+=1
        # Redirigir a la pagina de registro
        goToRegisterPage()
        # Apetar autorizacion
        action(f"{IMAGES_PATH}/si.png", click, 0.8)
        scroll(-500)
                               
        # Iniciar registro
        print(f"Registro {i+1} de {numeroDeRegistros} - {user.nombre}")
        
        try:
            # Ir llenando las secciones del usuario
            fillUserSections(user,i)
        except Exception as e:
            # Registrar usuario
            print(f"Error al registrar el usuario {user.nombre}: {e}")
            continue
        totalInscritos +=1
        
    # Finalizar proceso
    pyautogui.alert(f"Proceso de inscripcion finalizado con exito.\nTotal de inscritos: {totalInscritos} de {numeroDeRegistros} usuarios.")
    
# Ejecutar main
if __name__ == "__main__":
    main()









