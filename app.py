# ?? Functions (for testing)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


# ?? Run only when executed directly (Docker)
if __name__ == "__main__":
    from http.server import SimpleHTTPRequestHandler, HTTPServer

    PORT = 5000

    class MyHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            result = f"""
            <h1>CI/CD Pipeline</h1>
            <p>Add: {add(2,3)}</p>
            <p>Subtract: {subtract(5,2)}</p>
            <p>Divide: {divide(10,2)}</p>
            """

            self.wfile.write(result.encode())

    server = HTTPServer(("0.0.0.0", PORT), MyHandler)
    print("Server running on port 5000...")
    server.serve_forever()