def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 9
    assert "Basketball Team" in data
    assert "Chess Club" in data


def test_get_activities_has_required_fields(client):
    response = client.get("/activities")

    assert response.status_code == 200
    activity = response.json()["Basketball Team"]
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity
    assert isinstance(activity["participants"], list)


def test_successful_signup_adds_participant(client):
    response = client.post("/activities/Basketball Team/signup?email=student@test.com")

    assert response.status_code == 200
    assert response.json()["message"] == "Signed up student@test.com for Basketball Team"

    activities_response = client.get("/activities")
    activities_data = activities_response.json()
    assert "student@test.com" in activities_data["Basketball Team"]["participants"]


def test_duplicate_signup_returns_400(client):
    email = "duplicate@mergington.edu"

    first_response = client.post(f"/activities/Basketball Team/signup?email={email}")
    assert first_response.status_code == 200

    second_response = client.post(f"/activities/Basketball Team/signup?email={email}")
    assert second_response.status_code == 400
    assert "already signed up" in second_response.json()["detail"]


def test_delete_participant(client):
    email = "delete_me@mergington.edu"

    signup_response = client.post(f"/activities/Soccer Club/signup?email={email}")
    assert signup_response.status_code == 200

    delete_response = client.delete(f"/activities/Soccer Club/participant?email={email}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == f"Unregistered {email} from Soccer Club"

    activities_data = client.get("/activities").json()
    assert email not in activities_data["Soccer Club"]["participants"]


def test_delete_missing_participant_returns_404(client):
    response = client.delete("/activities/Art Club/participant?email=nonexistent@mergington.edu")

    assert response.status_code == 404
    assert "Participant not found" in response.json()["detail"]


def test_delete_from_nonexistent_activity_returns_404(client):
    response = client.delete("/activities/Nonexistent Club/participant?email=student@mergington.edu")

    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_signup_to_nonexistent_activity_returns_404(client):
    response = client.post("/activities/Nonexistent Club/signup?email=student@mergington.edu")

    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]
