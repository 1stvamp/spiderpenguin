import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from spiderpenguin.lib.base import BaseController, render

log = logging.getLogger(__name__)

class MainController(BaseController):

    def index(self):
        # Return a rendered template
        return render('/index.mako')


    def spin(self, direction):
        if direction == 'left':
            pass
        else:
            pass

        # Return a rendered template
        return render('/index.mako')


    def flippers(self, direction):
        if direction == 'up':
            pass
        else:
            pass

        # Return a rendered template
        return render('/index.mako')


    def eyes(self, action):
        if action == 'open':
            pass
        elif action == 'half':
            pass
        else:
            pass

        # Return a rendered template
        return render('/index.mako')


    def led(self, action):
        if action == 'on':
            pass
        elif action == 'off':
            pass
        else:
            pass

        # Return a rendered template
        return render('/index.mako')


    def speak(self, text):
        # Return a rendered template
        return render('/index.mako')
