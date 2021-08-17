from day_7.queryset_methods.models import Order, Customer

def get_order_count_by_customer(name):
    """Возвращает количества заказов по имени покупателя

    Args:
        name: имя покупателя

    Returns: число заказов (не может быть отрицательным, но может быть нулевым)
    """
    
    customer = Customer.objects.filter(name=name).values("id").first()

    if customer is None:
       order_count = 0
    else:
       order_count = Order.objects.filter(customer=customer["id"]).count()

    return order_count
