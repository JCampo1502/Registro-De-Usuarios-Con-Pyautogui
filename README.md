# ExplosionProject — Automatización de registros en cultura.ssiset.com

Resumen
-------
Script en Python que automatiza el proceso de inscripción de usuarios en la página `cultura.ssiset.com`. Usa `pyautogui` para interacción con la interfaz (clics, teclas, búsquedas por imagen) y un JSON de entrada con los datos de los usuarios.

Advertencia rápida
------------------
- Es un robot UI: llevará el control del ratón/teclado. No usar mientras trabajas en el equipo.
- Asegura que las imágenes en `captures/` coincidan exactamente con los elementos que el script busca.
- Ejecutar en Windows; requiere tener el navegador Brave en la barra de tareas (según las imágenes y la lógica del script).

Requisitos
----------
- Python 3.8+ instalado en Windows
- Dependencias:
  - pyautogui
  - box (pip install python-box)
- Archivos:  
  - `index.py` (script principal)  
  - `completos.json` (datos de entrada)  
  - carpeta `captures/` (imágenes usadas para localizar elementos en pantalla)

Instalación
----------
1. Crear y activar un entorno virtual (recomendado).
2. Instalar dependencias:
   ```bash
   pip install pyautogui python-box

Adjunto video de funcionamiento
----------
- Se adjunta un video que muestra el funcionamiento del script de automatización.



https://github.com/user-attachments/assets/57f8831e-ea8e-430c-bf00-607f0abca36b



https://github.com/user-attachments/assets/6e1ff8c8-faac-48e8-aa8d-cf11212057f7







