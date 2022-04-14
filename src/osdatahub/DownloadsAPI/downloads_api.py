from typing import Union
import requests
from typeguard import check_argument_types


class OpenDataDownload:

    __ENDPOINT = r"https://api.os.uk/downloads/v1/products/"
    HEADERS = {"method": "GET",
               "headers": "{'Content-Type': 'application/json'}"}

    def __get_endpoint(self):
        pass

    def query(self, product_id: str, file_name: str = None,
              format: str = None, subformat: str = None,
              area: str = None, redirect: bool = False
              ) -> Union[dict, list]:
        pass


class DataPackagesDownload:
    """NOTE: this only allows authentication by API key.
    Docs describe OAuth as an option but that's not implemented
    here yet.
    """

    __ENDPOINT = r"https://api.os.uk/downloads/v1/dataPackages"
    __HEADERS = {"method": "GET",
                 "headers": "{'Content-Type': 'application/json'}"}

    def __init__(self, key):
        self.key = key

    @property
    def headers(self):
        return {**self.__HEADERS, 'key': self.key}

    def __get_endpoint(self, data_package_id: Union[str, int] = None,
                       get_versions: bool = False,
                       version_id: Union[str, int] = None,
                       file_name: str = None) -> str:
        if data_package_id is None:
            return self.__ENDPOINT
        endpoint = f"{self.__ENDPOINT}/{data_package_id}"
        if version_id is not None:
            endpoint = f"{endpoint}/versions/{version_id}"
            if file_name is None:
                return endpoint
            return f"{endpoint}/downloads?fileName={file_name}"
        if get_versions:
            return f"{endpoint}/versions"
        return endpoint

    def query(self, data_package_id: Union[str, int] = None,
              get_versions: bool = False,
              version_id: Union[str, int] = None,
              file_name: str = None) -> Union[dict, list, str]:
        assert check_argument_types()
        endpoint = self.__get_endpoint(data_package_id, get_versions,
                                       version_id, file_name)
        response = requests.get(url=endpoint, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        # NOTE: I haven't been able to test this bit as our keys
        # don't seem to have any file associated with them!
        # Should only get this response when a filename is specified
        if response.status_code == 307:
            return response.headers['Location']
        raise requests.HTTPError(self._get_error_text(response))

    def _get_error_text(self, response):
        if 'message' in response.json():
            return (f"{response.status_code}: {response.json()['message']}. "
                    f"{response.reason} for url: {response.url}")
        return (f"{response.status_code}: {response.reason} "
                f"for url: {response.url}")
