from urllib.parse import quote_plus

import numpy as np
import requests
from django.conf import settings

SESSION = requests.Session()
URL = settings.VEC_API_URL


def get_word_vector(word):
    vector_response = SESSION.get('{}?word={}'.format(URL, quote_plus(word)))
    vector_response.raise_for_status()
    return np.array(vector_response.json())
