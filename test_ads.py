import requests
import pytest

BASE_URL = "https://qa-internship.avito.com"


def test_create_ad():
    seller_id = 660974
    ad_data = {
        "sellerID": seller_id,
        "name": "Test item2",
        "price": 9000,
        "statistics": {
            "contacts": 9,
            "likes": 90,
            "viewCount": 900
        }
    }

    response = requests.post(f"{BASE_URL}/api/1/item", json=ad_data)
    assert response.status_code == 200
    assert "status" in response.json()


def test_get_ad_by_id():
    ad_id = "3301ca4d-7c21-41b1-aea2-40604ef246fc"
    seller_id = 660974
    response = requests.get(f"{BASE_URL}/api/1/item/{ad_id}")
    assert response.status_code == 200
    assert response.json()[0]["id"] == ad_id
    assert response.json()[0]["sellerId"] == seller_id


def test_get_ads_by_seller_id():
    seller_id = 660974
    response = requests.get(f"{BASE_URL}/api/1/{seller_id}/item")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_statistics_by_item_id():
    ad_id = "3301ca4d-7c21-41b1-aea2-40604ef246fc"
    response = requests.get(f"{BASE_URL}/api/1/statistic/{ad_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "contacts" in response.json()[0]
    assert "likes" in response.json()[0]
    assert "viewCount" in response.json()[0]


if __name__ == "__main__":
    pytest.main()
