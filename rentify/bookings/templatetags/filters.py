# filters.py
from django import template

register = template.Library()


@register.filter
def calculate_total_price(booking):
    duration = (booking.end_date - booking.start_date).days + 1
    return duration * booking.booked_car.price
