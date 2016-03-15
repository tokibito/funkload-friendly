import json

from funkload.utils import Data


class JSONData(Data):
    """Support JSON
    """
    def __init__(self, data, content_type='application/json'):
        """Constructor

        :param data: data will be encoding to JSON.
        :type data: dict
        :param content_type: Content type for data
        :type content_type: str
        """
        Data.__init__(
            self,
            content_type,
            json.dumps(data))
