import subprocess

def get_wifi_passwords():
    # Get a list of all saved WiFi profiles
    profiles_data = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
    profiles = [line.split(":")[1].strip() for line in profiles_data.stdout.split("\n") if "All User Profile" in line]

    wifi_passwords = {}

    for profile in profiles:
        # Get the password for each profile
        profile_info = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], capture_output=True, text=True)
        for line in profile_info.stdout.split("\n"):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                wifi_passwords[profile] = password
                break
        else:
            wifi_passwords[profile] = "No password found"

    return wifi_passwords

if __name__ == "__main__":
    passwords = get_wifi_passwords()
    for wifi, password in passwords.items():
        print(f"WiFi: {wifi} | Password: {password}")
