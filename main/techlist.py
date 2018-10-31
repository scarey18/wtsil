import re


class TechCounter:
	def __init__(self, name, regex, category, count=0):
		self.name = name
		self.regex = self.create_regex(regex)
		self.category = category
		self.count = count
		self.graph_percentage = None

	def __repr__(self):
		return self.name

	def match(self, string):
		if self.regex.search(string):
			return True

	def create_regex(self, regex):
		formatted_reg = []
		for section in regex.split('$|'):
			formatted_reg.append(r'^(.+?[ ,\/])?' + section + r'([ ,\/].+?)?$')
		return re.compile(('|').join(formatted_reg), re.IGNORECASE|re.MULTILINE)


def new_tech_list():
	return [
		TechCounter('Assembly', r'assembly', 'Languages'),
		TechCounter('Bash', r'bash', 'Languages'),
		TechCounter('C', r'c', 'Languages'),
		TechCounter('C++', r'c\+\+([- ]?\d+)?', 'Languages'),
		TechCounter('C#', r'c#', 'Languages'),
		TechCounter('Clojure', r'clojure', 'Languages'),
		TechCounter('Java', r'java([- ]([ <>\n,]+|\d))?', 'Languages'),
		TechCounter('Python', r'python', 'Languages'),
		TechCounter(
			'JavaScript',
			r'javascript$|es([- ]?\d)?$|ecmascript([- ]?\d)?$|js',
			'Languages'
		),
		TechCounter('SQL', r'sql', 'Languages'),
		TechCounter('HTML', r'html(\d)?', 'Languages'),
		TechCounter('CSS', r'css(\d)?', 'Languages'),
		TechCounter('PHP', r'php', 'Languages'),
		TechCounter('Go', r'go$|golang', 'Languages'),
		TechCounter('Ruby', r'ruby', 'Languages'),
		TechCounter('Objective-C', r'objective[- ]?c', 'Languages'),
		TechCounter('Scala', r'scala', 'Languages'),
		TechCounter('Swift', r'swift([- ]?\d)?', 'Languages'),
		TechCounter('R', r'r', 'Languages'),
		TechCounter('COBOL', r'cobol', 'Languages'),
		TechCounter('Fortran', r'fortran', 'Languages'),
		TechCounter('Kotlin', r'kotlin', 'Languages'),
		TechCounter('XML', r'xml', 'Languages'),
		TechCounter('TypeScript', r'typescript', 'Languages'),
		TechCounter('JSON', r'json', 'Languages'),
		TechCounter('Perl', r'perl([- ]?[56])?', 'Languages'),
		TechCounter('Less', r'less', 'Languages'),
		TechCounter('Sass', r'sass', 'Languages'),
		TechCounter('CoffeeScript', r'coffeescript', 'Languages'),
		TechCounter('Lisp', r'lisp', 'Languages'),
		TechCounter('Pascal', r'pascal', 'Languages'),
		TechCounter('Dart', r'dart', 'Languages'),
		TechCounter('F', r'f', 'Languages'),
		TechCounter('F#', r'f#', 'Languages'),
		TechCounter('Haskell', r'haskell', 'Languages'),
		TechCounter('Lua', r'lua', 'Languages'),
		TechCounter('MATLAB', r'matlab', 'Languages'),
		TechCounter('PowerShell', r'powershell', 'Languages'),
		TechCounter('Elixir', r'elixir', 'Languages'),
		TechCounter('GraphQL', r'graphql', 'Languages'),
		TechCounter('D', r'd', 'Languages'),


		TechCounter('React', r'react(\.?js)?([ <>\n,](?!native).+?)?$', 'Frameworks/CMS'),
		TechCounter('Node', r'node(\.?js)?', 'Frameworks/CMS'),
		TechCounter('Spring', r'spring([- ]?mvc)?([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Angular', r'angular(\.?js)?\d?([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Rails', r'(ruby[- ]?on[- ]?)?rails([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Django', r'django([- ]?(?!rest)[ <>\n,]+)?([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('ASP.NET', r'asp.net([- ]?mvc)?([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('React Native', r'react[- ]?native([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Ember', r'ember(\.?js)', 'Frameworks/CMS'),
		TechCounter('Vue', r'vue(\.?js)?([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Flask', r'flask([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Django Rest Framework', r'drf$|django[- ]?rest[- ]?framework', 'Frameworks/CMS'),
		TechCounter('CakePHP', r'cake(php)?([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Phoenix', r'phoenix([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Express', r'express(\.?js)?([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Backbone', r'backbone(\.?js)?([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Drupal', r'drupal([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Laravel', r'laravel([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Symfony', r'symfony\d+?([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Pyramid', r'pyramid([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Sinatra', r'sinatra([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('WordPress', r'wordpress([- ]?framework)?', 'Frameworks/CMS'),
		TechCounter('Magento', r'magento([- ]?framework)?', 'Frameworks/CMS'),


		TechCounter('.NET', r'.net', 'Platforms/Web Services'),
		TechCounter('Docker', r'docker', 'Platforms/Web Services'),
		TechCounter('AWS', r'amazon([- ]?web[- ]?service(s)?)?$|aws', 'Platforms/Web Services'),
		TechCounter('Azure', r'azure', 'Platforms/Web Services'),
		TechCounter('Java EE', r'java[- ]?ee', 'Platforms/Web Services'),
		TechCounter('Kubernetes', r'kubernetes$|k8s', 'Platforms/Web Services'),
		TechCounter('Apache', r'apache', 'Platforms/Web Services'),
		TechCounter('Google Cloud', r'google[- ]?cloud([- ]?platform)?', 'Platforms/Web Services'),
		TechCounter('Salesforce', r'salesforce', 'Platforms/Web Services'),
		TechCounter('Oracle', r'oracle', 'Platforms/Web Services'),
		TechCounter('ROS', r'ros$|robot[- ]?operating[- ]?system', 'Platforms/Web Services'),


		TechCounter('Git', r'git', 'Libraries/Tools'),
		TechCounter('Hadoop', r'(apache[- ])?hadoop', 'Libraries/Tools'),
		TechCounter('Apache Spark', r'(apache[- ])?spark', 'Libraries/Tools'),
		TechCounter('Jenkins', r'jenkins', 'Libraries/Tools'),
		TechCounter('Chef', r'chef', 'Libraries/Tools'),
		TechCounter('Redux', r'(.+[- ])?redux', 'Libraries/Tools'),
		TechCounter('Selenium', r'selenium', 'Libraries/Tools'),
		TechCounter('Jquery', r'jquery', 'Libraries/Tools'),
		TechCounter('Elasticsearch', r'elasticsearch', 'Libraries/Tools'),
		TechCounter('Puppet', r'puppet', 'Libraries/Tools'),
		TechCounter('Kafka', r'(apache[- ])?kafka', 'Libraries/Tools'),
		TechCounter('Spring Boot', r'spring[- ]?boot', 'Libraries/Tools'),
		TechCounter('Ansible', r'ansible', 'Libraries/Tools'),
		TechCounter('Jira', r'(atlassian[- ]?)?jira', 'Libraries/Tools'),
		TechCounter('QT', r'([ <>\n,][- ]?)?qt([- ]?\d)?', 'Libraries/Tools'),
		TechCounter('TensorFlow', r'tensorflow', 'Libraries/Tools'),
		TechCounter('Ajax', r'ajax', 'Libraries/Tools'),
		TechCounter('Twitter Bootstrap', r'(twitter[- ]?)?bootstrap', 'Libraries/Tools'),
		TechCounter('Bulma', r'bulma', 'Libraries/Tools'),
		TechCounter('Cucumber', r'cucumber', 'Libraries/Tools'),
		TechCounter('Terraform', r'terraform', 'Libraries/Tools'),
		TechCounter('SQLAlchemy', r'sqlalchemy', 'Libraries/Tools'),


		TechCounter('Unity3D', r'unity(3d)?\d?', 'Game Engines'),
		TechCounter('Unreal Engine', r'unreal([- ]?engine)?', 'Game Engines'),
		TechCounter('Cry Engine', r'cry([- ]?engine)?', 'Game Engines'),


		TechCounter('Web Services', r'web[- ]?service(s)?', 'Concepts/Skills'),
		TechCounter('Agile', r'agile', 'Concepts/Skills'),
		TechCounter('Cloud', r'cloud', 'Concepts/Skills'),
		TechCounter('REST', r'rest(ful)?[- ]?(architecture)?', 'Concepts/Skills'),
		TechCounter('Machine Learning', r'machine[- ]?learning', 'Concepts/Skills'),
		TechCounter('SysAdmin', r'sysadmin', 'Concepts/Skills'),
		TechCounter('DevOps', r'devops', 'Concepts/Skills'),
		TechCounter('Testing', r'testing', 'Concepts/Skills'),
		TechCounter('Security', r'([ <>\n,]+)?[- ]?security', 'Concepts/Skills'),
		TechCounter('API ', r'api([- ][ <>\n,]+)?', 'Concepts/Skills'),
		TechCounter('User Interface', r'ui$|user[- ]?interface', 'Concepts/Skills'),
		TechCounter('Project Management', r'project[- ]?management', 'Concepts/Skills'),
		TechCounter('Microservices', r'microservice', 'Concepts/Skills'),
		TechCounter('SaaS', r'saas', 'Concepts/Skills'),
		TechCounter('Continuous Integration', r'ci$|continuous[- ]?integration', 'Concepts/Skills'),
		TechCounter('Automation', r'automation', 'Concepts/Skills'),
		TechCounter('QA', r'qa$|quality[- ]?assurance', 'Concepts/Skills'),
		TechCounter('Test Automation', r'test[- ]?automation$|automated[- ]?tests?', 'Concepts/Skills'),
		TechCounter('Object Oriented Programming', r'oop$|object[- ]?oriented[- ]?programming', 'Concepts/Skills'),
		TechCounter('Algorithms', r'algorithm', 'Concepts/Skills'),
		TechCounter('Scrum', r'scrum', 'Concepts/Skills'),
		TechCounter('ETL', r'etl$|extract[,\- ]?transform[,\- ]?load', 'Concepts/Skills'),
		TechCounter('Embedded', r'embedded', 'Concepts/Skills'),
		TechCounter('Big Data', r'big[- ]?data', 'Concepts/Skills'),
		TechCounter('Computer Science', r'cs$|computer[- ]?science', 'Concepts/Skills'),
		TechCounter('UX', r'ux$|user[- ]?experience', 'Concepts/Skills'),
		TechCounter('Test Driven Development', r'tdd$|test[- ]?driven[- ]?develop(e)?ment', 'Concepts/Skills'),
		TechCounter('Scalability', r'scalability$|scalable$|scaling', 'Concepts/Skills'),
		TechCounter('Backend', r'back[- ]?end', 'Concepts/Skills'),
		TechCounter('Frontend', r'front[- ]?end', 'Concepts/Skills'),
		TechCounter('Unit Testing', r'unit[- ]?test(ing)?', 'Concepts/Skills'),
		TechCounter('MVC', r'mvc$|model[- ]?view[- ]?controller', 'Concepts/Skills'),
		TechCounter('Neural Networks', r'neural[- ]?network', 'Concepts/Skills'),
		TechCounter('Debugging', r'debug(ging)?', 'Concepts/Skills'),
		TechCounter('Web Applications', r'web[- ]?app(s)?(lication(s)?)?', 'Concepts/Skills'),
		TechCounter('Design', r'design', 'Concepts/Skills'),
		TechCounter('Architecture', r'^(.+?([ <>\n,]|(\\\/)))?architecture', 'Concepts/Skills'),
		TechCounter('Functional Programming', r'fp$|functional[- ]?programming', 'Concepts/Skills'),
		TechCounter('Virtual Reality', r'vr$|virtual[- ]?reality', 'Concepts/Skills'),
		TechCounter('Cryptography', r'crypto(graphy)?', 'Concepts/Skills'),
		TechCounter('Microservices', r'micro[- ]?services?', 'Concepts/Skills'),


		TechCounter('Linux', r'linux', 'Operating Systems'),
		TechCounter('Android', r'android', 'Operating Systems'),
		TechCounter('iOS', r'([a-z]+[- ])?ios|iphone', 'Operating Systems'),
		TechCounter('Mobile', r'mobile', 'Operating Systems'),
		TechCounter('Unix', r'unix', 'Operating Systems'),
		TechCounter('Windows', r'windows', 'Operating Systems'),


		TechCounter('MySQL', r'mysql', 'Databases'),
		TechCounter('PostgreSQL', r'postgre(sql)?s?', 'Databases'),
		TechCounter('Mongodb', r'mongo(db)?', 'Databases'),
		TechCounter('SQL Server', r'(microsoft[- ]?)?sql[- ]?server$|mssql', 'Databases'),
		TechCounter('NoSQL', r'nosql', 'Databases'),
		TechCounter('Cassandra', r'(apache[- ])?cassandra', 'Databases'),
		TechCounter('Redis', r'redis', 'Databases'),
		TechCounter('SQLite', r'sqlite', 'Databases'),
		TechCounter('MariaDB', r'maria([- ]?db)?', 'Databases'),
	]