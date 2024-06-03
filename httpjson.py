from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
import cgi

'''
  Mon Jun  3 14:54:40 2024 

  # How to run it 
  python3 httpjson.py 8000

  # GET
  curl http://localhost:8000

  # POST
  curl -X POST http://localhost:8000 -H 'Content-Type: application/json' -d '{"key1" : "From client"}' 

  Get json from client 
  {'key1' : 'Get JSON'}

  Reply json to client 
  {'key1' : 'Reply from Server'}
'''

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()
        response = json.dumps({'hello': 'world', 'received': 'ok'})
        byteResp = bytes(response, 'utf-8')
        self.wfile.write(byteResp)
        
    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        
        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
            
        # read the message and convert it into a python dictionary
        length = int(self.headers.get('content-length'))
        payload_str = self.rfile.read(length).decode('utf-8') 
        jsonPayload = json.loads(payload_str) 
        print('jsonPayload=>', jsonPayload)
        jsonPayload['key1'] = 'Reply from Server'
        
        # send the message back
        self._set_headers()
        self.wfile.write(bytes(json.dumps(jsonPayload), 'utf-8'))
        
def run(server_class=HTTPServer, handler_class=Server, port=8008):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print('Starting httpd on port %d...' % port)
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
        
