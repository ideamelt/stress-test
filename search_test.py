from datetime import datetime, timedelta
import time
import random
import json
import grequests
import settings
import helpers
import urlparse
import math
import os


random_users_list = random.sample(settings.USER_LIST, settings.USERS_TO_TEST)

def write_log(message):
	if not os.path.exists('logs'):
		os.makedirs('logs')
	with open('logs/search_log.txt', 'ab') as f:
		m = '%s -> %s\n\n' % (datetime.utcnow(), message)
		f.write(m)
		print m

def search_test():
	# setup global variables
	timing_data = {}
	errors = {}
	started = {}
	# setup test stop condition
	total_loops = math.floor(settings.SEARCH_TOTAL_TIME / settings.SEARCH_INTERVAL_TIME)
	if total_loops < 1: total_loops = 1
	current_loop = 0
	# setup urls
	urls = [helpers.create_echo_url(settings.BASE_USER_URL + str(i)) for i in random_users_list]
	# setup global test time
	global_start = time.time()
	write_log('INFO - Starting test')
	write_log('INFO - Looping %s times for %s users' % (total_loops, settings.USERS_TO_TEST))
	# run test
	while current_loop < total_loops:
		write_log('INFO - Starting loop %s' % (current_loop))
		started[current_loop] = time.time()
		# setup variable
		loop_data = {}
		# sending requests for first batch
		reqs = (grequests.get(u) for u in urls)
		resp = grequests.map(reqs)
		# analyze response
		for r in resp:
			# nothing returned in response
			try:
				content = json.loads(r._content)
			except Exception, e:
				write_log('FATAL ERROR - No data returned. Quitting test')
				write.log('Exception: %s -- Status Code: %s -- URL: %s -- Content: %s' % (e, r.status_code, r.url, r._content))
				raise Exception
			# error checking
			if r.status_code != 200:
				write_log('ERROR - Request failed with %s error' % (content['errorCode']))
				if content['errorCode'] not in errors: errors[content['errorCode']] = 0
				errors[content['errorCode']] += 1
			# capture and store timeing
			request_time = (r.elapsed.seconds * 1000.0 + r.elapsed.microseconds / 1000.0)
			parsed = urlparse.urlparse(r.url)
			loop_data[urlparse.parse_qs(parsed.query)['q'][0]] = request_time
		# save data
		write_log('INFO - Loop finish %s' % (current_loop))
		timing_data[current_loop] = loop_data
		current_loop = current_loop + 1
		# figure out how long to sleep for
		elasped_time = time.time() - started[current_loop - 1]
		if(elasped_time < settings.SEARCH_INTERVAL_TIME):
			time.sleep(settings.SEARCH_INTERVAL_TIME - elasped_time)
	# aggregate stats and finish test
	global_data = {
		'total_time': time.time() - global_start,
		'raw': timing_data,
		'errors': errors,
		'start_times': started
	}
	write_log("ENDING TEST -- Total Run Time: %s " % (global_data['total_time']))
	helpers.export_data('search', helpers.aggregate_data(global_data))


# autorun when called from shell
search_test()