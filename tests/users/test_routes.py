
def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200

    data = response.get_json()
    assert "users" in data
    assert len(data["users"]) == 2

    emails = [user["email"] for user in data["users"]]
    assert "user1@email.com" in emails
    assert "user2@email.com" in emails