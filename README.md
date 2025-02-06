# **🌐 Cloudflare Tunnel Distributor**  
Ever used the **free Cloudflare Tunnel**, but got tired of manually copying the new link every time? Well, not anymore! 🎉  

This script **automates everything**, it launches `cloudflared`, grabs the generated tunnel URL, and updates a private JSONBin for easy access. Now, your apps or scripts can **always fetch the latest link** without lifting a finger! 🤖✨  

## **🚀 How It Works**  
1. The script starts a **Cloudflare Tunnel**.  
2. It extracts the generated **temporary URL**.  
3. It updates the URL in **JSONBin**, keeping it always accessible.  
4. Your app can fetch the latest link via a simple **API request**.  

## **🔧 Setup Guide**  

### **1️⃣ Install Dependencies**  
Make sure you have **Python 3.x** installed. Then, install the required packages:  
```bash
pip install requests python-dotenv
```

### **2️⃣ Install Cloudflare Tunnel**  
Download and install `cloudflared`:  
- **Linux/macOS:**  
  ```bash
  sudo apt install cloudflared  # or brew install cloudflared
  ```
- **Windows:** [Download it here](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/) and add it to your system PATH.

### **3️⃣ Create a JSONBin Account**  
1. Go to [JSONBin.io](https://jsonbin.io/) and create a free account.  
2. Click **Create a New Bin**, add `{ "cloudflare_link": "" }`, and save it.  
3. Copy the **Bin ID** from the URL (`https://jsonbin.io/b/YOUR_BIN_ID`).  
4. Get your **API Key** from the **Developer Settings**.

### **4️⃣ Create a `.env` File**  
Inside your project folder, create a `.env` file and add:  
```
API_KEY=your_jsonbin_api_key
BIN_ID=your_bin_id
```

### **5️⃣ Run the Script!**  
```bash
python main.py
```

✅ The Cloudflare Tunnel will start, and the script will automatically update the JSONBin with the latest URL. 🎉  

Now, your apps can **always** access the latest Cloudflare Tunnel link automatically! 🚀  

## **🎯 Why Use This?**  
✅ No more **manually copying** Cloudflare Tunnel links.  
✅ Keep the latest URL **accessible** via API.  
✅ **Automate hosting** for temporary servers.  
✅ Works on **Windows, macOS, and Linux**.  

Start hosting with **Cloudflare Tunnels the easy way!** 🎉🚀
