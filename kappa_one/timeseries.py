# KappaOne time series

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

import requests
import json


class K1_Parcel(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)


class K1_S1TimeSeries(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)


class K1_TimeSeries(object):
    def __init__(self, token):
        self.base_url = "https://demodev2.kappazeta.ee/api-" + token + "/v1"

    def get_status(self):
        return requests.get(self.base_url + "/status").json()

    def get_parcels(self, **kwargs):
        parcels = requests.get(self.base_url + "/parcel", params=kwargs).json()["parcels"]
        return [K1_Parcel(p) for p in parcels]

    def get_s1_time_series(self, **kwargs):
        s1_ts = requests.get(self.base_url + "/time_series/s1", params=kwargs).json()["s1_time_series"]
        return [K1_S1TimeSeries(ts) for ts in s1_ts]

