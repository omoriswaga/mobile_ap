import os

"""Script used to define constants used across codebase."""

SECRET_KEY = os.getenv(
    'PAYSTACK_SECRET_KEY',
    'sk_test_c283fd1e67a0c8ae7ef617e67bedd7f31c52d66e')
HEADERS = {'Authorization': 'Bearer {}'}
API_URL = 'https://api.paystack.co/'
