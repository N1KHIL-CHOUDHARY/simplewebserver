# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
"""
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
"""

## OUTPUT:
![alt text](<Screenshot (20).png>)
![alt text](<Screenshot (21).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
