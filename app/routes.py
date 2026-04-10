import math
from flask import Blueprint, current_app, render_template, request
from app.services.product_service import get_products

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/products")
def products():
    query = request.args.get("q", "").strip()
    page = request.args.get("page", default=1, type=int)

    if page is None or page < 1:
        page = 1

    page_size = current_app.config["PRODUCTS_PER_PAGE"]

    result = get_products(
        page=page,
        query=query,
        page_size=page_size,
        base_url=current_app.config["PRODUCTS_API_BASE_URL"],
        timeout=current_app.config["REQUEST_TIMEOUT"],
    )

    total = result["total"]
    total_pages = max(1, math.ceil(total / page_size)) if total else 1

    if page > total_pages:
        page = total_pages
        result = get_products(
            page=page,
            query=query,
            page_size=page_size,
            base_url=current_app.config["PRODUCTS_API_BASE_URL"],
            timeout=current_app.config["REQUEST_TIMEOUT"],
        )
        total = result["total"]
        total_pages = max(1, math.ceil(total / page_size)) if total else 1

    return render_template(
        "products.html",
        products=result["products"],
        query=query,
        current_page=page,
        total_pages=total_pages,
        error_message=result["error_message"],
    )