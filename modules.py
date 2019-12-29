
import datetime
import time
# if we just need date we can pull date from datetime
from datetime import date
from time import time
# we can install pip3 install and import them
import camelcase
# custom modules
import re

today = date.today()
timestamp = time()
camel = camelcase.CamelCase()
text = 'hello dear'
print(camel.hump(text))
print(timestamp)
print(today)