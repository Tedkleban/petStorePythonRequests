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

    def validate_json_scheme(self, scheme: tuple):
        for each in scheme:
            assert each in self.response_json

    def get_parsed_object(self):
        return self.parsed_object

    def __str__(self):

        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json}"
