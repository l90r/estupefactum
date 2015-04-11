from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def top_menu(context):
	items = (
		('home', "The Word of Today", {}),
		('recent', 'Recent', {}),
		('submit', 'Submit', {}),
		('contributors', 'Contributors', {}),
		('page', 'About', {'slug': 'about'})
	)
	result = '<ul class="nav navbar-nav">'
	current_name = context['view_name']
	for (name, title, kwargs) in items:
		url = reverse(name, kwargs=kwargs)
		active = ' class="active"' if name == current_name else ''
		result += '<li{}><a href="{}">{}</a></li>'.format(active, url, title)
	result += '</ul>'
	return result


