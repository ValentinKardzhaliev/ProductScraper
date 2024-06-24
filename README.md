# Product Info Scraper

A web scraper to extract product information from a website using Scrapy and Selenium.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- Git
- Google Chrome (for Selenium)

### Installation

1. **Clone the repository:**

2. **Set up a virtual environment:**

    ```sh
    # On Windows
    python -m venv venv
    venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

### Running the Scraper

To run the Scrapy spider, use the following command:

```sh
scrapy crawl product_scraper

