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
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
from resource_management import *




def project_config():
  """
  Sets up the config files common to master, standby and segment nodes.
  """
  import params
  
  # File(params.catalind_path,content=StaticFile('catalina.sh'))
  # configFile("/opt/bdos/bdos-project/webapps/jupiter-project/WEB-INF/classes/bdos_environment.properties",template_name="bdos_environment.properties.j2")
  # File(format("/opt/tomcat/webapps/jupiter-project/WEB-INF/classes/bdos-config-common/bdos_common_config_customize_cn_product.properties"),
  #      content=Template("bdos_common_config_customize_cn_product.properties.j2")
  # )
  File(format("/opt/tomcat/conf/server.xml"),
       content=Template("server.xml.j2")
  )
  File(format("/etc/redis.conf"),
       content=Template("redis.conf.j2")
  )

  File(format("/opt/tomcat/webapps/bcmp-web/WEB-INF/classes/application-db.properties"),
       content=Template("application-db.properties.j2")
  )
  File(format("/opt/tomcat/webapps/bcmp-web/WEB-INF/classes/application.properties"),
       content=Template("application.properties.j2")
  )
  File(format("/opt/tomcat/webapps/bcmp-web/WEB-INF/classes/jobrunner-config.properties"),
       content=Template("jobrunner-config.properties.j2")
  )
# def configFile(name,template_name=None):
#     import params
#     File(name,
#         content=Template(template_name),
#         owner = params.project_user,
#         group = params.project_group
#         )
#
  
  
  
