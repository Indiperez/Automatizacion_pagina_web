from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from datetime import datetime
from PIL import Image

# URL base de tu sitio web
URL_BASE = "http://localhost:3000/index.php"  
CAPTURES_DIR = "capturas10"

# Función para capturar toda la página mediante scroll
def screenshot_full_scroll(driver, path):
    viewport_height = driver.execute_script("return window.innerHeight")
    total_height = driver.execute_script("return document.body.scrollHeight")

    slices = []

    # Realiza scroll y toma capturas
    for offset in range(0, total_height, viewport_height):
        driver.execute_script(f"window.scrollTo(0, {offset});")
        time.sleep(0.5)  
        slice_path = f"{CAPTURES_DIR}/temp_scroll_{offset}.png"
        driver.save_screenshot(slice_path)
        slices.append(slice_path)

    # Une todas las imágenes capturadas
    images = [Image.open(img) for img in slices]
    total_width = images[0].size[0]
    combined_height = sum(img.size[1] for img in images)

    final_image = Image.new('RGB', (total_width, combined_height))

    y_offset = 0
    for img in images:
        final_image.paste(img, (0, y_offset))
        y_offset += img.size[1]

    final_image.save(path)

    # Elimina las capturas temporales
    for img in slices:
        os.remove(img)

# Crear directorio para capturas si no existe
os.makedirs(CAPTURES_DIR, exist_ok=True)

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Iniciar el driver de Selenium
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

try:
    # Paso 1: Abrir la página inicial
    driver.get(URL_BASE)
    time.sleep(1)
    driver.save_screenshot(f"{CAPTURES_DIR}/1_home.png")

    
    ejercicios_menu = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Ejercicios")))
    actions.move_to_element(ejercicios_menu).perform()
    time.sleep(1)  
    driver.save_screenshot(f"{CAPTURES_DIR}/2_dropdown_abierto.png")

    ejercicio1_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Ejercicio 10")))
    ejercicio1_link.click()
    time.sleep(1)
    driver.save_screenshot(f"{CAPTURES_DIR}/3_ejercicio.png")
    
    submit_button = driver.find_element(By.LINK_TEXT, "Generar otro chiste")
    submit_button.click()
    time.sleep(2)
    
    driver.save_screenshot(f"{CAPTURES_DIR}/4_resultado.png")
    

    # Generación del nombre del archivo para el reporte
    fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"report_{fecha_actual}.html"

    # Contenido HTML del reporte
    html_content = f"""
    <html lang="es">
    <head>
        <title>Reporte Ejercicio 10 - {fecha_actual}</title>
        
        <style>
            body {{ font-family: Arial, sans-serif; }}
            h1 {{ color: #4CAF50; }}
            .step {{ margin-bottom: 20px; }}
            .step img {{ max-width: 100%; width: 600px; }}
            ol {{ width: 100%; margin-top: 20px; border-collapse: collapse; }}
            li img {{ max-width: 600px; }}
        </style>
    </head>
    <body>
        <h1>Reporte de Automatización - Ejercicio 10</h1>
        <p><strong>Fecha y Hora del Reporte:</strong> {fecha_actual}</p>
        <h2>Pasos Realizados:</h2>
        
        <ol>
            <li>
            	<h2>Paso 1</h2>
                <img src="1_home.png" alt="Paso 1">
            </li>
            <li>
            	<h2>Paso 2</h2>
                <img src="2_dropdown_abierto.png" alt="Paso 2">
            </li>
            <li>
            	<h2>Paso 3</h2>
                <img src="3_ejercicio.png" alt="Paso 3">
            </li>
            <li>
            	<h2>Paso 4</h2>
                <img src="4_resultado.png" alt="Paso 4">
            </li>
        </ol>
    </body>
    </html>
    """

    # Guardar el reporte HTML
    with open(f"{CAPTURES_DIR}/{report_filename}", "w") as f:
        f.write(html_content)

finally:
    # Cerrar el driver
    driver.quit()

print("Proceso completado. Capturas guardadas en la carpeta 'capturas'.")
