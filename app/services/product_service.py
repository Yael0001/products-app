import requests

def get_products(page, query, page_size, base_url, timeout=5):
    skip = (page - 1) * page_size

    if query:
        url = f"{base_url}/search"
        params = {
            "q": query,
            "limit": page_size,
            "skip": skip,
        }
    else:
        url = base_url
        params = {
            "limit": page_size,
            "skip": skip,
        }

    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()

        data = response.json()

        return {
            "products": data.get("products", []),
            "total": data.get("total", 0),
            "error_message": None,
        }

    except requests.RequestException:
        return {
            "products": [],
            "total": 0,
            "error_message": "Failed to load products. Please try again later.",
        }