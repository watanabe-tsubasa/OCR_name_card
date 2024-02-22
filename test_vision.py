
# Imports the Google Cloud client library
from google.cloud import vision
from google.oauth2 import service_account

def run_quickstart() -> vision.EntityAnnotation:
    """Provides a quick start example for Cloud Vision."""
    credentials = service_account.Credentials.from_service_account_file('./divine-fuze-387415-41eaafa270ca.json')

    # Instantiates a client
    client = vision.ImageAnnotatorClient(credentials=credentials)

    # The URI of the image file to annotate
    file_uri = "gs://cloud-samples-data/vision/label/wakeupcat.jpg"

    image = vision.Image()
    image.source.image_uri = file_uri

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print("Labels:")
    for label in labels:
        print(label.description)

    return labels

run_quickstart()