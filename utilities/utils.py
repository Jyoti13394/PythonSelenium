class Utils:

    def assrtListItemText(self, list_name, value):
        for stop in list_name:
            print("The text is :" + stop.text)
            assert stop.text == value
            print("assert pass")
