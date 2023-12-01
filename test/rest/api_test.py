import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        response_text = response.read().decode('utf-8')
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        
    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/7/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        
    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/7"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_add_with_letters_param1(self):
        try:
            url = f"{BASE_URL}/calc/add/abc/2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
            
    def test_api_add_with_letters_param2(self):
        try:
            url = f"{BASE_URL}/calc/add/2/abc"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_substract_with_letters_param1(self):
        try:
            url = f"{BASE_URL}/calc/substract/abc/2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_substract_with_letters_param2(self):
        try:
            url = f"{BASE_URL}/calc/substract/2/abc"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_multiply_with_letters_param1(self):
        try:
            url = f"{BASE_URL}/calc/multiply/abc/2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
            
    def test_api_multiply_with_letters_param2(self):
        try:
            url = f"{BASE_URL}/calc/multiply/2/abc"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_divide_with_letters_param1(self):
        try:
            url = f"{BASE_URL}/calc/divide/abc/2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
            
    def test_api_divide_with_letters_param2(self):
        try:
            url = f"{BASE_URL}/calc/divide/2/abc"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
        
    def test_api_divide_with_zero(self):
        try:
            url = f"{BASE_URL}/calc/divide/2/0"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_power_with_letters(self):
        try:
            url = f"{BASE_URL}/calc/power/abc/xyz"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_sqrt_with_letters(self):
        try:
            url = f"{BASE_URL}/calc/sqrt/abc"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_sqrt_with_negative(self):
        try:
            url = f"{BASE_URL}/calc/sqrt/-2"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_log10_with_letters(self):
        try:
            url = f"{BASE_URL}/calc/log10/abc"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
            
    def test_api_log10_with_negative(self):
        try:
            url = f"{BASE_URL}/calc/log10/-100"
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")