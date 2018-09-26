import requests
import xml.etree.ElementTree as ET
import re


class TechCounter:
	def __init__(self, name, regex, category, count=0):
		self.name = name
		self.regex = re.compile(regex, re.IGNORECASE)
		self.category = category
		self.count = count

	def match(self, string):
		if self.regex.search(string):
			return True


def search_all_sites(request):
	return aggregate_results([
		search_stackoverflow(request),
	])

def aggregate_results(search_results):
	techs = [
		TechCounter('Assembly', r'^assembly', 'languages'),
		TechCounter('Bash', r'^bash', 'languages'),
		TechCounter('C', r'^c$', 'languages'),
		TechCounter('C++', r'^c\+\+', 'languages'),
		TechCounter('C#', r'^c#', 'languages'),
		TechCounter('Clojure', r'^clojure', 'languages'),
		TechCounter('Java', r'^java([- ]?(\w+|\d))?$', 'languages'),
		TechCounter('Python', r'^python', 'languages'),
		TechCounter(
			'JavaScript',
			r'^javascript|^es([- ]?\d)?|^ecmascript([- ]?\d)?|^js$',
			'languages'
		),
		TechCounter('SQL', r'^sql$', 'languages'),
		TechCounter('HTML', r'^html(\d)?', 'languages'),
		TechCounter('CSS', r'^css(\d)?', 'languages'),
		TechCounter('PHP', r'^php', 'languages'),
		TechCounter('Go', r'^go$|^golang', 'languages'),
		TechCounter('Ruby', r'^ruby', 'languages'),
		TechCounter('Objective-C', r'^objective[- ]?c', 'languages'),
		TechCounter('Scala', r'^scala$', 'languages'),
		TechCounter('Swift', r'^swift([- ]?\d)?$', 'languages'),
		TechCounter('R', r'^r$', 'languages'),
		TechCounter('COBOL', r'^cobol', 'languages'),
		TechCounter('Fortran', r'^fortran', 'languages'),
		TechCounter('Kotlin', r'^kotlin', 'languages'),
		TechCounter('XML', r'^xml', 'languages'),
		TechCounter('TypeScript', r'^typescript', 'languages'),
		TechCounter('JSON', r'^json', 'languages'),
		TechCounter('Perl', r'^perl([- ]?[56])?$', 'languages'),
		TechCounter('Less', r'^less$', 'languages'),
		TechCounter('Sass', r'^sass$', 'languages'),
		TechCounter('CoffeeScript', r'^coffeescript', 'languages'),
		TechCounter('Lisp', r'^lisp$', 'languages'),
		TechCounter('Pascal', r'^pascal', 'languages'),
		TechCounter('Dart', r'^dart', 'languages'),
		TechCounter('F', r'^f$', 'languages'),
		TechCounter('F#', r'^f#', 'languages'),
		TechCounter('Haskell', r'^haskell', 'languages'),
		TechCounter('Lua', r'^lua$', 'languages'),
		TechCounter('MATLAB', r'^matlab', 'languages'),
		TechCounter('PowerShell', r'^powershell', 'languages'),
		TechCounter('Elixir', r'^elixir', 'languages'),
		TechCounter('GraphQL', r'^graphql', 'languages'),
		TechCounter('D', r'^d$', 'languages'),

		TechCounter('React', r'^react(.?js)?([- ]?(?!native)\w+)?$', 'frameworks'),
		TechCounter('Node', r'^node(.?js)?$', 'frameworks'),
		TechCounter('Spring', r'^spring([- ]?mvc)?([- ]?framework)?$', 'frameworks'),
		TechCounter('Angular', r'^angular(.?js)?([- ]?framework)?$', 'frameworks'),
		TechCounter('Rails', r'^(ruby[- ]?on[- ]?)?rails([- ]?framework)?', 'frameworks'),
		TechCounter('Django', r'^django([- ]?(?!rest)\w+)?([- ]?framework)?$', 'frameworks'),
		TechCounter('ASP.NET', r'^asp.net([- ]?mvc)?([- ]?framework)?', 'frameworks'),
		TechCounter('React Native', r'^react[- ]?native([- ]?framework)?$', 'frameworks'),
		TechCounter('Ember', r'^ember', 'frameworks'),
		TechCounter('Vue', r'^vue(.?js)?([- ]?framework)?$', 'frameworks'),
		TechCounter('Flask', r'^flask([- ]?framework)?$', 'frameworks'),
		TechCounter('DRF', r'^drf|^django[- ]?rest[- ]?framework', 'frameworks'),
		TechCounter('CakePHP', r'^cake(php)?([- ]?framework)?', 'frameworks'),
		TechCounter('Phoenix', r'^phoenix([- ]?framework)?$', 'frameworks'),
		TechCounter('Express', r'^express(.?js)?([- ]?framework)?$', 'frameworks'),
		TechCounter('Backbone', r'^backbone(.?js)?([- ]?framework)?$', 'frameworks'),
		TechCounter('Drupal', r'^drupal([- ]?framework)?$', 'frameworks'),
		TechCounter('Laravel', r'^laravel([- ]?framework)?$', 'frameworks'),
		TechCounter('Symfony', r'^symfony([- ]?framework)?', 'frameworks'),
		TechCounter('Pyramid', r'^pyramid([- ]?framework)?$', 'frameworks'),
		TechCounter('Sinatra', r'^sinatra([- ]?framework)?$', 'frameworks'),
		TechCounter('WordPress', r'^wordpress([- ]?framework)?', 'frameworks'),
		TechCounter('Magento', r'^magento([- ]?framework)?', 'frameworks'),

		TechCounter('.NET', r'^.net', 'platforms'),
		TechCounter('Docker', r'^docker$', 'platforms'),
		TechCounter('AWS', r'^amazon([- ]?web[- ]?service(s)?)?$|^aws$', 'platforms'),
		TechCounter('Azure', r'^azure$', 'platforms'),
		TechCounter('Java EE', r'^java[- ]?ee$', 'platforms'),
		TechCounter('Kubernetes', r'^kubernetes|^k8s$', 'platforms'),
		TechCounter('Apache', r'^apache$', 'platforms'),
		TechCounter('Google Cloud', r'^google[- ]?cloud', 'plcreate_regex(key)atforms'),
		TechCounter('Salesforce', r'^salesforce$', 'platforms'),
		TechCounter('Oracle', r'^oracle$', 'platforms'),
		TechCounter('ROS', r'^ros$|^robot[- ]?operating[- ]?system$', 'platforms'),

		TechCounter('Git', r'^git', 'tools'),
		TechCounter('Hadoop', r'^(apache[- ])?hadoop$', 'tools'),
		TechCounter('Apache Spark', r'^(apache[- ])?spark$', 'tools'),
		TechCounter('Jenkins', r'^jenkins$', 'tools'),
		TechCounter('Chef', r'^chef$', 'tools'),
		TechCounter('Redux', r'^(\w+[- ]?)?redux$', 'tools'),
		TechCounter('Selenium', r'^selenium', 'tools'),
		TechCounter('Jquery', r'^jquery', 'tools'),
		TechCounter('Elasticsearch', r'^elasticsearch$', 'tools'),
		TechCounter('Puppet', r'^puppet$', 'tools'),
		TechCounter('Kafka', r'^(apache[- ])?kafka$', 'tools'),
		TechCounter('Spring Boot', r'^spring[- ]?boot$', 'tools'),
		TechCounter('Ansible', r'^ansible$', 'tools'),
		TechCounter('Jira', r'^(atlassian[- ]?)?jira$', 'tools'),
		TechCounter('QT', r'^(\w[- ]?)?qt([- ]?\d)?$', 'tools'),
		TechCounter('TensorFlow', r'^tensorflow$', 'tools'),
		TechCounter('Ajax', r'^ajax', 'tools'),
		TechCounter('Twitter Bootstrap', r'^(twitter[- ]?)?bootstrap', 'tools'),
		TechCounter('Bulma', r'^bulma', 'tools'),

		TechCounter('Unity3D', r'^unity(3d)?$', 'engines'),
		TechCounter('Unreal Engine', r'^unreal([- ]?engine)?', 'engines'),
		TechCounter('Cry Engine', r'^cry([- ]?engine)?$', 'engines'),

		TechCounter('Web Services', r'^web[- ]?service(s)?$', 'concepts'),
		TechCounter('Agile', r'^agile', 'concepts'),
		TechCounter('Cloud', r'^cloud$', 'concepts'),
		TechCounter('REST', r'^rest(ful)?[- ]?(architecture)?$', 'concepts'),
		TechCounter('Machine Learning', r'^machine[- ]?learning$', 'concepts'),
		TechCounter('SysAdmin', r'^sysadmin$', 'concepts'),
		TechCounter('DevOps', r'^devops$', 'concepts'),
		TechCounter('Testing', r'^testing$', 'concepts'),
		TechCounter('Security', r'^(\w+)?[- ]?security$', 'concepts'),
		TechCounter('API', r'^api([- ]\w+)?$', 'concepts'),
		TechCounter('UI', r'^ui$|^user[- ]?interface$', 'concepts'),
		TechCounter('Project Management', r'^project[- ]?management$', 'concepts'),
		TechCounter('Microservices', r'^microservice', 'concepts'),
		TechCounter('SaaS', r'^saas$', 'concepts'),
		TechCounter('CI', r'^ci$|^continuous[- ]?integration$', 'concepts'),
		TechCounter('Automation', r'^automation$', 'concepts'),
		TechCounter('QA', r'^qa$|^quality[- ]?assurance$', 'concepts'),
		TechCounter('Test Automation', r'^test[- ]?automation$|^automated[- ]?test', 'concepts'),
		TechCounter('OOP', r'^oop$|^object[- ]?oriented[- ]?programming$', 'concepts'),
		TechCounter('Algorithms', r'^algorithm', 'concepts'),
		TechCounter('Scrum', r'^scrum', 'concepts'),
		TechCounter('ETL', r'^etl$|^extract[,\- ]?transform[,\- ]?load$', 'concepts'),
		TechCounter('Embedded', r'^embedded', 'concepts'),
		TechCounter('Big Data', r'^big[- ]?data$', 'concepts'),
		TechCounter('Computer Science', r'^cs$|^computer[- ]?science$', 'concepts'),
		TechCounter('UX', r'^ux$|^user[- ]?experience$', 'concepts'),
		TechCounter('Database', r'^database$', 'concepts'),
		TechCounter('TDD', r'^tdd$|^test[- ]?driven[- ]?develop(e)?ment$', 'concepts'),
		TechCounter('Scalability', r'^scalability$|^scalable$|^scaling$', 'concepts'),
		TechCounter('Backend', r'^back[- ]?end$', 'concepts'),
		TechCounter('Frontend', r'^front[- ]?end$', 'concepts'),
		TechCounter('Unit Testing', r'^unit[- ]?test(ing)?$', 'concepts'),
		TechCounter('MVC', r'^mvc$|^model[- ]?view[- ]?controller$', 'concepts'),
		TechCounter('Neural Networks', r'^neural[- ]?network', 'concepts'),
		TechCounter('Debugging', r'^debug(ging)?$', 'concepts'),
		TechCounter('Web Applications', r'^web[- ]?app(s)?(lication(s)?)?$', 'concepts'),
		TechCounter('Design', r'^design$', 'concepts'),
		TechCounter('Architecture', r'^architecture$', 'concepts'),
		TechCounter('Functional Programming', r'^fp$|^functional[- ]?programming$', 'concepts'),
		TechCounter('Virtual Reality', r'^vr$|^virtual[- ]?reality$', 'concepts'),

		TechCounter('Linux', r'^linux', 'os'),
		TechCounter('Android', r'^android$', 'os'),
		TechCounter('iOS', r'^([a-z]+[- ])?ios|^iphone$', 'os'),
		TechCounter('Mobile', r'^mobile$', 'os'),
		TechCounter('Unix', r'^unix$', 'os'),
		TechCounter('Windows', r'^windows$', 'os'),

		TechCounter('MySQL', r'^mysql$', 'databases'),
		TechCounter('PostgreSQL', r'^postgre(sql)?$', 'databases'),
		TechCounter('Mongodb', r'^mongo(db)?$', 'databases'),
		TechCounter('SQL Server', r'^(microsoft[- ]?)?sql[- ]?server$|^mssql$', 'databases'),
		TechCounter('NoSQL', r'^nosql$', 'databases'),
		TechCounter('Cassandra', r'^(apache[- ])?cassandra$', 'databases'),
		TechCounter('Redis', r'^redis$', 'databases'),
		TechCounter('SQLite', r'^sqlite', 'databases'),
	]

	categories = {
		'languages': [],
		'frameworks': [],
		'platforms': [],
		'tools': [],
		'engines': [],
		'concepts': [],
		'os': [],
		'databases': [],
		'other': [],
	}
	for results in search_results:
		for key in results:
			match = False
			for tech in techs:
				if tech.match(key):
					tech.count += results[key]
					match = True
					if tech not in categories[tech.category]:
						categories[tech.category].append(tech)
			if not match:
				new_tech = TechCounter(key, create_regex(key), 'other', count=results[key])
				categories['other'].append(new_tech)
				techs.append(new_tech)

	for c in categories:
		categories[c] = sorted(categories[c], key=lambda tech: -tech.count)

	return categories


def create_regex(string):
	tokens = '-.?+*,$'
	regex = r''
	for char in string:
		if char in tokens:
			regex += f'\{char}'
		else:
			regex += char
	return regex

def search_stackoverflow(request):
	location = request.GET['search']
	resp = requests.get('https://stackoverflow.com/jobs/feed', params={'location': location})
	root = ET.fromstring(resp.content)
	
	keywords = {}
	job_posts = [x for x in root[0] if x.tag == 'item']
	for post in job_posts:
		categories = [x for x in post if x.tag == 'category']
		for category in categories:
			try: 
				keywords[category.text] += 1
			except KeyError:
				keywords[category.text] = 1
	return keywords