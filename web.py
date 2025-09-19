from http.server import HTTPServer,BaseHTTPRequestHandler
content ='''<!DOCTYPE html>
<html lang="en">
<head>
  
 
  <title>TCP/IP Model</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      background-color: #f4f4f4;
      color: #333;
    }

    header {
      background-color: #004080;
      color: white;
      padding: 7px;
      text-align: center;
    }

    main {
      padding: 20px;
      max-width: 900px;
      margin: auto;
    }

    h2 {
      color: #004080;
    }

    .model-diagram {
      display: flex;
      flex-direction: column;
      width: 300px;
      margin: 20px auto;
      border: 2px solid #004080;
    }

    .layer {
      padding: 10px;
      text-align: center;
      border-bottom: 1px solid #ccc;
      background-color: #e0ecff;
    }
  </style>
</head>
<body>

  <header>
    <h1>TCP/IP Model</h1>
  </header>

  <main>

    <section>
      <h2>What is the TCP/IP Model?</h2>
      <p>The TCP/IP model is a set of communication protocols used to interconnect network devices on the internet. It stands for <strong>Transmission Control Protocol/Internet Protocol</strong>. Developed by the U.S. Department of Defense, it is the foundational model for data communication over networks.</p>
    </section>

    <section>
      <h2>Layers of the TCP/IP Model</h2>
      <div class="model-diagram">
        <div class="layer"><strong>Application Layer</strong><br> (e.g., HTTP, FTP, DNS)</div>
        <div class="layer"><strong>Transport Layer</strong><br> (e.g., TCP, UDP)</div>
        <div class="layer"><strong>Internet Layer</strong><br> (e.g., IP, ICMP)</div>
        <div class="layer"><strong>Network Access Layer</strong><br> (e.g., Ethernet, Wi-Fi)</div>
      </div>
    </section>

    <section>
      <h2>Comparison with OSI Model</h2>
      <p>The OSI model has 7 layers, whereas the TCP/IP model has only 4. Here's a brief comparison:</p>
      <ul>
        <li><strong>Application (TCP/IP)</strong> = Application, Presentation, Session (OSI)</li>
        <li><strong>Transport</strong> = Transport (OSI)</li>
        <li><strong>Internet</strong> = Network (OSI)</li>
        <li><strong>Network Access</strong> = Data Link + Physical (OSI)</li>
      </ul>
    </section>
  </main>
</body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address=('',8000)
httpd=HTTPServer(server_address,MyServer)
httpd.serve_forever()