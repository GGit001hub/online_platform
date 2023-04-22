from rest_framework import renderers
import json


class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        respons = ''
        if 'ErrorDetail' in str(data):
            respons = json.dumps({'errors':data})
        else:
            respons = json.dumps(data)

        return respons 