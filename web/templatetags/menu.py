from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def top_menu():
	items = (
		('home', "Today's word"),
		('recent', 'Recent'),
		('submit', 'Submit'),
		('contributors', 'Contributors'),
	)
	result = '<ul class="nav navbar-nav">'
	current_name = 'home'
	for (name, title) in items:
		url = reverse(name)
		active = ' class="active"' if name == current_name else ''
		result += '<li{}><a href="{}">{}</a></li>'.format(active, url, title)
	result += '</ul>'
	return result


