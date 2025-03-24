# Timezone settings
TIME_ZONE = 'Europe/Riga'
USE_TZ = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} 

STATUS_UPDATE_ENDPOINT = 'https://httpbin.org/post'  # Replace with your webhook.site URL

# Warehousepassword
WAREHOUSE_PASSWORD = 'drosa-api-sazina'  # Replace with actual secure password
