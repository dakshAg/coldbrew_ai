from google.cloud import vision
import io
import os 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'COLDBREW_AI/detection/data/visionAPI.json'

def detect_labels(path):
    """Detects labels in the file."""

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
def main():
    file_path = 'coldbrew_ai/detection/data/test_img_coke.png'
    detect_labels(file_path)

if __name__ == '__main__':
    main()