import pytest
from poorlib.crypto.aes_chiper import AESCipher  # Assuming your class is saved in aes_cipher.py


@pytest.fixture
def password():
    return "mysecretpassword"


@pytest.fixture
def cipher(password):
    return AESCipher(password)


def test_encrypt_decrypt(cipher):
    plaintext = "Hello, World!"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)

    assert decrypted == plaintext, "Decrypted text should match the original plaintext"


def test_encrypt_decrypt_empty_string(cipher):
    plaintext = ""
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)

    assert decrypted == plaintext, "Decrypted empty string should return an empty string"


def test_encryption_is_different_for_different_passwords():
    password1 = "password1"
    password2 = "password2"

    cipher1 = AESCipher(password1)
    cipher2 = AESCipher(password2)

    plaintext = "Sensitive Data"

    encrypted1 = cipher1.encrypt(plaintext)
    encrypted2 = cipher2.encrypt(plaintext)

    assert encrypted1 != encrypted2, "Encrypted data should be different for different passwords"


def test_encryption_produces_different_output_for_same_input(cipher):
    plaintext = "Hello, World!"

    encrypted1 = cipher.encrypt(plaintext)
    encrypted2 = cipher.encrypt(plaintext)

    assert encrypted1 != encrypted2, "Encryption should produce different ciphertext for the same plaintext due to random IV"


def test_decryption_with_wrong_password():
    correct_password = "correct_password"
    wrong_password = "wrong_password"

    correct_cipher = AESCipher(correct_password)
    wrong_cipher = AESCipher(wrong_password)

    plaintext = "Secret Message"
    encrypted = correct_cipher.encrypt(plaintext)

    with pytest.raises(Exception):  # Expect decryption with wrong password to raise an error
        wrong_cipher.decrypt(encrypted)
