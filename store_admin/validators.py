from django.core.exceptions import ValidationError

def non_negative(value):
    if value < 0:
        raise ValidationError(f'O valor {value} não pode ser menor que 0.')
    
def above_4_digits(value):
    if value > 9999:
        raise ValidationError(f'O valor {value} não pode ter mais de 4 digitos.')