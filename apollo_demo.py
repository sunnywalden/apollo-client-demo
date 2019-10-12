#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyapollo import ApolloClient

client = ApolloClient(app_id="SampleApp", timeout=65)
client.start(use_eventlet=True)

timeout = client.get_value('timeout', namespace="demo")

print("Timeout value is:%s" % timeout)

# client.stop()
