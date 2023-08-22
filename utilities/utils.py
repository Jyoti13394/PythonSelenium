import inspect
import logging
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

    def custom_logger(loglevel=logging.DEBUG):
        # Create logger
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        # set level
        logger.setLevel(loglevel)
        # set format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # create console handler or file handler for log messages
        fh = logging.FileHandler("automation.log")
        # add format to logger
        fh.setFormatter(formatter)
        # add handler to logger
        logger.addHandler(fh)
        return logger

