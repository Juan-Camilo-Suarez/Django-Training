# Django-Training

## instalacion y ejecución del proyecto
1. crear un entorno virtual:\
```python -m venv venv```
2. activar el entorno virtual:\
```venv\Scripts\activate.bat``` - для Windows \
```source venv/bin/activate``` - для Linux и MacOS
3. instalar las dependencias:\
```pip install -r requirements.txt```
4. crear la base datos con ayuda de docker en PostgreSQL:\
```docker-compose up```
5. crear las migraciones:\
```python manage.py migrate```
6. correr el servidor:\
```python manage.py runserver```