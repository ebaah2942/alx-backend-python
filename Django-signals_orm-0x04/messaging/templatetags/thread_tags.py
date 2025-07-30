from django import template
register = template.Library()

@register.inclusion_tag('messaging/thread.html')
def render_thread(message):
    return {'message': message}
