from src.backend_steps import user_steps
from src.base_classes.response import Response


def test_create_user(get_user_generator):
    Response(user_steps.create_user(get_user_generator.build())) \
        .assert_status_code(200) \
        .check_json_is_not_empty()

