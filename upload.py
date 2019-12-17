# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-7-29
UpdateTime: 2019-12-17
Info: 上传Excel文件
"""
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.netutil
from tornado.escape import json_encode
import os

# 解决跨域问题
def set_default_header(self):
    # 后面的*可以换成ip地址，意为允许访问的地址
    self.set_header('Access-Control-Allow-Origin', '*')
    self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
    self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')

class UploadFile(tornado.web.RequestHandler):
    def post(self):
        set_default_header(self)
        ret = {'result': 'OK'}
        files = os.path.dirname(__file__)
        print("ret.....",ret)
        print("files.....",files)
        upload_path = files + '/create'  # 生成文件的路径
        print("upload_path.....",upload_path)
        file_metas = self.request.files.get('exceldata', None)  # 提取表单中‘name’为‘exceldata’的文件元数据
        print("file_metas.....",file_metas)
        if not file_metas:
            ret['result'] = 'Invalid Args'
            print("ret.....",ret)
        else:
            for meta in file_metas:
                filename = meta['filename']
                file_path = upload_path + "/" + filename
                with open(file_path, 'wb') as up:
                    up.write(meta['body'])
        self.write(json_encode(ret))

def make_app():
    return tornado.web.Application([
        (r"/upload", UploadFile),
    ])

if __name__ =="__main__":
    port = 9088
    app = make_app()
    sockets = tornado.netutil.bind_sockets(port)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.add_sockets(sockets)
    print("Upload File Server Start Ok.....")
    tornado.ioloop.IOLoop.instance().start()