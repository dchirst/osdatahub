from typing import Union
import requests

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

    __ENDPOINT = r"https://api.os.uk/downloads/v1/dataPackages"
    __HEADERS = {"method": "GET",
               "headers": "{'Content-Type': 'application/json'}"}

    def __init__(self, key):
        self.key = key

    @property
    def headers(self):
        return {**self.__HEADERS, 'key': self.key}

    def __get_endpoint(self, data_package_id: str = None,
                       get_versions: bool = False,
                       version_id: str = None,
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

    def query(self, data_package_id: str = None, get_versions: bool = False,
              version_id: str = None,
              file_name: str = None) -> Union[dict, list]:
        endpoint = self.__get_endpoint(data_package_id, get_versions,
                                       version_id, file_name)
        response = requests.get(url=endpoint, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        response.raise_for_status()
