import json

from funkload.utils import Data


class JSONData(Data):
    """Support JSON
    """
    def __init__(self, data, content_type='application/json'):
        Data.__init__(
            self,
            content_type,
            json.dumps(data))
