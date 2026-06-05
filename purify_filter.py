import requests

def run_purify_filter():
    print("Opening filter gates... straining system noise.")
    
    # A reliable public live-signal checkpoint
    target_url = "https://api.github.com"
    
    try:
        response = requests.get(target_url)
        # 200 means a perfectly clear, successful connection
        if response.status_code == 200:
            print("✨ Signal is pure. System chaos successfully filtered.")
            return True
        else:
            print(f"⚠️ Variance detected. Signal block code: {response.status_code}")
    except Exception as e:
        print(f"❌ Structural friction encountered: {e}")
    
    return False

if __name__ == "__main__":
    run_purify_filter()

