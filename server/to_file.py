# coding=utf-
from datetime import datetime
import json


class WriteToFileLog:
    def __init__(self, serelize_request, body):
        self.serelize_request = serelize_request
        self.body = body

    def write_to_file(self):
        str_to_log = '\n' + str(datetime.now())
        params = json.dumps(self.serelize_request.get_general_params())
        headers = json.dumps(self.serelize_request.get_request_headers())
        body = self.body

        str_to_log = str_to_log + '\n' + 'Params: ' + params + '\n\t' \
                     + 'Headers: ' + headers + '\n' + '\n\t' + 'BODY: ' + str(body)
        dash = '-'
        str_to_log = str_to_log + dash * 100
        f = open('/app/log/bottlesite.all.log', 'a')
        f.write(str_to_log)
        f.close()
