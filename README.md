# Meu primerio Projeto Django
Este é meu primeiro projeto Django, que aborda as bases do framework.

## Instrução para baixar, editar e executar local
1. Clone o repositório
```bash
git clone https://github.com/JDelfinox/projeto1.git
```
2. Entre na pasta do Projeto e crie um ambiente virtual python
```bash
cd projeto1
```
``` bash
python -m venv venv
```
3. Ative o ambiente virtual
no windows:
```bash
venv\Scripts\activate
```
no linux:
```bash
source .venv/bin/activate
```
4. Instale as dependências
```bash
pip install -r requirements.txt
```
5. Execute as migrações
```bash
python manage.py migrate
```
6. Execute o servidor
```bash
python manage.py runserver
```