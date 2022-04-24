#!/var/www/html/public/venv/bin/python
#: optional path to your local python site-packages folder
#import sys
#sys.path.insert(0, '/var/www/html/public/venv/lib/python/site-packages')

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain;charset=utf-8')])
    return ['Hello World!\n']

#if __name__ == '__main__':
#    from flipflop import WSGIServer
#    WSGIServer(application).run()
