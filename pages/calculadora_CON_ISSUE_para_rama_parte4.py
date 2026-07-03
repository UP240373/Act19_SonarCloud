"""
NO subir este archivo tal cual al repo.
Es la referencia de qué cambiar en pages/calculadora.py cuando hagan
la rama de la Parte 4 (romper el Quality Gate).

Instrucciones:
1. git checkout -b issue/hardcoded-password
2. Abran pages/calculadora.py y agreguen, por ejemplo, al inicio del archivo:

       DB_PASSWORD = "clave123"

   Esto dispara la regla python:S2068 de SonarQube (Hard-coded credentials
   are security-sensitive) y debería marcar el Quality Gate del PR como
   Failed.
3. git add pages/calculadora.py
4. git commit -m "test: introducir credencial embebida para romper Quality Gate"
5. git push origin issue/hardcoded-password
6. Abran el Pull Request hacia main en GitHub y esperen el comentario de SonarCloud.
7. Tomen la Evidencia 4 (captura del PR con el estado Failed).
8. Cierren el PR sin hacer merge (o revierta el cambio) para no dejar la
   credencial en main.
"""
