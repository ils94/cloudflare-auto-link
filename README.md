# **🌐 Cloudflare Tunnel Distributor**

Ever used the **free Cloudflare Tunnel**, but got tired of manually copying the new link every time? Well, not anymore! 🎉

This script **automates everything**, it launches `cloudflared`, grabs the generated tunnel URL, and updates a **private Gist** for easy access. Now, your apps or scripts can **always fetch the latest link** without lifting a finger! 🤖✨

## **🚀 How It Works**

1.  The script starts a **Cloudflare Tunnel**.
2.  It extracts the generated **temporary URL**.
3.  It updates the URL in a **private GitHub Gist**, keeping it always accessible.
4.  Your app can fetch the latest link via a simple **API request**.

## **🔧 Setup Guide**

### **1️⃣ Install Dependencies**

Make sure you have **Python 3.x** installed. Then, install the required packages:

```bash
pip install requests python-dotenv
```

### **2️⃣ Install Cloudflare Tunnel**

Download and install `cloudflared`:

-   **Linux/macOS:**
    
    ```bash
    sudo apt install cloudflared  # or brew install cloudflared
    ```
    
-   **Windows:** [Download it here](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/) and add it to your system PATH.

### **3️⃣ Create a GitHub Personal Access Token**

1.  Go to [GitHub Developer Settings](https://github.com/settings/tokens).
2.  Click **Generate new token (classic)** and select:
    -   **gist** (Read & Write access)
3.  Copy and save the token securely (you won’t see it again).

### **4️⃣ Create a Private Gist**

1.  Go to [GitHub Gist](https://gist.github.com/).
2.  Click **New Gist**, name it `cloudflare_tunnel.json`, and set it to **Secret**.
3.  Add `{ "cloudflare_link": "" }` as the content and create the Gist.
4.  Copy the **Gist ID** from the URL (`https://gist.github.com/YOUR_GITHUB_USERNAME/YOUR_GIST_ID`).

### **5️⃣ Create a `.env` File**

Inside your project folder, create a `.env` file and add:

```
GITHUB_TOKEN=your_github_token
GIST_ID=your_gist_id
CLOUDFLARED_PATH=path/to/your/cloudflared  # Leave as "cloudflared" if it's installed in the OS PATH
URL=http://127.0.0.1:XXXXX  # Replace "XXXXX" with the actual port number
```

### **6️⃣ Run the Script!**

```bash
python main.py
```

👉 The Cloudflare Tunnel will start, and the script will automatically update the Gist with the latest URL. 🎉

Now, your apps can **always** access the latest Cloudflare Tunnel link automatically! 🚀

## **🎯 Why Use This?**

👉 No more **manually copying** Cloudflare Tunnel links.  
👉 Keep the latest URL **accessible** via API.  
👉 **Automate hosting** for temporary servers.  
👉 Works on **Windows, macOS, and Linux**.

Start hosting with **Cloudflare Tunnels the easy way!** 🎉🚀
