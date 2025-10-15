from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Initial dummy data to simulate a database
data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=200):
        """Helper function to send JSON responses."""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())


    # def do_GET(self):
    #     """Return all data records."""
    #     self.send_data({
    #         "message": "Data retrieved successfully",
    #         "data": data
    #     })
        
    def do_PUT(self):
        """Handle PUT requests for updating data."""
        content_size = int(self.headers.get('Content-Length', 0))
        parsed_data = self.rfile.read(content_size)
        put_data = json.loads(parsed_data)

        # Expecting JSON with an 'id' field to identify what to update
        record_id = put_data.get("id")
        if record_id is None:
            self.send_data({"error": "Missing 'id' in request body"}, status=400)
            return

        # Find and update the record
        for record in data:
            if record["id"] == record_id:
                record.update(put_data)
                self.send_data({
                    "message": "Data updated successfully",
                    "updated_data": record
                })
                return

        # If not found, return 404
        self.send_data({"error": f"Record with id {record_id} not found"}, status=404)


def run():
    print("Application is running on http://localhost:8080")
    server = HTTPServer(('localhost', 8080), BasicAPI)
    server.serve_forever()


if __name__ == "__main__":
    run()
