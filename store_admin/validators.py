from django.core.exceptions import ValidationError

def nao_negativo(value):
    if value < 0:
        raise ValidationError(f'O valor {value} não pode ser menor que 0.')
    
def valor_acima_4_digitos(value):
    if value > 9999:
        raise ValidationError(f'O valor {value} não pode ter mais de 4 digitos.')