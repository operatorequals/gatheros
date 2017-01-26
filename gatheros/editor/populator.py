

def populateDict( dict_ ) :
	for key in dict_.keys() :

		# print "Going for '%s'" % key

		if type( dict_[key] ) not in ( dict, list, tuple )  :
			cur_value = dict_[key]
			added_comment = ''
			if cur_value != None :
				added_comment = "[%s]" % cur_value
			value = raw_input( "* Type a value for key '%s' %s: " % ( key, added_comment ) ).strip()[:-1]
			if not value :
				# print " - Space found. Continuing"
				# print 
				# print 
				continue

			dict_[key] = value

	return dict_


def populateList( list_ ) :
	eof = '-EOF-'
	print "type '%s' to submit the list" % eof
	value = input("Append next element: ")
	while value != eof :
		list_.append( value )
		value = input("Append next element: ")

	return _list
