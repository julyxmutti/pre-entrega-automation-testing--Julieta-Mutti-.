# Automatización QA - SauceDemo

Proyecto de automatización de pruebas realizado con Python para el curso de Talento Tech.

## Tecnologías usadas

- Python
- Selenium
- Pytest
- Behave
- Git
- GitHub

## Instalación

Instalar las dependencias necesarias:

```bash
pip install selenium pytest pytest-html behave
```

## Ejecutar las pruebas

Desde la carpeta raíz del proyecto:

```bash
python -m pytest                 # Ejecutar todos los tests
python -m pytest tests/test_login.py  # Ejecutar tests de login
python -m behave                 # Ejecutar pruebas BDD con Behave
```

**Nota:** Si Windows no reconoce el comando `python`, verificar el PATH y los alias de ejecución de aplicaciones. En VS Code se recomienda utilizar PowerShell como terminal.

## Reporte HTML

El proyecto utiliza pytest-html para generar reportes de ejecución.

El reporte se guarda en:

`reports/reporte.html`

Abrir ese archivo en el navegador para consultar los resultados, siempre que se haya generado durante la ejecución.

## Casos de prueba

- Login exitoso
- Agregar producto al carrito
- Verificar producto del carrito