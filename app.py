from datetime import datetime

from bottle import route, run, template, app, request
from bottlemock.utils.serialize_request import Serelize_Request
from bottlemock.utils.to_file import WriteToFileLog

index_html = '''My first web app! By <strong>{{ author }}</strong>. ''' + str(datetime.now())


@route('/')
def index():
    return template(index_html, author='Real Python')


@route("/mockdefault")
def mockdefault():
    serelize_request = Serelize_Request()
    w = WriteToFileLog(serelize_request)
    w.write_to_file()
    print(serelize_request)
    print(serelize_request.get_request_headers())
    return ['OK']


@route("/bob")
def mockdefault():
    serelize_request = Serelize_Request()
    write_to_file = WriteToFileLog()
    serelize_request.get_request_headers()
    serelize_request.get_general_params()
    write_to_file.write_to_file()
    return template(index_html, author='Real Python')


if __name__ == '__main__':
    run(
        # app=StripPathMiddleware(app),
        # server='gunicorn',
        host='roma.dev',
        port='7777',
        debug=True)
