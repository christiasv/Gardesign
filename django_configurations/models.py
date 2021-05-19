import base64

from cryptography.fernet import Fernet
from django.conf import settings
from django.db import models


class Configurations(models.Model):
    key = models.CharField(max_length=50, unique=True)
    value = models.CharField(max_length=1000, verbose_name='value')
    is_secret = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_secret:
            self.value = encrypt(self.value)

        super().save(force_insert, force_update, using, update_fields)

    @property
    def clean_value(self):
        return decrypt(self.value) if self.is_secret else self.value

    @clean_value.setter
    def clean_value(self, value):
        self.value = encrypt(value) if self.is_secret else value

    @property
    def obfuscated_value(self):
        return self.value[:20] + "..." if self.is_secret else self.value

    @obfuscated_value.setter
    def obfuscated_value(self, value):
        self.value = value


def encrypt(txt):
    try:
        # convert integer etc to string first
        txt = str(txt)
        # get the key from settings
        cipher_suite = Fernet(settings.FIELD_ENCRYPTION_KEY.encode('utf-8'))  # key should be byte
        # #input should be byte, so convert the text to byte
        encrypted_text = cipher_suite.encrypt(txt.encode('utf-8'))
        # encode to urlsafe base64 format
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode('utf-8')
        return encrypted_text
    except Exception as e:
        return None


def decrypt(txt: str):
    try:
        # base64 decode
        txt = base64.urlsafe_b64decode(txt)
        cipher_suite = Fernet(settings.FIELD_ENCRYPTION_KEY.encode('utf-8'))
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")
        return decoded_text
    except Exception as e:
        return None
