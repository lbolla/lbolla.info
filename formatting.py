import datetime
import time
 
def dt_from_tt(tt):
	"""Datetime from tt."""
	return tt and datetime.datetime.fromtimestamp(time.mktime(tt))

def fmt_date(dt):
	return dt and dt.strftime('%Y-%m-%d')

def fmt_datetime(dt):
	return dt and dt.strftime('%Y-%m-%d %H:%M')

def fmt_tt(tt):
	return tt and fmt_datetime(dt_from_tt(tt))
