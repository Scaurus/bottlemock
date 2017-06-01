# coding=utf-8
from bottle import request, response


class Serelize_Request:
    def __init__(self):
        self.dict_general = {
            "Request_URL": None,
            "Request_Method": None,
            "Status_Code": None,
            "Remote_Address": None,
            "Server": None,
            "Server_name": None,
            "Remote_host": None,
            "Server_port": None,
            "Server_protocol": None,
        }

        self.dict_request_headers = {
            "Accept": None,
            "Accept-Encoding": None,
            "Accept-Language": None,
            "Cache-Control": None,
            "Connection": None,
            "Content-Type": None,
            "Cookie": None,
            "Host": None,
            "Upgrade-Insecure-Requests": None,
            "User-Agent": None,
            "X-Compress": None,
        }

    def get_request_headers(self):
        for i in self.dict_request_headers.keys():
            self.dict_request_headers[i] = request.get_header(i)
        print(self.dict_request_headers)
        return self.dict_request_headers

    def get_general_params(self):
        self.dict_general['Request_URL'] = request.environ['PATH_INFO']
        self.dict_general['Request_Method'] = request.environ['REQUEST_METHOD']
        self.dict_general['Remote_Address'] = request.environ['REMOTE_ADDR']
        self.dict_general['Server'] = request.environ['SERVER_SOFTWARE']
        self.dict_general['Server_name'] = request.environ['SERVER_NAME']
        self.dict_general['Remote_host'] = request.environ['REMOTE_HOST']
        self.dict_general['Server_port'] = request.environ['SERVER_PORT']
        self.dict_general['Server_protocol'] = request.environ['SERVER_PROTOCOL']
        self.dict_general['Status_Code'] = response.status

        print(self.dict_general)
        return self.dict_general



