# KappaOne WCS services

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

from owslib.wcs import WebCoverageService


class K1_WCS(object):
    def __init__(self, token):
        self.wcs = WebCoverageService("https://api.kappa1.eu/user/" + token + "/wcs", version='1.0.0')

    def list_layers(self):
        return list(self.wcs.contents)

    def get(self, *args, **kwargs):
        return self.wcs.getCoverage(*args, **kwargs)

