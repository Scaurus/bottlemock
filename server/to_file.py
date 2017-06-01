# coding=utf-
from datetime import datetime
import json


class WriteToFileLog:
    def __init__(self, serelize_request):
        self.serelize_request = serelize_request

    def write_to_file(self):
        str_to_log = '\n' + str(datetime.now())
        params = json.dumps(self.serelize_request.get_general_params())
        headers = json.dumps(self.serelize_request.get_request_headers())

        str_to_log = str_to_log + '\n' + 'Params: ' + params + '\n\t' + 'Headers: ' + headers + '\n'
        dash = '-'
        str_to_log = str_to_log + dash * 100
        f = open('/var/log/bottlesite.all.log', 'a')
        f.write(str_to_log)
        f.close()
