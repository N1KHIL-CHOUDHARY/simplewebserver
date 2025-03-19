from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<html>
<head>
    <title>TCP/IP Layers</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
            margin: 0;
        }
        .container {
            text-align: center;
        }
        .layer {
            width: 300px;
            padding: 15px;
            margin: 10px auto;
            border-radius: 8px;
            color: white;
            font-size: 18px;
            font-weight: bold;
        }
        .application { background-color: #ff5733; }
        .transport { background-color: #33b5e5; }
        .internet { background-color: #2ecc71; }
        .network { background-color: #8e44ad; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Types of TCP/IP Layers</h2>
        <div class="layer application">Application Layer</div>
        <div class="layer transport">Transport Layer</div>
        <div class="layer internet">Internet Layer</div>
        <div class="layer network">Network Access Layer</div>
    </div>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()