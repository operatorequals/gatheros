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

command_dict = {}


@flask_app.route('/')
def index() :
    return render_template("index.html", command_filenames = sorted(command_dict['command_groups'].keys()))


@flask_app.route('/command/<name>')
def commandsPage( name ) :
	if name not in command_dict['command_groups'].keys() :
		return abort(404)
	return render_template("commands.html", title = name, comm_list = command_dict['command_groups'][name] )


@flask_app.route('/commands')
def commandListPage() :
    return render_template("command_list.html", command_array = command_dict['command_groups'])


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
