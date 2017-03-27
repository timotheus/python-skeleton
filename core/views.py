"""
views.py
"""
from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse, get_script_prefix
import json


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'app_root': get_script_prefix,
        'jsonify': json.dumps
    })
    return env
