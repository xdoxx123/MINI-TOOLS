import subprocess
import re
import colorama
def get_profiles():
    result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'],
                            capture_output=True, text=True)
    profiles = re.findall(r"All User Profile\s*:\s(.*)", result.stdout)
    return [profile.strip() for profile in profiles]

def get_password(profile):
    result = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'],
                            capture_output=True, text=True)
    match = re.search(r"Key Content\s*:\s(.*)", result.stdout)
    return match.group(1).strip() if match else "N/A"

