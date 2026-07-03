# Proyecto base — Actividad SonarCloud + CI (E-EMDS-2)

Este proyecto ya trae código funcional, tests con 100% de cobertura y los
archivos de configuración listos. Lo único que falta es lo que **solo
ustedes pueden hacer** porque requiere sus cuentas reales de GitHub y
SonarCloud (así se genera la evidencia que pide el profesor).

## Pasos que tienen que hacer ustedes

### 1. Crear el repo (Parte 1)
```bash
cd proyecto-sonarcloud
git init
git add .
git commit -m "Proyecto base para actividad SonarCloud"
git branch -M main
git remote add origin https://github.com/SU_USUARIO/SU_REPO.git
git push -u origin main
```
Borren o ignoren el archivo `pages/calculadora_CON_ISSUE_para_rama_parte4.py`
al hacer el commit inicial (es solo instrucciones, no es código del proyecto).

### 2. Conectar SonarCloud (Parte 1)
- Entren a sonarcloud.io con su cuenta de GitHub.
- Importen su organización y el repositorio (**Analyze new project**).
- Elijan **With GitHub Actions** y desactiven **Automatic Analysis**.
- Tomen la Evidencia 1 (captura del proyecto creado).
- Copien los valores reales de `sonar.organization` y `sonar.projectKey`
  y reemplácenlos en `sonar-project.properties`.

### 3. Configurar el secreto y hacer push (Parte 2 y 3)
- En SonarCloud generen un token (My Account → Security).
- En GitHub: Settings → Secrets and variables → Actions → New repository
  secret → nombre `SONAR_TOKEN`, valor el token generado.
- Tomen la Evidencia 2 (captura de los archivos + el secret creado).
- Hagan commit/push del `sonar-project.properties` actualizado.
- Vean correr el workflow en la pestaña **Actions**.
- Cuando termine en verde, tomen la Evidencia 3 (Action verde + tablero
  de SonarCloud) y anoten los valores reales de Reliability, Security,
  Maintainability, Coverage y Duplications en la tabla del .tex.

### 4. Romper el Quality Gate (Parte 4)
Sigan las instrucciones dentro de
`pages/calculadora_CON_ISSUE_para_rama_parte4.py` para crear la rama,
introducir la credencial embebida y abrir el Pull Request. Tomen la
Evidencia 4 (captura del PR con el estado Failed).

## Correr los tests localmente (opcional, para verificar antes de subir)
```bash
pip install -r requirements.txt pytest-cov
pytest --cov=pages --cov-report=xml
```
