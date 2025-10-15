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

    def do_DELETE(self):
        """Handle DELETE requests for removing a record by ID."""
        content_size = int(self.headers.get('Content-Length', 0))
        parsed_data = self.rfile.read(content_size)
        
        # Expecting JSON input like {"id": 2}
        try:
            delete_data = json.loads(parsed_data)
        except json.JSONDecodeError:
            self.send_data({"error": "Invalid JSON format"}, status=400)
            return

        record_id = delete_data.get("id")
        if record_id is None:
            self.send_data({"error": "Missing 'id' in request body"}, status=400)
            return

        # Find and remove the record
        for record in data:
            if record["id"] == record_id:
                data.remove(record)
                self.send_data({
                    "message": f"Record with id {record_id} deleted successfully",
                    "remaining_data": data
                })
                return

        # If no record matches the id
        self.send_data({"error": f"Record with id {record_id} not found"}, status=404)

def run():
    print("Application is running on http://localhost:8080")
    server = HTTPServer(('localhost', 8080), BasicAPI)
    server.serve_forever()

if __name__ == "__main__":
    run()
