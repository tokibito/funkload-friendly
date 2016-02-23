import json

from funkload.utils import Data


class JSONData(Data):
    """Support JSON
    """
    def __init__(self, data, content_type='application/json'):
        super(JSONData, self).__init__(
            content_type,
            json.dumps(data))
