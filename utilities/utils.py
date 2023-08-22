import softest


class Utils(softest.TestCase):

    def assrtListItemText(self, list_name, value):
        for stop in list_name:
            print("The text is :" + stop.text)
            self.soft_assert(self.assertEqual, stop.text, value)
            if stop.text == value:
                print("Test Passed")
            else:
                print("Test failed")
        self.assert_all()
