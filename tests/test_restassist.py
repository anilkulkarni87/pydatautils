"""This is a test Module."""
import json

from pydataassist import restassist
from pydataassist import sparkassist


def test_api_to_df() -> None:
    """This is a test function."""
    df = restassist.api_to_df("https://www.boredapi.com/api/activity")
    column_list = [
        "activity",
        "type",
        "participants",
        "price",
        "link",
        "key",
        "accessibility",
    ]
    assert column_list.sort() == df.columns.sort()


def test_get_spark_schema_from_json_response() -> None:
    """This is a test function."""
    schema = sparkassist.get_spark_schema_from_json_response(
        json.dumps(restassist.call_api("https://jsonplaceholder.typicode.com/users/1"))
    )
    field_list = [
        "id",
        "name",
        "username",
        "email",
        "address",
        "phone",
        "website",
        "company",
    ]
    assert field_list.sort() == schema.fieldNames().sort()
