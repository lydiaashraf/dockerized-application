from fastapi.testclient import TestClient 
# Ben-import el client elly hayeb3at HTTP requests lel API fel tests
from app.main import app
# Ben-import el FastAPI application beta3etna
from unittest.mock import patch  
# Ben-import patch 3ashan nebdl Redis behavior fel tests temporarily

client = TestClient(app)  
# Benghz client nest5dmo fel tests men gheir ma nsh8l server monfsl


def test_home():
    response = client.get("/") 
    # Ben3ml GET request 3ala el root endpoint

    assert response.status_code == 200  
    # Benet2aked en el request nag7
    assert response.json() == {"message": "Hello from Docker Project"}  
    # Benet2aked en el response motabk ll motwak3

def test_cache():
    with patch("app.main.r") as mock_redis:  
    # Benbdl Redis client b mock temporarily
        mock_redis.get.return_value = "Hello from Redis"  
    # Ben7dd el value elly get() hayrg3ha

        response = client.get("/cache")  
    # Benb3t GET request lel cache endpoint

        assert response.status_code == 200 
    # Benet2aked en el request nag7
        assert response.json() == {"message": "Hello from Redis"}  
    # Benet2aked en el response sa7
        mock_redis.set.assert_called_once_with("message", "Hello from Redis") 
    # Benet2aked en set etndht b el kima el motwk3a

def test_create_user():
    user_data = {
        "name": "Lydia",
        "email": "lydia@example.com"
    }  
    # Benghz sample user data 3ashan neb3atha lel API

    with patch("app.main.r") as mock_redis:  
    # Benstbdl Redis client b mock temporarily
        response = client.post("/users", json=user_data)  
    # Benb3t POST request w el data fel JSON body

        assert response.status_code == 200  
    # Benet2aked en el request nag7
        assert response.json()["message"] == "User created successfully" 
    # Benet2aked en el message sa7
        assert response.json()["user"] == user_data  
    # Benet2aked en el API rag3 nfs bynat el most5dm

        mock_redis.set.assert_called_once_with(
            "user:lydia@example.com",
            '{"name":"Lydia","email":"lydia@example.com"}'
        )  
    # Benet2aked en el API 7awl y5zn bynat el most5dm fel Redis b el key w el JSON el motawaqqa3

def test_get_user():
    user_json = '{"name":"Lydia","email":"lydia@example.com"}'  
# Sample JSON data elly Redis hayrg3ha

    with patch("app.main.r") as mock_redis:  
# Benstbdl Redis client b mock
        mock_redis.get.return_value = user_json  
# Ben7dd el value elly Redis get() hayrg3ha

        response = client.get("/users/lydia@example.com") 
# Benb3t GET request 3ashan negib el user

        assert response.status_code == 200  
# Benet2aked en el request nag7
        assert response.json() == {
            "user": {
                "name": "Lydia",
                "email": "lydia@example.com"
            }
        }  
# Benet2aked en el API rg3 user data belshakl el motwak3

        mock_redis.get.assert_called_once_with("user:lydia@example.com")  
# Benet2aked en el API talab el user b el Redis key el sa7    

def test_get_user_not_found():
    with patch("app.main.r") as mock_redis:  
# Benstbdl Redis client b mock
        mock_redis.get.return_value = None  
# Ben7aky Redis ml2ash user bel email dh

        response = client.get("/users/missing@example.com")  
# Bentlob user mesh mawgood

        assert response.status_code == 200  
# Benet2aked en el API rg3 response tabi3y

        assert response.json() == {"message": "User not found"} 
 # Benet2aked en el message sa7
        mock_redis.get.assert_called_once_with("user:missing@example.com") 
 # Benet2aked en el Redis key sa7