import requests
from models.WorkshopFollower import WorkshopFollower


class WorkshopFollowerRepository(object):
    def __init__(self, base_url):
        self._base_url = base_url

    def find_workshop_follower(self, id):
        url = self._base_url + '/workshopfollower/' + str(id)
        response = requests.get(url)
        if response.status_code == 200:
            print(response.json())
            user = WorkshopFollower(**response.json())
            return user
        else:
            return response

    def save_workshop_follower(self, user):
        url = self._base_url + '/workshopfollower'
        response = requests.post(url, json=user.to_json())
        return response
