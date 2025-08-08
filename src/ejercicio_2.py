from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from datetime import datetime

#
URL_BASE = "http://localhost:3000"  
CAPTURES_DIR = "capturas2"


os.makedirs(CAPTURES_DIR, exist_ok=True)


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

try:
    
    driver.get(URL_BASE)
    time.sleep(1)
    driver.save_screenshot(f"{CAPTURES_DIR}/1_home.png")

    
    ejercicios_menu = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Ejercicios")))
    actions.move_to_element(ejercicios_menu).perform()
    time.sleep(1)
    driver.save_screenshot(f"{CAPTURES_DIR}/2_dropdown_abierto.png")

    
    ejercicio2_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Ejercicio 2")))
    ejercicio2_link.click()
    time.sleep(1)
    driver.save_screenshot(f"{CAPTURES_DIR}/3_ejercicio2.png")

    
    input_nombre = wait.until(EC.presence_of_element_located((By.NAME, "dato")))
    input_nombre.send_keys("Selenium")
    driver.save_screenshot(f"{CAPTURES_DIR}/4_input_nombre.png")

    
    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.click()
    time.sleep(2)  
    driver.save_screenshot(f"{CAPTURES_DIR}/5_resultado.png")

    
    fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"report_{fecha_actual}.html"
    

    
    html_content = f"""
    <html lang="es">
    <head>
        <title>Reporte Ejercicio 2 - {fecha_actual}</title>
        
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
        <h1>Reporte de Automatización - Ejercicio 2</h1>
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
                <img src="3_ejercicio2.png" alt="Paso 3">
            </li>
            <li>
            	<h2>Paso 4</h2>
                <img src="4_input_nombre.png" alt="Paso 4">
            </li>
            <li>
            	<h2>Paso 5</h2>
                <img src="5_resultado.png" alt="Paso 5">
            </li>
        </ol>
    </body>
    </html>

    """

    
    # Guardar el informe HTML en el directorio de capturas
    with open(f"{CAPTURES_DIR}/{report_filename}", "w") as f:
        f.write(html_content)

finally:
    driver.quit()

print("Proceso completado. Capturas guardadas en la carpeta 'capturas'.")
