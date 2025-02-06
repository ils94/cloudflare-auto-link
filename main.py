import subprocess
import re
import create_bin

# Command to start the cloudflared server
command = ["cloudflared/cloudflared-windows-amd64.exe", "tunnel", "--url", "http://127.0.0.1:5000"]

# Start the subprocess
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Regex pattern to match the URL
url_pattern = r"https://[a-zA-Z0-9\-]+\.trycloudflare\.com"

# Read output line by line
url_found = False

while True:
    # Read a line from stderr (cloudflared logs to stderr)
    line = process.stderr.readline()
    if not line:
        break  # Exit loop when process ends

    # Print the line (for debugging)
    print(line, end="")

    # Search for the URL in the line
    match = re.search(url_pattern, line)
    if match and not url_found:
        url = match.group(0)
        print("\nExtracted URL:", url)
        create_bin.publish_link_jsonbin(url)
        url_found = True

# Wait for the process to finish
process.wait()

if not url_found:
    print("URL not found in the output.")
