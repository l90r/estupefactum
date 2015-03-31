from django import template

register = template.Library()

@register.filter()
def form_control(field):
	return field.as_widget(attrs={'class': 'form-control'})

@register.inclusion_tag('_form_body.html')
def form_body(form):
	return {'form': form}