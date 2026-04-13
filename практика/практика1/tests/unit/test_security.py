from app.core.security import create_access_token, decode_token, hash_password, verify_password


def test_password_hash_roundtrip() -> None:
    password = "my-secret"
    hashed = hash_password(password)
    assert hashed != password
    assert verify_password(password, hashed)


def test_jwt_encode_decode() -> None:
    token = create_access_token("42")
    payload = decode_token(token)
    assert payload["sub"] == "42"
