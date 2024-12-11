from rolepermissions.roles import AbstractUserRole

class Cliente(AbstractUserRole):
    role_name = 'cliente'
    available_permissions = {
        'view_product': True,
        'add_to_cart': True,
        'finish_purchase': True,
        'view_history': True,
        'send_reviews': True,
    }

class Vendedor(AbstractUserRole):
    role_name = 'vendedor'
    available_permissions = {
        'create_store': True,
        'view_orders': True,
        'add_product': True,
        'edit_product': True,
        'delete_product': True,
        'manage_stock': True,
        'respond_reviews': True,
    }