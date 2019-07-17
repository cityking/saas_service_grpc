import json
class DataGetMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'GET':
            request.data = request.GET.dict()
        elif request.method == 'POST':
            try:
                data = request.body.decode()
                data = json.loads(data)
                request.data = data
            except:
                request.data = request.POST.dict()
        else:
            try:
                data = request.body.decode()
                data = json.loads(data)
                request.data = data
            except:
                request.data = {}


        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Headers'] = 'X-Requested-With, X_Requested_With, Content-Type'
        response['Access-Control-Allow-Origin'] = '*'

        return response
