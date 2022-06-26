from io import StringIO
from textwrap import dedent
from utrello import model


class TestCardCreation:
    def test_card_from_args(self):
        card = model.Card(name="Test card", desc="Empty desc", idList="abc123")

        args = {"name": "Test card", "desc": "Empty desc", "idList": "abc123"}
        new_card = model.card_from_dict(args)

        assert card == new_card

    def test_only_name(self):
        card = model.Card(name="Test card")

        args = {"name": "Test card"}
        new_card = model.card_from_dict(args)

        assert card == new_card

    def test_only_desc(self):
        card = model.Card(desc="Empty desc")

        args = {"desc": "Empty desc"}
        new_card = model.card_from_dict(args)

        assert card == new_card

    def test_only_list(self):
        card = model.Card(idList="abc123")

        args = {"idList": "abc123"}
        new_card = model.card_from_dict(args)

        assert card == new_card


class TestCsvCardCreation:
    def make_pandas_csv(self, csv):
        return StringIO(dedent(csv).strip())

    def test_full_csv(self):
        card = model.Card(name="Test card", desc="Empty desc", idList="abc123")

        csv = """
        name,desc,idList
        Test card,Empty desc,abc123
        """

        new_card_list = model.cards_from_csv(self.make_pandas_csv(csv))

        assert [card] == new_card_list

    def test_order_not_important(self):
        card = model.Card(name="Test card", desc="Empty desc", idList="abc123")

        csv = """
        desc,idList,name
        Empty desc,abc123,Test card
        """

        new_card_list = model.cards_from_csv(self.make_pandas_csv(csv))

        assert [card] == new_card_list

    def test_multiple_cards(self):
        cards = [
            model.Card(name="Test card", desc="Empty desc", idList="abc123"),
            model.Card(name="Test card", desc="Empty desc", idList="abc456"),
            model.Card(name="Test card", desc="Empty desc", idList="abc123"),
            model.Card(name="Test card", desc="Empty desc", idList="abc456"),
            model.Card(name="Test card", desc="Empty desc", idList="abc123")
        ]

        csv = """
        name,desc,idList
        Test card,Empty desc,abc123
        Test card,Empty desc,abc456
        Test card,Empty desc,abc123
        Test card,Empty desc,abc456
        Test card,Empty desc,abc123
        """

        new_card_list = model.cards_from_csv(self.make_pandas_csv(csv))

        assert cards == new_card_list
