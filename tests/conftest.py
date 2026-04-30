import copy
import pytest

from src.app import app, activities

INITIAL_ACTIVITIES = {
    "Basketball Team": {
        "description": "Play basketball and learn team strategies",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Soccer Club": {
        "description": "Practice soccer skills and compete in matches",
        "schedule": "Mondays and Wednesdays, 3:00 PM - 4:30 PM",
        "max_participants": 22,
        "participants": []
    },
    "Art Club": {
        "description": "Explore various art forms and create masterpieces",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": []
    },
    "Drama Club": {
        "description": "Act in plays and improve public speaking",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Debate Club": {
        "description": "Learn argumentation and debate topics",
        "schedule": "Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 12,
        "participants": []
    },
    "Science Club": {
        "description": "Conduct experiments and learn about science",
        "schedule": "Tuesdays, 3:00 PM - 4:00 PM",
        "max_participants": 18,
        "participants": []
    },
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset app.activities state before each test."""
    activities.clear()
    activities.update(copy.deepcopy(INITIAL_ACTIVITIES))
    yield
    activities.clear()
    activities.update(copy.deepcopy(INITIAL_ACTIVITIES))


@pytest.fixture
def client():
    from fastapi.testclient import TestClient

    return TestClient(app)
