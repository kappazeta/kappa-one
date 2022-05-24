# Copyright 2022 KappaZeta Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from kappa_one.wms import K1_WMS
from kappa_one.wcs import K1_WCS
from kappa_one.timeseries import K1_TimeSeries


API_TOKEN = "ard_de_test"


def get_wms():
    aoi_bbox = (1363672.5100108385, 7171632.9206572, 1399769.896618513, 7190092.46298807)

    k1_wms = K1_WMS(API_TOKEN)

    img = k1_wms.get(
        layers=["ard_de_s0cohvv6"],
        srs="EPSG:3857",
        bbox=aoi_bbox,
        time="2021-12-25",
        size=(1889, 966),
        format="image/png",
        transparent=True
    )

    with open('wms_test.png', 'wb') as out:
        out.write(img.read())


def get_wcs():
    aoi_bbox = (1318793.017583814, 7172251.198574754, 1411050.147119888, 7217274.59981189)

    k1_wcs = K1_WCS(API_TOKEN)

    img = k1_wcs.get(
        identifier="ard_de_cohvv6",
        time="2021-11-13",
        bbox=aoi_bbox,
        width=1920,
        height=937,
        crs="EPSG:3857",
        format="image/png",
        timeout=180
    )

    with open('wcs_test.png', 'wb') as out:
        out.write(img.read())


def get_ts():
    k1_ts = K1_TimeSeries(API_TOKEN)

    parcel1 = k1_ts.get_parcels()[0]
    print(parcel1)
    print(k1_ts.get_s1_time_series(parcel_id=parcel1.parcel_id))


def main():
    get_ts()


if __name__ == "__main__":
    main()
