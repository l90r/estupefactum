from django import template

register = template.Library()

@register.filter()
def form_control(field):
	return field.as_widget(attrs={'class': 'form-control'})
