#   Copyright 2021 Google LLC
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import abc
from helpers.base import BaseHelper, Context
import copy


class NotConfiguredException(Exception):
    pass


class Output(BaseHelper):

    def __init__(self, config, output_config, jinja_environment, data, event,
                 context: Context):
        self.config = copy.deepcopy(config)
        self.output_config = copy.deepcopy(output_config)
        self.data = data
        self.event = event
        self.context = context

        super().__init__(jinja_environment)

    @abc.abstractmethod
    def output(self):
        pass