from django.core.management.utils import get_random_secret_key

def main():
    private_key = get_random_secret_key()

    print("Adicione a seguinte linha em um arquivo chamado .env na pasta core do projeto:")
    print(f"SECRET_KEY = '{private_key}'")

if __name__ == "__main__":
    main()