from datetime import datetime, timedelta
import urllib
import settings
import simplejson as json
import os

# common methods
def create_echo_url(user_url_s):
	return (settings.ECHO_API_URL + settings.ECHO_CLIENT_URL + settings.ECHO_DATATYPE_URL +
			urllib.quote_plus(user_url_s) + settings.ECHO_APP_KEY_QP)

def export_data(filename, data):
	if not os.path.exists('data'):
		os.makedirs('data')
	with open('data/%s-%s.json' % (filename, datetime.utcnow()), 'w') as outfile:
		json.dump(data, outfile, indent=4)

def aggregate_data(global_data):
	global_data['stats'] = {}
	# global stats
	total_requests = 0
	total_request_time = 0
	# iterate over each batch of tests
	for interval in global_data['raw']:
		data = global_data['raw'][interval]
		count = len(data)
		total = 0
		# aggregate time
		for user in data:
			total = total + data[user]
		# save data to global
		total_requests += count
		total_request_time += total
		# save data
		global_data['stats'][interval] = {
			'sent': count,
			'total': round(total / 1000, 6),
			'average': round((total / count) / 1000, 6),
		}
	# calculate global numbers
	global_data['total_requests'] = total_requests
	global_data['avg_request_time'] = round((total_request_time / total_requests) / 1000, 6)
	# return it all back!
	return global_data




