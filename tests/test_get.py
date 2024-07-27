import requests

test_param = {"bear_type": "POLAR", "bear_name": "MISHA", "bear_age": 13}
test_answ = {"bear_id": 1, "bear_type": "POLAR", "bear_name": "MISHA", "bear_age": 13}


class TestGetBear(object):

    def test_get_brown(self, bear):
        response = requests.get(url=bear)
        assert response.json() == [test_answ]
