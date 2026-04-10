# Products Table Application

## Overview

This project is a backend-driven web application that displays a list of products retrieved from the DummyJSON API.
The application supports search and pagination, with all dynamic behavior handled on the backend.

---

## Installation Instructions

### Prerequisites

* Python 3.12 (or compatible version)
* pip

### Setup

1. Clone the repository:

```bash
git clone https://github.com/Yael0001/products-app.git
cd products-app
```

2. Create and activate a virtual environment:

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python run.py
```

5. Open your browser and navigate to:

```text
http://127.0.0.1:5000/products
```

---

## How the Application Works

The application follows a server-side rendering approach using Flask.

### Backend Flow

* The client sends a request to `/products` with optional query parameters:

  * `page` – current page number
  * `q` – search query
* The backend processes the request and calls the DummyJSON API:

  * `/products` for regular listing
  * `/products/search` for search queries
* Pagination is handled using the API’s `limit` and `skip` parameters
* The backend calculates pagination metadata (total pages, current page)
* Data is passed to Jinja templates and rendered as HTML

### Frontend Behavior

* The UI is rendered using Jinja templates.
* A search form submits requests to the backend using GET parameters
* Pagination links trigger backend requests
* A small JavaScript module handles the "Gallery" feature:

  * Clicking the button inserts a row below the product
  * Displays up to 3 product images

---

## Configuration

The application uses a centralized configuration (`config.py`) to control key behaviors:

* `PRODUCTS_PER_PAGE` – defines how many products are displayed per page (default: 10)
  → This value directly affects pagination logic and API requests (`limit` and `skip`)

* `PRODUCTS_API_BASE_URL` – base URL for the external products API
  → Used to construct both listing and search requests

* `REQUEST_TIMEOUT` – timeout (in seconds) for API calls
  → Prevents the application from hanging if the external service is slow or unavailable

Centralizing these values allows changes to application behavior without modifying business logic. 
While pagination size and timeout can be adjusted freely, the base API URL assumes a compatible API structure.

---

## Assumptions & Design Decisions

### Backend-driven logic

All dynamic features (data retrieval, search, pagination) are implemented on the backend.

### Use of DummyJSON search endpoint

Search functionality is implemented using the API’s `/search` endpoint rather than local filtering.

### Pagination via API

Pagination is handled using the API’s `limit` and `skip` parameters instead of slicing data locally.
The page size is controlled via the `PRODUCTS_PER_PAGE` configuration.

### Handling invalid page values

If a requested page exceeds the available number of pages, the application falls back to the last valid page and re-fetches the data.

### Template structure

The page template is split into smaller partials (search, table, pagination) to improve readability and maintainability, while also laying a foundation for future reuse.

### Responsiveness

Basic responsive adjustments were added to improve usability on smaller screens.
Given the table-heavy layout, horizontal scrolling was preferred over restructuring the layout to maintain clarity and simplicity.

### Error handling

The application handles API failures gracefully by displaying a user-friendly message instead of crashing.

---