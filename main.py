import subprocess
import re
import create_gist
import global_variables


def main():
    # Command to start the cloudflared server
    command = [global_variables.CLOUDFLARED_PATH, "tunnel", "--url", global_variables.URL]

    # Start the subprocess
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Regex pattern to match the URL
    url_pattern = r"https://[a-zA-Z0-9\-]+\.trycloudflare\.com"

    while True:
        # Read a line from stderr (cloudflared logs to stderr)
        line = process.stderr.readline()

        # Print the line (for debugging)
        print(line, end="")

        # Search for the URL in the line
        match = re.search(url_pattern, line)

        if match:
            url = match.group(0)
            print("\n\n")
            create_gist.publish_link_gist(url)
            print("\n\n")


if __name__ == "__main__":
    main()
