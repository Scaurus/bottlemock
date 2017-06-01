from datetime import datetime

from bottle import route, run, template, post, get

from to_file import WriteToFileLog
from serialize_request import Serelize_Request

index_html = '''My first web app! By <strong>{{ author }}</strong>. ''' + str(datetime.now())


@route('/')
def index():
    return template(index_html, author='Real Python')


@route("/mockdefault")
def mockdefault():
    serelize_request = Serelize_Request()
    w = WriteToFileLog(serelize_request)
    w.write_to_file()
    return ['OK']


@post("/rpc/communication.sendMail")
def mockdefault():
    serelize_request = Serelize_Request()
    w = WriteToFileLog(serelize_request)
    w.write_to_file()
    return ['OK']


@get("/rpc/communication.sendMail")
def mockdefault():
    serelize_request = Serelize_Request()
    w = WriteToFileLog(serelize_request)
    w.write_to_file()
    return ['OK']


@route("/bob")
@post("/bob")
def mockdefault():
    serelize_request = Serelize_Request()
    w = WriteToFileLog(serelize_request)
    w.write_to_file()
    return template(index_html, author='Real Python')


if __name__ == '__main__':
    run(
        host='0.0.0.0',
        port='7777',
        debug=True)
