import threading
import webbrowser
import BaseHTTPServer
import SimpleHTTPServer
import csv_to_graph_json 
import json 

FILE = 'upload.html'
PORT = 8080


class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """The test example handler."""

    def do_POST(self):
        """Handle a post request by returning the square of the number."""
        length = int(self.headers.getheader('content-length'))
        data_string = self.rfile.read(length)
        try:
            # result = int(data_string) ** 2
            result = data_string
            # result = "I just changed this! Congrats!"
            with open("upload.txt", "w") as text_file:
                text_file.write(data_string)
            
            try:
                csv_to_graph_json.main("upload.txt")
                result = "Success!"
            except:
                result = "alert(\"Unable to load file\")"

        except:
            result = 'error'


        #send the result back to the server 
        self.wfile.write(result)


def open_browser():
    """Start a browser after waiting for half a second."""
    def _open_browser():
        webbrowser.open('http://localhost:%s/%s' % (PORT, FILE))
    thread = threading.Timer(0.5, _open_browser)
    thread.start()

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, TestHandler)
    server.serve_forever()


''' When file is called from command line ''' 


if __name__ == "__main__":
    open_browser()
    start_server()
