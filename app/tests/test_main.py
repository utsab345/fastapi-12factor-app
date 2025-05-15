from fastapi.testclient import TestClient
from app.main import app


def test_main():
    client = TestClient(app)
    url = "https://reddit.com"

    res = client.post("/api/short", json={"url": url})
    assert res.status_code == 200
    short = res.json()["short_link"]
    assert len(short) == 7

    res = client.get(f"/{short}", follow_redirects=False)
    assert res.status_code == 307
    assert res.headers["location"] == url

    assert client.get("/badpath").status_code == 404
