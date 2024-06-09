from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

test_bikin = ['Secret Share', 'QR Code']

for test_bikin in test_bikin:
    file_metadata = {
        'name': test_bikin,
        'mimeType': 'application/vnd.google-apps.folder'
        # 'parents': []
    }

    service.files().create(body=file_metadata).execute()