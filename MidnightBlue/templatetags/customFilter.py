from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def trimDate(value):
    return value[-4:]

@register.filter
def trim(value):
    value = str(value)
    return value[:-2]

@register.filter(is_safe=True)
def seperateGenre(value, arg):
    res = len(value.split(' '))
    argu = int(arg)
    if argu<=res and arg=="1":
        result = value.split(' ', 1)
        result = "<span class='blue'><a href='#'>" + result[0] + "</a></span>"
        return mark_safe(result)
        
    elif argu<=res and arg=="2":
        result = value.split(' ', 2)
        result = "<span class='yell'><a href='#'>" + result[1] + "</a></span>"
        return mark_safe(result)
    
    elif argu<=res and arg=="3":
        result = value.split(' ', 3)
        result = "<span class='orange'><a href='#'>" + result[2] + "</a></span>"
        return mark_safe(result)
    
    elif argu<=res and arg=="4":
        result = value.split(' ', 4)
        result = "<span class='green'><a href='#'>" + result[3] + "</a></span>"
        return mark_safe(result)
        
    elif argu<=res and arg=="5":
        result = value.split(' ', 5)
        result = "<span class='blue'><a href='#'>" + result[4] + "</a></span>"
        return mark_safe(result)
    
    elif argu<=res and arg=="6":
        result = value.split(' ', 6)
        result = "<span class='green'><a href='#'>" + result[5] + "</a></span>"
        return mark_safe(result)
        hey this is me
    else:
        result = "<span></span>"
        return mark_safe(result)