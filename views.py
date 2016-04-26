from flask import render_template
from flask_nav import Nav
from flask_nav.elements import *
from app import app
from collections import Counter


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Future Employers!'}  
    with open('app/static/txt/resume.txt','rU') as new_file:
		count=Counter(''.join(e for e in new_file.read().lower() if e.isalpha()))
		count_list=list(count.items())
		final_list=[]
		for tup in count_list:
			d={}
			d["letter"]=tup[0]
			d["value"]=str(tup[1])
			#d[tup[0]]=str(tup[1])
			final_list.append(d)
		return render_template('index.html',
                           title='Home',
                           data=final_list,
                           user=user)

@app.route('/example2')
def example2():
	title="Here's the second example"
	pageType='about'

	return render_template("example2.html",title=title, pageType=pageType)
#nav.init_app(app)
    # {"letter":"a", "value":20},
	 		# 		{"letter":"b", "value":40}, 
	 		# 		{"letter":"c", "value":50},
	 		# 		{"letter":"m", "value":60}