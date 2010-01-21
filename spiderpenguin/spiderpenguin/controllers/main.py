# coding=UTF-8

import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from spiderpenguin.lib.base import BaseController, render

from spiderpenguin.lib.tuxsh import *
from tuxisalive.api import SPV_VERYSLOW, SPV_SLOW, SPV_NORMAL, SPV_FAST, SPV_VERYFAST, LFX_NONE, LFX_FADE, LFX_STEP


log = logging.getLogger(__name__)

class MainController(BaseController):

    def index(self):
        # Return a rendered template
        return render('/index.mako')


    def spin(self, id):
        if id == 'left':
            tux.spinning.leftOn()
        elif id == 'right':
            tux.spinning.rightOn()

        # Return a rendered template
        return render('/index.mako')


    def flippers(self, id):
        if id == 'up':
            tux.flippers.up()
        elif id == 'down':
            tux.flippers.down()

        # Return a rendered template
        return render('/index.mako')


    def eyes(self, id):
        if id == 'open':
            tux.eyes.open()
        elif id == 'half':
            pass
        elif id == 'closed':
            tux.eyes.close()

        # Return a rendered template
        return render('/index.mako')


    def led(self, id):
        eyes = request.GET.get('eyes', 'both')
        if eyes not in ('both', 'left', 'right'):
            eyes = 'both'
        tux_eyes = getattr(tux.led, eyes)
        if id == 'on':
            tux_eyes.on()
        elif id == 'off':
            tux_eyes.off()
        elif id == 'blink':
            tux_eyes.blink()

        # Return a rendered template
        return render('/index.mako')


    def speak(self, id):
        tux.tts.speak(id)
        # Return a rendered template
        return render('/index.mako')
