from django.utils.deprecation import MiddlewareMixin
from time import time

class FakeUser:
    def __init__(self, auth=None):
        self.auth = auth

    # определите у пользователя аттрибуты auth
   
    
# Необходимо изменить поведение указанных методов.
# Помните про __call__()
class MyMiddleware(MiddlewareMixin):
    
    def __call__(self, request):
        start = time()
        response = self.process_request(request)
        self.process_response(request, response)
        end = time()
        runtime = end - start
        request.runtime = runtime
        return response

    def process_request(self, request):
        user = FakeUser()
        if request.auth == 'VALID_TOKEN':
           user.auth = True
        elif request.auth == 'INVALID_TOKEN':
           user.auth = False    

        request.auth = user.auth
                             
        return self.get_response(request)
                                                                  
    def process_response(self, request, response):
        
        return response
