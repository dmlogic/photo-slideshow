import requests
import tempfile

class Lookup:

    database = None
    filepath = None

    def __init__(self, endpoint: str, width: int, height: int):
        self.endpoint = endpoint
        self.width = width
        self.height = height

    def call_api(self):
        api_response = requests.get(self.endpoint, params = {"w": self.width, "h": self.height}, timeout=10)
        api_response.raise_for_status()
        return api_response.json()

    def download_image(self, image_url):
        image_response = requests.get(image_url, stream=True, timeout=10)
        image_response.raise_for_status()

        with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.jpg') as temp_file:
            for chunk in image_response.iter_content(chunk_size=8192):
                temp_file.write(chunk)

            temp_file_path = temp_file.name
            return temp_file_path

    def random_image(self):
        try:
            data = self.call_api()

            tempfile = self.download_image(data.get('url'))

            return {
                # 'path': self.filepath+'bluebells.jpg',
                'path': tempfile,
                'title': data.get('title'),
                'date': data.get('date')
            }
        except requests.exceptions.RequestException as e:
            print(f"❌ An error occurred with the network request: {e}")
            return None
        except KeyError:
            print(f"❌ Error: The key was not found in the JSON response.")
            return None
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            return None

