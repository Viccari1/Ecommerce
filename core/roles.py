from rolepermissions.roles import AbstractUserRole

class Cliente(AbstractUserRole):
    role_name = 'cliente'
    available_permissions = {
        'view_product': True,
        'add_to_cart': True,
        'finish_purchase': True,
        'view_history': True,
    }

class Vendedor(AbstractUserRole):
    role_name = 'vendedor'
    available_permissions = {
        'view_orders': True,
        'add_product': True,
        'edit_product': True,
        'delete_product': True,
        'view_sales': True,
    }