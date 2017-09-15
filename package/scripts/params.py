#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""


import ambari_simplejson as json # simplejson is much faster comparing to Python 2.6 json module and has the same functions set.
import os

from urlparse import urlparse
from resource_management.libraries.resources.xml_config import XmlConfig
from ambari_commons.constants import AMBARI_SUDO_BINARY
from ambari_commons.os_check import OSCheck

from resource_management.libraries.functions.default import default
from resource_management.libraries.functions.format import format
from resource_management.libraries.functions.is_empty import is_empty
from resource_management.libraries.functions.copy_tarball import STACK_ROOT_PATTERN, STACK_NAME_PATTERN, STACK_VERSION_PATTERN
from resource_management.libraries.functions import get_kinit_path
from resource_management.libraries.functions.get_not_managed_resources import get_not_managed_resources
from resource_management.libraries.script.script import Script
from resource_management.libraries.functions import StackFeature
from resource_management.libraries.functions.stack_features import check_stack_feature
from resource_management.libraries.functions.stack_features import get_stack_feature_version
from resource_management.libraries.functions.get_port_from_url import get_port_from_url
from resource_management.libraries.functions.expect import expect
from resource_management.libraries import functions

# server configurations
config = Script.get_config()
tmp_dir = Script.get_tmp_dir()
#project_class="/opt/bdos/bdos-project/webapps/jupiter-project/WEB-INF/classes/com.zip"
###mysql###
mysql_host = config['clusterHostInfo']['mysql_master_hosts'][0]
mysql = config['configurations']['mysql-master']
mysql_port = mysql['mysql_master_port']
mysql_username = mysql['mysql_username']
mysql_passwd = mysql['mysql_password']


#bdos_project## 
server_http_port = config['configurations']['project-server']['project_http_port']
server_shutdown_port = config['configurations']['project-server']['project_shutdown_port']
server_ajp_port = config['configurations']['project-server']['project_ajp_port']
catalind_path='/opt/bdos/bdos-project/bin/catalina.sh'
project_install_dir='/opt/bdos/bdos-project'
bcmp_project_pid='/opt/tomcat/bcmp-project/bcmp_project.pid'

project_user=config['configurations']['project-env']['product_user']
project_group=config['configurations']['project-env']['product_group']
#redis config#
redis_host = config['configurations']['redis-server']['redis_host']
redis_port = config['configurations']['redis-server']['redis_port']
redis_timeout = config['configurations']['redis-server']['redis_timeout']
#hive config
hive_mysql_datasource = config['configurations']['bcmp-hive-site']['hive_mysql_datasource']
hive_mysql_port = config['configurations']['bcmp-hive-site']['hive_mysql_port']
hive_datasource_database = config['configurations']['bcmp-hive-site']['hive_datasource_database']
hive_mysql_username = config['configurations']['bcmp-hive-site']['hive_mysql_username']
hive_mysql_password = config['configurations']['bcmp-hive-site']['hive_mysql_password']
hive_server2_connect = config['configurations']['bcmp-hive-site']['hive_server2_connect']
hive_server2_user = config['configurations']['bcmp-hive-site']['hive_server2_user']
hive_server2_password = config['configurations']['bcmp-hive-site']['hive_server2_password']

#bcmp config
mysql_jdbc_connect = config['configurations']['bcmp-application']['mysql_jdbc_connect']
mysql_jdbc_port = config['configurations']['bcmp-application']['mysql_jdbc_port']
database = config['configurations']['bcmp-application']['database']
mysql_jdbc_username = config['configurations']['bcmp-application']['mysql_jdbc_username']
mysql_jdbc_password = config['configurations']['bcmp-application']['mysql_jdbc_password']
mysql_jdbc_driver = config['configurations']['bcmp-application']['mysql_jdbc_driver']
mysql_max_active = config['configurations']['bcmp-application']['mysql_max_active']
mysql_initial_size = config['configurations']['bcmp-application']['mysql_initial_size']
mysql_min_idle = config['configurations']['bcmp-application']['mysql_min_idle']
bcmp_zookeeper_host = config['configurations']['bcmp-application']['bcmp_zookeeper_host']

#java64_home = config['hostLevelParams']['java_home']
#rt_file = java64_home+"/jre/lib/rt.jar"
#io_util_file = java64_home+"/jre/lib/amd64/libjava_io_SecurityUtil.so"


