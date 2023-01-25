class Response:

    def __init__(self, response):
        self.response = response
        self.response_json: dict = response.json()
        self.response_status = response.status_code
        self.parsed_object = None

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def check_json_is_not_empty(self):
        assert self.response_json != "{}", self
        return self

    def check_response_scheme(self, scheme: dict):
        assert sorted(self.response_json) == sorted(scheme), self

    def check_response_values(self, values: dict):
        sorted_json = sorted(self.response_json.items())
        sorted_values = sorted(values.items())
        assert sorted_json == sorted_values, self

    def check_value_in_json(self, key: str, value):
        assert self.response_json.get(key) == value, self

    def __str__(self):

        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json}"
