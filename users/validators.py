import re
from django.core.exceptions import ValidationError

def validate_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValidationError("Tamanho do CPF inválido ou caracteres não numéricos encontrados.")
    if cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido com todos os dígitos idênticos.")
    for i in range(9, 11):
        value = sum((int(cpf[num]) * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != int(cpf[i]):
            raise ValidationError("CPF inválido.")

def validate_phone(phone: str) -> bool:
    pattern = re.compile(r'^\(?\d{2}\)?[\s-]?\d{4,5}[\s-]?\d{4}$')
    if not pattern.match(phone):
        raise ValidationError("Formato de telefone inválido.")

def validate_password(password: str) -> bool:
    if len(password) < 8:
        raise ValidationError("Senha precisa ter no mínimo 8 caracteres.")
    if not re.search(r'[A-Z]', password):
        raise ValidationError("Senha precisa ter no mínimo uma letra maiúscula.")
    if not re.search(r'[a-z]', password):
        raise ValidationError("Senha precisa ter no mínimo uma letra minúscula.")
    if not re.search(r'[0-9]', password):
        raise ValidationError("Senha precisa ter no mínimo um número.")
    if not re.search(r'[\W_]', password):
        raise ValidationError("Senha precisa ter no mínimo um caractere especial.")
