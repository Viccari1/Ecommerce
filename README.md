# Projeto Loja

Este é um projeto de Ecommerce (Comércio virtual, ou Loja virtual) feito com Python Django.

## Tecnologias Utilizadas
- Django
- Python
- Bootstrap
- Sqlite

## Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/Viccari1/Ecommerce.git
    ```
2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
3. Ative esse ambiente:
    ```bash
    # Para Windows
    venv\Scripts\activate

    # Para Linux ou MacOS
    source venv/bin/activate
    ```
4. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```
5. Rode as migrações:
    ```bash
    python manage.py migrate
    ```

6. Adicione arquivo .env na pasta Ecommerce/core/:
    ```bash
    # Caso você não tenha a chave, execute:
    python manage.py gerar_chave
    SECRET_KEY = [ADICIONE A CHAVE SECRETA]
    ```

7. Inicie o servidor local:
    ```bash
    python manage.py runserver
    ```

## Uso
Para acessar o site, abra o navegador e acesse: http://127.0.0.1:8000/

## Licença
Este projeto está licenciado sob uma licença Copyright, todos os direitos reservados para Andrey Viccari.

## Contato
Email: viccariandrey@gmail.com <br>
Linkedin: <a href="https://www.linkedin.com/in/andrey-viccari-3a2356290/">Andrey Viccari</a>
