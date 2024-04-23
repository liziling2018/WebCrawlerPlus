```python
# Configuration file for WebCrawlerPlus

# Target website URL
URL = 'https://www.example.com'

# Data to extract
DATA = {
    'title': {
        'selector': 'h1',
        'attribute': 'text'
    },
    'description': {
        'selector': 'p',
        'attribute': 'text'
    }
}

# Additional settings
MAX_PAGES = 10  # Maximum number of pages to crawl
OUTPUT_FILE = 'data.csv'  # Output file for storing the extracted data
