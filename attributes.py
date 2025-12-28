import re

def detect_style(image_url):
    url = image_url.lower()

    if "aviator" in url:
        return "Aviator"
    if "round" in url:
        return "Round"
    if "rectangle" in url or "rectangular" in url:
        return "Rectangle"
    if "rimless" in url:
        return "Rimless"
    if "cat" in url:
        return "Cat Eye"
    if "wayfarer" in url:
        return "Wayfarer"
    if "square" in url:
        return "Square"
    if "transparent" in url:
        return "Transparent Frame"

    return "Generic Eyewear"
