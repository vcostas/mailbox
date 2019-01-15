from django.http import HttpResponseRedirect

import re

class PasswordChangeMiddleware:
    def process_request(self, request):
        if request.user.is_authenticated and \
            re.match(r'^/?', request.path) and \
            not re.match(r'^/change_password/?', request.path):

            profile = request.user.profile
            if profile.force_password_change:
                return HttpResponseRedirect('/change_password/')