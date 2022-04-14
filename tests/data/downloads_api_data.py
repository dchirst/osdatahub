from pytest import param


def test__get_endpoint():
    test_variables = "data_package_id, get_versions, version_id, file_name, expected_result"
    test_data = [
        param(
            "1",
            True,
            "2",
            "bob",
            "https://api.os.uk/downloads/v1/dataPackages/1/versions/2/downloads?fileName=bob",
            id="All values supplied"
        ),
        param(
            None,
            True,
            "2",
            "bob",
            "https://api.os.uk/downloads/v1/dataPackages",
            id="No data_package_id"
        ),
        param(
            "1",
            True,
            None,
            "bob",
            "https://api.os.uk/downloads/v1/dataPackages/1/versions",
            id="Return data_package_id versions"
        ),
        param(
            "1",
            False,
            "2",
            None,
            "https://api.os.uk/downloads/v1/dataPackages/1/versions/2",
            id="Return specific version info"
        ),
        param(
            None,
            False,
            None,
            None,
            "https://api.os.uk/downloads/v1/dataPackages",
            id="All missing"
        ),
        param(
            "1",
            False,
            "2",
            "bob",
            "https://api.os.uk/downloads/v1/dataPackages/1/versions/2/downloads?fileName=bob",
            id="get_version = False, but filename"
        )
    ]
    return test_variables, test_data
