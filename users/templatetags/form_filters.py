from django import template
import shlex

register = template.Library()


@register.filter(name="add_class")
def add_class(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name="add_attrs")
def add_attrs(field, arg):
    """
    Adds multiple HTML attributes to Django form fields via a string like:
    class="form-control" oninvalid="..." oninput="..."
    """
    attrs = {}
    try:
        parts = shlex.split(arg)
        for part in parts:
            key, value = part.split("=", 1)
            attrs[key] = value.strip('"')
    except Exception as e:
        print(f"Error in add_attrs filter: {e}")
    return field.as_widget(attrs=attrs)


@register.filter(name="add_class_and_attrs")
def add_class_and_attrs(field, args):
    class_name, attrs_str = args.split("|", 1)
    attrs = dict(item.split("=") for item in attrs_str.split(","))
    attrs["class"] = class_name
    return field.as_widget(attrs=attrs)
