from django import template
import json

register = template.Library()


@register.filter(name='add_attr')
def add_attr(field, attr):
    attr = attr.replace('field.name', field.name)
    attr = attr.replace('field.id', field.auto_id)
    dict = json.loads(attr)
    if 'class' in dict and field.field.widget.input_type == "checkbox":
        dict['class'] = 'form-check'
    return field.as_widget(attrs=dict)
