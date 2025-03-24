# Timezone settings
TIME_ZONE = 'Europe/Riga'
USE_TZ = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} 

STATUS_UPDATE_ENDPOINT = 'https://webhook.site/your-unique-url'  # Replace with your webhook.site URL

# Replace the API_KEY with WAREHOUSE_PASSWORD
WAREHOUSE_PASSWORD = 'drosa-api_sazina'  # Replace with actual secure password
