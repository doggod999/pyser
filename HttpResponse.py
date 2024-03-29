#coding=utf-8
#Author: ooaixt
#Create time: 2009-04-24

import os
import posixpath
import time

class HttpResponse():
    def __init__(self, connection):
        self.wfile = connection.makefile('wb', 0)
    
    def doGetResponse(self, url, apppath):
        file = self.getFile(url, apppath)
        if file is None:
            self.sendError(404)
            return False
        else:
            f = open(file, 'rb')
            body = f.read()
            self.sendResponse(200, file, body)
            return True
    
    def doPostResponse(self, url, apppath):
        file = self.getFile(url, apppath)
        if file is None:
            self.sendError(404)
            return False
        else:
            f = open(file, 'rb')
            body = f.read()
            self.sendResponse(200, file, body)
            return True
    
    def doHeadResponse(self, url, apppath):
        file = self.getFile(url, apppath)
        if file is None:
            self.sendError(404)
            return False
        else:
            self.sendResponse(200, file)
            return True
    
    def getFile(self, url, apppath):
        '''解析要请求的url，返回请求的文件。
        url为文件夹默认返回index.html。
                    请求的文件不存在则返回None。
        '''
        
        words = url.split('/')
        words = filter(None, words)
        path = apppath
        for word in words:
            drive, word = os.path.splitdrive(word)
            head, word = os.path.split(word)
            if word in (os.curdir, os.pardir):
                continue
            path = os.path.join(path, word)
        if not os.path.exists(path):
            return None
        
        #默认返回index.html
        if os.path.isdir(path):
            path = path + os.sep + 'index.html'
            if not os.path.exists(path):
                return None
        return path

    def sendError(self, code):
        if code in self.responses:
            message, explain = self.responses[code]
        else:
            message, explain = self.responses[400]
        body = (self.error_message % {'code': code, 'message': message, 'explain': explain})
        self.sendResponse(code, '.html', body)
    
            
    
    def sendAndFinish(self, msg):
        self.wfile.write(msg)
        self.wfile.flush()
        self.wfile.close()
    
    def finish(self):
        self.wfile.flush()
        self.wfile.close()
    
    def sendResponse(self, code, path, body=None):
        if code in self.responses:
             message = self.responses[code][0]
        else:
            message = ''
        try:    
            self.writeResponseLine(code, message)
    #        print self.date_time_string()
    #        print self.server_version
            self.writeHeader('Content-Type', self.getType(path))
            self.writeHeader('Date', self.dateTimeString())
            self.writeHeader('Server', self.server_version)
            self.writeHeader('Connection', 'close')
            if body:
                self.writeBody(body)
            self.finish()
        except:
            print 'error: (10054, "Connection reset by peer")'
    
    def writeResponseLine(self, code, message):
        self.wfile.write("%s %d %s\r\n" % (self.version, code, message))
       
        
    def writeHeader(self, keyword, value):
        self.wfile.write("%s: %s\r\n" % (keyword, value))
            
    def writeBody(self, body):
        self.wfile.write("\r\n%s" % body)
    
    
    weekdayname = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    monthname = [None,
                 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']    
    
    def dateTimeString(self, timestamp=None):
        """Return the current date and time formatted for a message header."""
        if timestamp is None:
            timestamp = time.time()
        year, month, day, hh, mm, ss, wd, y, z = time.gmtime(timestamp)
        s = "%s, %02d %3s %4d %02d:%02d:%02d GMT" % (
                self.weekdayname[wd],
                day, self.monthname[month], year,
                hh, mm, ss)
        return s
    
    def getType(self, path):
        """Return the type of a file."""

        base, ext = posixpath.splitext(path)
        if ext in self.content_type:
            return self.content_type[ext]
        ext = ext.lower()
        if ext in self.content_type:
            return self.content_type[ext]
        else:
            return self.content_type['']
    
    #服务器版本
    server_version = 'BaseServer-Python/0.1beta'
    
    #HTTP协议版本号    
    version = 'HTTP/1.1'
    
    #响应消息
    #Copy from python2.5 BaseHTTPServer.py
    responses = {
        100: ('Continue', 'Request received, please continue'),
        101: ('Switching Protocols',
              'Switching to new protocol; obey Upgrade header'),

        200: ('OK', 'Request fulfilled, document follows'),
        201: ('Created', 'Document created, URL follows'),
        202: ('Accepted',
              'Request accepted, processing continues off-line'),
        203: ('Non-Authoritative Information', 'Request fulfilled from cache'),
        204: ('No Content', 'Request fulfilled, nothing follows'),
        205: ('Reset Content', 'Clear input form for further input.'),
        206: ('Partial Content', 'Partial content follows.'),

        300: ('Multiple Choices',
              'Object has several resources -- see URI list'),
        301: ('Moved Permanently', 'Object moved permanently -- see URI list'),
        302: ('Found', 'Object moved temporarily -- see URI list'),
        303: ('See Other', 'Object moved -- see Method and URL list'),
        304: ('Not Modified',
              'Document has not changed since given time'),
        305: ('Use Proxy',
              'You must use proxy specified in Location to access this '
              'resource.'),
        307: ('Temporary Redirect',
              'Object moved temporarily -- see URI list'),

        400: ('Bad Request',
              'Bad request syntax or unsupported method'),
        401: ('Unauthorized',
              'No permission -- see authorization schemes'),
        402: ('Payment Required',
              'No payment -- see charging schemes'),
        403: ('Forbidden',
              'Request forbidden -- authorization will not help'),
        404: ('Not Found', 'Nothing matches the given URI'),
        405: ('Method Not Allowed',
              'Specified method is invalid for this server.'),
        406: ('Not Acceptable', 'URI not available in preferred format.'),
        407: ('Proxy Authentication Required', 'You must authenticate with '
              'this proxy before proceeding.'),
        408: ('Request Timeout', 'Request timed out; try again later.'),
        409: ('Conflict', 'Request conflict.'),
        410: ('Gone',
              'URI no longer exists and has been permanently removed.'),
        411: ('Length Required', 'Client must specify Content-Length.'),
        412: ('Precondition Failed', 'Precondition in headers is false.'),
        413: ('Request Entity Too Large', 'Entity is too large.'),
        414: ('Request-URI Too Long', 'URI is too long.'),
        415: ('Unsupported Media Type', 'Entity body in unsupported format.'),
        416: ('Requested Range Not Satisfiable',
              'Cannot satisfy request range.'),
        417: ('Expectation Failed',
              'Expect condition could not be satisfied.'),

        500: ('Internal Server Error', 'Server got itself in trouble'),
        501: ('Not Implemented',
              'Server does not support this operation'),
        502: ('Bad Gateway', 'Invalid responses from another server/proxy.'),
        503: ('Service Unavailable',
              'The server cannot process the request due to a high load'),
        504: ('Gateway Timeout',
              'The gateway server did not receive a timely response'),
        505: ('HTTP Version Not Supported', 'Cannot fulfill request.'),
        }
    
    #错误页面
    error_message = """\
    <html>
    <head>
    <title>ERROR PAGE</title>
    </head>
    <body>
    <h1>ERROR: %(code)d, %(message)s </h1>
    <p>Error code explanation: %(code)d = %(explain)s.
    </body>
    </html>
    """
    
    #Content-Type列表
    content_type = {
        ''        : 'application/octet-stream', #default type
        '.bmp'    : 'image/x-ms-bmp',
        '.css'    : 'text/css',
        '.doc'    : 'application/msword',
        '.exe'    : 'application/octet-stream',
        '.gif'    : 'image/gif',
        '.htm'    : 'text/html',
        '.html'   : 'text/html',
        '.jpe'    : 'image/jpeg',
        '.jpeg'   : 'image/jpeg',
        '.jpg'    : 'image/jpeg',
        '.js'     : 'application/x-javascript',
        '.mht'    : 'message/rfc822',
        '.mhtml'  : 'message/rfc822',
        '.mp3'    : 'audio/mpeg',
        '.mpeg'   : 'video/mpeg',
        '.mpg'    : 'video/mpeg',
        '.pdf'    : 'application/pdf',
        '.png'    : 'image/png',
        '.ppt'    : 'application/vnd.ms-powerpoint',
        '.swf'    : 'application/x-shockwave-flash',
        '.tar'    : 'application/x-tar',
        '.zip'    : 'application/zip',
        }
    