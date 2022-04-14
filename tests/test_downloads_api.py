import pytest

from osdatahub.DownloadsAPI.downloads_api import OpenDataDownload, DataPackagesDownload
from tests.data import downloads_api_data as data


class TestDataPackagesDownload:
    @pytest.mark.parametrize(*data.test__get_endpoint())
    def test__params(self, data_package_id, get_versions,
                     version_id, file_name, expected_result):
        # Arrange
        downloader = DataPackagesDownload('key')

        # Act
        endpoint = downloader._DataPackagesDownload__get_endpoint(
            data_package_id, get_versions, version_id, file_name
            )

        # Assert
        assert endpoint == expected_result
