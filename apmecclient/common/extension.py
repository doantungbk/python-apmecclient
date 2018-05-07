# Copyright 2015 Rackspace Hosting Inc.
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
from stevedore import extension

from apmecclient.apmec import v1_0 as apmecV10


def _discover_via_entry_points():
    emgr = extension.ExtensionManager('apmecclient.extension',
                                      invoke_on_load=False)
    return ((ext.name, ext.plugin) for ext in emgr)


class ApmecClientExtension(apmecV10.ApmecCommand):
    pagination_support = False
    _formatters = {}
    sorting_support = False


class ClientExtensionShow(ApmecClientExtension, apmecV10.ShowCommand):
    def get_data(self, parsed_args):
        # NOTE(mdietz): Calls 'execute' to provide a consistent pattern
        #               for any implementers adding extensions with
        #               regard to any other extension verb.
        return self.execute(parsed_args)

    def execute(self, parsed_args):
        return super(ClientExtensionShow, self).get_data(parsed_args)


class ClientExtensionList(ApmecClientExtension, apmecV10.ListCommand):

    def get_data(self, parsed_args):
        # NOTE(mdietz): Calls 'execute' to provide a consistent pattern
        #               for any implementers adding extensions with
        #               regard to any other extension verb.
        return self.execute(parsed_args)

    def execute(self, parsed_args):
        return super(ClientExtensionList, self).get_data(parsed_args)


class ClientExtensionDelete(ApmecClientExtension, apmecV10.DeleteCommand):
    def run(self, parsed_args):
        # NOTE(mdietz): Calls 'execute' to provide a consistent pattern
        #               for any implementers adding extensions with
        #               regard to any other extension verb.
        return self.execute(parsed_args)

    def execute(self, parsed_args):
        return super(ClientExtensionDelete, self).run(parsed_args)


class ClientExtensionCreate(ApmecClientExtension, apmecV10.CreateCommand):
    def get_data(self, parsed_args):
        # NOTE(mdietz): Calls 'execute' to provide a consistent pattern
        #               for any implementers adding extensions with
        #               regard to any other extension verb.
        return self.execute(parsed_args)

    def execute(self, parsed_args):
        return super(ClientExtensionCreate, self).get_data(parsed_args)


class ClientExtensionUpdate(ApmecClientExtension, apmecV10.UpdateCommand):
    def run(self, parsed_args):
        # NOTE(mdietz): Calls 'execute' to provide a consistent pattern
        #               for any implementers adding extensions with
        #               regard to any other extension verb.
        return self.execute(parsed_args)

    def execute(self, parsed_args):
        return super(ClientExtensionUpdate, self).run(parsed_args)
