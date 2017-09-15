"""
bcmp master file
"""

#from resource_management import *
from resource_management.libraries.script.script import Script
from resource_management.libraries.functions import get_unique_id_and_date
from resource_management.libraries.functions import conf_select
from resource_management.libraries.functions import stack_select
from resource_management.libraries.functions import StackFeature
from resource_management.libraries.functions.version import compare_versions, format_stack_version
from resource_management.libraries.functions.stack_features import check_stack_feature
from resource_management.libraries.functions.security_commons import build_expectations, \
  cached_kinit_executor, get_params_from_filesystem, validate_security_config_properties, \
  FILE_TYPE_JAAS_CONF
from resource_management.core import shell
from resource_management.core.logger import Logger
from resource_management.core.resources.system import Execute
from resource_management.libraries.functions.check_process_status import check_process_status
from resource_management.libraries.functions.format import format
from resource_management.libraries.functions.validate import call_and_match_output
import signal
import sys
import os
from os.path import isfile

from project_config import project_config

class Bcmp(Script):
    def install(self, env):
        import params
        env.set_params(params)
        print 'Install the Master'
        self.configure(env)
        self.install_packages(env)
    def configure(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        print 'Install plugins'
        project_config()
    def stop(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        stop_cmd = format("/opt/tomcat/bin/shutdown.sh")
        Execute(stop_cmd)
        stop_redis = format("/etc/init.d/redis stop")
        Execute(stop_redis)
        print 'Stop the Master'
    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        start_cmd = format("/opt/tomcat/bin/startup.sh")
        Execute(start_cmd)
        redis_cmd = format("/etc/init.d/redis start")
        Execute(redis_cmd)
        print 'Start the Master'
    def status(self, env):
        import params
        check_process_status(params.bcmp_project_pid)
        print('Status of the Master')
if __name__ == "__main__":
    Bcmp().execute()
