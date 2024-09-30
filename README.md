# G Academica

G Academica es un proyecto desarrollado en Python utilizando el framework Django.

## Requisitos previos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado)

## Instalación

1. Clona el repositorio:
   ```
   git clone https://github.com/DavidPPizarro/demo.git
   cd demo
   ```

2. (Opcional) Crea y activa un entorno virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Configuración de la base de datos

1. Aplica las migraciones:
   ```
   python manage.py migrate
   ```

2. (Opcional) Crea un superusuario:
   ```
   python manage.py createsuperuser
   ```

## Ejecutar el proyecto

1. Asegúrate de que tu entorno virtual esté activado (si lo estás utilizando).

2. Ejecuta el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

3. Abre tu navegador y visita `http://localhost:8000` para ver la aplicación en funcionamiento.

## Desarrollo

- Para crear nuevas migraciones después de cambios en los modelos:
  ```
  python manage.py makemigrations
  ```

- Para ejecutar pruebas:
  ```
  python manage.py test
  ```

## Despliegue

Para desplegar en producción, asegúrate de configurar adecuadamente los siguientes aspectos:

- Desactiva el modo DEBUG en `settings.py`: `DEBUG = False`
- Configura una base de datos apropiada para producción
- Implementa medidas de seguridad adecuadas, como una `SECRET_KEY` segura
- Configura los hosts permitidos en `ALLOWED_HOSTS`
- Utiliza un servidor web como Gunicorn o uWSGI junto con Nginx

**Nota de seguridad**: Antes de desplegar en producción, es crucial implementar medidas de seguridad adecuadas, incluyendo una `SECRET_KEY` segura y única. La ausencia de estas medidas puede comprometer la seguridad de tu aplicación.

## Contribuir

Si deseas contribuir al proyecto, por favor:

1. Haz un fork del repositorio
2. Crea una nueva rama para tu función: `git checkout -b nueva-funcion`
3. Haz tus cambios y realiza commits: `git commit -am 'Agrega nueva función'`
4. Empuja tus cambios a la rama: `git push origin nueva-funcion`
5. Envía un pull request
