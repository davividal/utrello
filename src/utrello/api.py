import requests


implemented_services = ['boards', 'cards']


class TrelloApi(object):
    base_url = 'https://api.trello.com/1'
    service_endpoint = None
    url = None
    params = {}

    def __init__(self, api_key, api_token):
        self.params['key'] = api_key
        self.params['token'] = api_token
        self.url = "{}{}".format(self.base_url, self.service_endpoint)


class Boards(TrelloApi):
    base_url = 'https://api.trello.com/1/members/me'
    service_endpoint = '/boards'

    def list(self):
        params = self.params.copy()
        params['fields'] = 'name'
        req = requests.get(self.url, params=params)
        return req.json()

class Lists(TrelloApi):
    service_endpoint = '/boards/{board_id}/lists'
    board_id = None

    def list(self):
        req = requests.get(self.url.format(board_id=self.board_id), params=self.params)
        return req.json()


class Cards(TrelloApi):
    service_endpoint = '/cards'

    def create(self, card):
        headers = { "Accept": "application/json" }
        print(self.url)

        query = self.params.copy()
        query.update(card.__dict__)
        print(query)

        response = requests.post(self.url, headers=headers, params=query)
        print(response)
        return response.json()
