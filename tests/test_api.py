
# x-api-key: pub_ccb7423645c94ec1940eda35d142516020604aa6b6224e338145b36de9546884
# py -m pytest tests/test_api.py

import requests
from utils.logger import logger


def test_obtener_usuario(base_url, headers):
    try:
        logger.info("Iniciando prueba de obtener usuario")

        url = f"{base_url}/users/2"
        response = requests.get(url, headers=headers)
        logger.info("Solicitud GET ejecutada")

        # NIVEL 1: STATUS CODE
        codigo = response.status_code
        assert codigo == 200
        logger.info("Codigo de estado validado")

        # NIVEL 2: HEADERS
        assert "application/json" in response.headers["Content-Type"]
        logger.info("Content-Type validado")

        # NIVEL 3: ESTRUCTURA
        data = response.json()
        logger.info("Respuesta JSON obtenida")

        assert isinstance(data, dict)
        assert "data" in data
        assert isinstance(data["data"], dict)

        assert "id" in data["data"]
        assert "email" in data["data"]
        assert "first_name" in data["data"]
        assert "last_name" in data["data"]
        logger.info("Estructura de respuesta validada")

        # NIVEL 4: CONTENIDO
        assert data["data"]["id"] == 2
        assert data["data"]["email"] == "janet.weaver@reqres.in"
        logger.info("Contenido de usuario validado")

        # NIVEL 5: TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 2
        logger.info("Tiempo de respuesta validado")

    except Exception:
        logger.exception("Error durante la prueba de obtener usuario")
        raise


def test_crear_usuario(base_url, headers):
    try:
        logger.info("Iniciando prueba de crear usuario")

        url = f"{base_url}/users/"

        usuario = {
            "email": "jose.montezuma@bue.edu.ar",
            "first_name": "Jose",
            "last_name": "Montezuma",
            "job": "Instructor"
        }

        response = requests.post(url, headers=headers, json=usuario)
        logger.info("Solicitud POST ejecutada")

        # NIVEL 1
        assert response.status_code == 201
        logger.info("Codigo de estado validado")

        # NIVEL 2
        assert "application/json" in response.headers["Content-Type"]
        logger.info("Content-Type validado")

        # NIVEL 3
        data = response.json()
        assert "email" in data
        assert "first_name" in data
        assert "last_name" in data
        assert "id" in data
        logger.info("Estructura de respuesta validada")

        # NIVEL 4
        assert data["email"] == usuario["email"]
        assert data["first_name"] == usuario["first_name"]
        logger.info("Contenido del usuario validado")

        # NIVEL 5: TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 2
        logger.info("Tiempo de respuesta validado")

    except Exception:
        logger.exception("Error durante la prueba de crear usuario")
        raise


def test_eliminar_usuario(base_url, headers):
    try:
        logger.info("Iniciando prueba de eliminar usuario")

        url = f"{base_url}/users/2"
        response = requests.delete(url, headers=headers)
        logger.info("Solicitud DELETE ejecutada")

        # NIVEL 1: STATUS CODE
        assert response.status_code == 204
        logger.info("Codigo de estado validado")

        # NIVEL 2: HEADERS
        assert "Content-Type" not in response.headers
        logger.info("Ausencia de Content-Type validada")

        # NIVEL 3 y 4: ESTRUCTURA Y CONTENIDO
        assert len(response.content) == 0
        logger.info("Respuesta sin contenido validada")

        # NIVEL 5: TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 2
        logger.info("Tiempo de respuesta validado")

    except Exception:
        logger.exception("Error durante la prueba de eliminar usuario")
        raise
