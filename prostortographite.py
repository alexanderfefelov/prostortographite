#!/usr/bin/env python

import graphitesend
import os
import urllib2
import yaml

with open(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'prostortographite.yml', 'r') as yml_file:
    config = yaml.load(yml_file)

prostor_config = config['prostor']
request = 'http://api.prostor-sms.ru/messages/v2/balance/?login=%s&password=%s' \
          % (prostor_config['login'], prostor_config['password'])
result = urllib2.urlopen(request).read()
value = result.split(';')[1]

graphite_config = config['graphite']
graphite_engine = graphitesend.init(graphite_server=graphite_config['host'], graphite_port=graphite_config['port'],
                                    prefix='', system_name='')
metric = prostor_config['metric']
graphite_engine.send(metric, value)
