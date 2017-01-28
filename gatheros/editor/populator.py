

def populateDict( dict_, recursive = True ) :
	for key in dict_.keys() :
		print "===================="
		print "Editing [%s]:" % key

		if type( dict_[key] ) == dict and recursive:
			value = populateDict( dict_[key] )
		if type( dict_[key] ) == list and recursive:
			value = populateList( dict_[key] )

		else :
			cur_value = dict_[key]
			added_comment = ''
			if cur_value != None :
				added_comment = "[%s]" % cur_value
			value = raw_input( "* Type a value %s: " % ( added_comment ) ).strip()
			if not value :
				# print " - Space found. Continuing"
				# print 
				# print 
				continue

		dict_[key] = value

	return dict_


def populateList( list_ ) :
	eof = '-EOF-'
	print "Type Empty String to submit the list"
	value = raw_input("*	Append next element: ")
	while value != '' :
		list_.append( value )
		value = raw_input( "*	Append next element: ").strip()

	return list_
