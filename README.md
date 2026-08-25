# BlazeDemo - Framework de Automatización con Selenium y CI/CD

Framework de pruebas automatizadas end-to-end para el flujo de reserva de vuelos de [BlazeDemo](https://blazedemo.com), construido con Selenium, Python y pytest siguiendo el patrón Page Object Model. Incluye integración continua con GitHub Actions, que ejecuta la suite completa de pruebas automáticamente en cada push, y un caso de prueba que documenta un bug real de validación de formularios encontrado durante el testing exploratorio.
## Tecnologías usadas

- Python 3.14
- Selenium WebDriver
- pytest
- pytest-html (reportes)
- GitHub Actions (CI/CD)
- Page Object Model (patrón de diseño)

## Cómo correr el proyecto localmente

1. Clona el repositorio:
```bash
git clone https://github.com/AlexandraMateran/blazedemo-cicd-framework.git
cd blazedemo-cicd-framework
```

2. Crea y activa un entorno virtual:
```bash
python -m venv venv
source venv/Scripts/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Corre las pruebas:
```bash
pytest tests/ -v
```
## Estructura del proyecto

```
blazedemo-cicd-framework/
├── .github/workflows/     # Pipeline de GitHub Actions
├── pages/                 # Page Objects (una clase por página del sitio)
├── tests/                 # Casos de prueba y configuración de pytest
├── requirements.txt       # Dependencias del proyecto
└── README.md
```
## Hallazgo destacado

Durante el testing exploratorio del formulario de compra, se identificó que **BlazeDemo no valida los campos obligatorios** (nombre, dirección, número de tarjeta, etc.): el sitio permite completar una compra incluso enviando el formulario completamente vacío.

Este comportamiento está cubierto por la prueba `test_purchase_with_empty_fields`, que documenta el bug con un assert y un mensaje explicativo, en lugar de simplemente ignorarlo. Si el sitio corrige esta validación en el futuro, la prueba fallará intencionalmente, señalando el cambio.
