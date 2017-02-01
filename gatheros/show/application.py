from flask import Flask, request, render_template, abort
import json
import os

base_dir = os.sep.join(__file__.split( os.sep )[:-1])

template_folder = base_dir + os.sep + "templates"
static_folder = base_dir + os.sep + "static"

# print template_folder, static_folder
# print __name__
flask_app_name = __name__.split('.')[0]
# flask_app_name = "gatheros." + __name__.split('.')[0]
# flask_app_name = "gatheros"
# flask_app_name = __name__
# print flask_app_name
flask_app = Flask( flask_app_name,\
					template_folder = template_folder,\
					static_folder = static_folder)

commStruct = {}


@flask_app.route('/')
def index_page() :
	groups = commStruct['CommandGroups']
	group_items = groups.items()
	ordered_groups = sorted(groups.items(), key = lambda i:i[1]['index'] )
	return render_template("index.html", commandGroups = ordered_groups)


@flask_app.route('/command/<name>')
def commandsPage( name ) :
	if name not in commStruct['CommandGroups'].keys() :
		return abort(404)

	group = commStruct['CommandGroups'][ name ]
	command_ids = set( group['Commands'] )
	print command_ids
	command_dict = [ (id_, comm) for id_, comm in commStruct['Commands'].iteritems() if id_ in command_ids]
	ordered_commands = sorted(command_dict, key = lambda i:i[1]['index'] )
	# print ordered_commands
	return render_template("commands.html", title = group['name'], commList = ordered_commands )


@flask_app.route('/search/', methods = ['POST'])
def searchPage() :
	if request.method != 'POST' :
		return index()
	data = request.form
	if 'keyword' not in data :
		return index()
	keyword = data['keyword']
	ret = {}
	ret['commands'] = []
	for command_list in command_dict['command_groups'].values() :
		for command in command_list['commands'] :
			if keyword in ' '.join( command.values() ) :
				ret['commands'].append( command )
	ret['name'] = 'Search for keyword "%s" - %d results' % (keyword, len( ret['commands'] ))
	return render_template("commands.html", comm_list = ret, meta = command_dict['meta'] )
