import os
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Get the path to the static folder (assuming it's one folder back)
    static_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
    # Get the requested file path from the HTTP request
    file_path = os.path.join(static_folder_path, req.route_params.get('route', '').lstrip('/'))
    # Check if the requested file exists
    if os.path.exists(file_path):
        # Read the file content
        with open(file_path, 'rb') as file:
            content = file.read()

        # Determine the content type based on file extension
        content_type = get_content_type(file_path)

        # Return the file content as an HTTP response
        return func.HttpResponse(content, mimetype=content_type)

    # Return a 404 response if the file is not found
    return func.HttpResponse("File not found", status_code=404)

def get_content_type(file_path):
    # Map file extensions to content types
    content_types = {
        '.html': 'text/html',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        # Add more file extensions and content types as needed
    }

    # Get the file extension
    _, extension = os.path.splitext(file_path)

    # Default content type is 'application/octet-stream'
    return content_types.get(extension.lower(), 'application/octet-stream')
