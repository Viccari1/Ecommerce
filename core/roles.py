from rolepermissions.roles import AbstractUserRole

class Client(AbstractUserRole):
    role_name = 'client'
    available_permissions = {
        'view_product': True,
        'add_to_cart': True,
        'finish_purchase': True,
        'view_history': True,
        'send_reviews': True,
    }

class Seller(AbstractUserRole):
    role_name = 'seller'
    available_permissions = {
        'create_store': True,
        'view_orders': True,
        'add_product': True,
        'edit_product': True,
        'delete_product': True,
        'manage_stock': True,
        'respond_reviews': True,
    }