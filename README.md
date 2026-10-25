# Automatización QA - SauceDemo

Proyecto de automatización de pruebas realizado con Python para el curso de Talento Tech.

## Tecnologías usadas

- Python
- Selenium
- Pytest
- Git
- GitHub

## Instalación

Instalar las dependencias necesarias:

```bash
pip install selenium
pip install pytest
pip install pytest-html
```

## Ejecutar las pruebas

Ejecutar todos los tests desde la carpeta raíz del proyecto:

```bash
pytest
```

Si el comando `python` o `pytest` no funciona en Git Bash, utilizar la ruta completa del intérprete de Python:

```bash
"C:/Users/Julyx/AppData/Local/Python/pythoncore-3.14-64/python.exe" -m pytest
```

### Ejecutar un archivo específico

Por ejemplo, para ejecutar las pruebas de login (Va todo "C:/Users/Julyx/AppData/Local/Python/pythoncore-3.14-64/python.exe" -m pytest tests/test_login.py):

```bash
"C:/Users/Julyx/AppData/Local/Python/pythoncore-3.14-64/python.exe" -m pytest tests/test_login.py
```

## Reporte HTML

El proyecto utiliza pytest-html para generar reportes de ejecución.

El reporte se guarda en:

`reports/reporte.html`

Abrir ese archivo en el navegador para consultar los resultados, siempre que se haya generado durante la ejecución.

## Casos de prueba

- Login exitoso
- Agregar producto al carrito
- Verificar producto del carrito
