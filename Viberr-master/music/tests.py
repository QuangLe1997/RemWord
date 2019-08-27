from django.test import TestCase

# Create your tests here.
from google_images_download import google_images_download

# creating object
response = google_images_download.googleimagesdownload()

search_queries = ['đẩy lùi',]


def downloadimages(query):
    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit": 4,
                 "print_urls": True,
                 "size": "medium",
                 "aspect_ratio": panoramic }
    try:
        response.download(arguments)

        # Handling File NotFound Error
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit": 4,
                     "print_urls": True,
                     "size": "medium"}

        # Providing arguments for the searched query
        try:
            # Downloading the photos based
            # on the given arguments
            response.download(arguments)
        except:
            pass
# Driver Code
for query in search_queries:
    downloadimages(query)
    print()
