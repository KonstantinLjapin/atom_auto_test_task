import requests
from utils import get_available_bears_json, get_broken_bear_json
import random
import time

class TestPositive:

    def test_info(self, info):
        response = requests.get(info)
        assert response.status_code == 200

    def test_bears(self, bear):
        response = requests.get(bear)
        assert response.status_code == 200

    def test_post_bear(self, bear):
        response = requests.post(bear, data=get_available_bears_json())
        assert response.status_code == 200

    def test_put_bear(self, bear):
        new_bear = get_available_bears_json()
        response = requests.get(bear)
        id_bear = random.choice(response.json()).get("bear_id")
        #"http://0.0.0.0:8091/bear/1"
        bear = bear + "/" + str(id_bear)
        put_response = requests.put(bear, data=new_bear)
        assert response.status_code == 200
        assert put_response.status_code == 200

    def test_delete_bear(self, bear):
        response = requests.get(bear)
        id_bear = random.choice(response.json()).get("bear_id")
        #"http://0.0.0.0:8091/bear/1"
        bear = bear + "/" + str(id_bear)
        delete_response = requests.delete(bear)
        assert response.status_code == 200
        assert delete_response.status_code == 200

    def test_delete_all_bear(self, bear):
        response = requests.delete(bear)
        assert response.status_code == 200


class TestNegative:

    def test_info(self, info):
        info = info + "sdwffh"
        response = requests.get(info)
        assert response.status_code == 404

    def test_bears(self, bear):
        bear = bear + "/165745980796845098976545340-9876540-987654398765430-987654309876543"
        response = requests.get(bear)
        assert response.status_code == 404

    def test_post_bear(self, bear):
        response = requests.post(bear, data=get_broken_bear_json())
        assert response.status_code == 500

    def test_put_bear(self, bear):
        new_bear = get_available_bears_json()
        bear = bear + "/" + str(89765640987654765543765432876543876543287654)
        put_response = requests.put(bear, data=new_bear)
        assert put_response.status_code == 500

    def test_delete_bear(self, bear):
        bear = bear + "/" + str(8765643786564487865437654328765432)
        delete_response = requests.delete(bear)
        assert delete_response.status_code == 404

    def test_delete_all_bear(self, bear):
        bear = bear+"hjtytetrey"
        response = requests.delete(bear)
        assert response.status_code == 404


class TestBrake:

    def test_info(self, info):
        info = info

        for _ in range(1000):
            requests.get(info)
            time.sleep(0.1)
        response = requests.get(info)
        assert response.status_code == 200
