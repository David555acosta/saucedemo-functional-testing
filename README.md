# SauceDemo Automation Testing

## Descripción

Este proyecto corresponde al Trabajo Práctico Final de la materia Taller de Testing Automation.

El objetivo es automatizar la validación funcional de la aplicación SauceDemo, una tienda online diseñada para prácticas de testing, utilizando Selenium WebDriver en Python.

---

## Objetivo

Desarrollar pruebas automatizadas que validen el correcto funcionamiento de los principales flujos de la aplicación:

* Inicio de sesión
* Agregado de productos al carrito
* Validación de productos seleccionados

---

## Tecnologías utilizadas

* Python
* Selenium WebDriver
* unittest
* ChromeDriver

---

## Casos de prueba automatizados

### Caso 1 – Inicio de sesión exitoso

Verifica que el usuario pueda iniciar sesión correctamente utilizando credenciales válidas.

**Validación:**

* Acceso exitoso al sistema
* Visualización de la pantalla de productos

---

### Caso 2 – Agregado de múltiples productos

Verifica que sea posible agregar dos productos distintos al carrito.

**Validaciones:**

* Ambos productos se agregan correctamente
* Los productos aparecen en el carrito
* Los nombres coinciden con los esperados

---

### Caso 3 – Validación de cantidad de productos

Verifica que la cantidad de productos en el carrito sea correcta.

**Validación:**

* La cantidad de productos coincide con la cantidad agregada

---

## Credenciales de acceso

* Usuario: `standard_user`
* Contraseña: `secret_sauce`

---

## Estructura del proyecto

```
SAUCEDEMO-FUNCTIONAL-TESTING/
│
├── capturas/
│   ├── caso1Capturas/      # Evidencias del login exitoso
│   ├── caso2Capturas/      # Evidencias de agregado al carrito
│   └── caso3Capturas/      # Evidencias de validación de cantidad
│
├── caso1.py                # Caso de prueba 1
├── caso2.py                # Caso de prueba 2
├── caso3.py                # Caso de prueba 3
│
└── README.md
```

---

## Ejecución

1. Instalar dependencias:

```
pip install selenium
```

2. Descargar ChromeDriver y configurarlo en el PATH del sistema.

3. Ejecutar el script:

```
python caso1.py
python caso2.py
python caso3.py
```

---

## Consideraciones

* Se utilizan esperas para asegurar la correcta carga de los elementos.
* Se emplea el framework unittest para la estructuración de los tests.
* Se validan tanto elementos individuales como listas de resultados.

---

## Funcionalidades implementadas

* Automatización de login
* Interacción con elementos dinámicos
* Uso de `find_element` y `find_elements`
* Extracción de texto mediante `.text`
* Validación de múltiples elementos
* Comparación entre valores esperados y obtenidos

---

## Posibles mejoras

* Implementación de Page Object Model (POM)
* Uso de WebDriverWait en lugar de `time.sleep`
* Integración con herramientas de CI/CD
* Ejecución en múltiples navegadores

---

## Autor

David Acosta
