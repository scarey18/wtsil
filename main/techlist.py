import re


class TechCounter:
	def __init__(self, name, regex, category, count=0):
		self.name = name
		self.regex = re.compile(regex, re.IGNORECASE|re.MULTILINE)
		self.category = category
		self.count = count

	def __repr__(self):
		return self.name

	def match(self, string):
		if self.regex.search(string):
			return True


def new_tech_list():
	return [
		TechCounter('Assembly', r'^(.+\W)?assembly(\W.+?)?$', 'Languages'),
		TechCounter('Bash', r'^(.+\W)?bash(\W.+?)?$', 'Languages'),
		TechCounter('C', r'^(.+\W)?c(\W.+?)?$', 'Languages'),
		TechCounter('C++', r'^(.+\W)?c\+\+(\W.+?)?$', 'Languages'),
		TechCounter('C#', r'^(.+\W)?c#(\W.+?)?$', 'Languages'),
		TechCounter('Clojure', r'^(.+\W)?clojure(\W.+?)?$', 'Languages'),
		TechCounter('Java', r'^(.+\W)?java([- ](\w+|\d))?(\W.+?)?$', 'Languages'),
		TechCounter('Python', r'^(.+\W)?python(\W.+?)?$', 'Languages'),
		TechCounter(
			'JavaScript',
			r'^(.+\W)?javascript(\W.+?)?$|^(.+\W)?es([- ]?\d)?(\W.+?)?$|^(.+\W)?ecmascript([- ]?\d)?(\W.+?)?$|^(.+\W)?js(\W.+?)?$',
			'Languages'
		),
		TechCounter('SQL', r'^(.+\W)?sql(\W.+?)?$', 'Languages'),
		TechCounter('HTML', r'^(.+\W)?html(\d)?(\W.+?)?', 'Languages'),
		TechCounter('CSS', r'^(.+\W)?css(\d)?(\W.+?)?', 'Languages'),
		TechCounter('PHP', r'^(.+\W)?php(\W.+?)?', 'Languages'),
		TechCounter('Go', r'^(.+\W)?go(\W.+?)?$|^(.+\W)?golang', 'Languages'),
		TechCounter('Ruby', r'^(.+\W)?ruby(\W.+?)?', 'Languages'),
		TechCounter('Objective-C', r'^(.+\W)?objective[- ]?c(\W.+?)?', 'Languages'),
		TechCounter('Scala', r'^(.+\W)?scala(\W.+?)?$', 'Languages'),
		TechCounter('Swift', r'^(.+\W)?swift([- ]?\d)?(\W.+?)?$', 'Languages'),
		TechCounter('R', r'^(.+\W)?r(\W.+?)?$', 'Languages'),
		TechCounter('COBOL', r'^(.+\W)?cobol(\W.+?)?', 'Languages'),
		TechCounter('Fortran', r'^(.+\W)?fortran(\W.+?)?', 'Languages'),
		TechCounter('Kotlin', r'^(.+\W)?kotlin(\W.+?)?', 'Languages'),
		TechCounter('XML', r'^(.+\W)?xml(\W.+?)?', 'Languages'),
		TechCounter('TypeScript', r'^(.+\W)?typescript(\W.+?)?', 'Languages'),
		TechCounter('JSON', r'^(.+\W)?json(\W.+?)?', 'Languages'),
		TechCounter('Perl', r'^(.+\W)?perl([- ]?[56])?(\W.+?)?$', 'Languages'),
		TechCounter('Less', r'^(.+\W)?less(\W.+?)?$', 'Languages'),
		TechCounter('Sass', r'^(.+\W)?sass(\W.+?)?$', 'Languages'),
		TechCounter('CoffeeScript', r'^(.+\W)?coffeescript(\W.+?)?', 'Languages'),
		TechCounter('Lisp', r'^(.+\W)?lisp(\W.+?)?$', 'Languages'),
		TechCounter('Pascal', r'^(.+\W)?pascal(\W.+?)?', 'Languages'),
		TechCounter('Dart', r'^(.+\W)?dart(\W.+?)?', 'Languages'),
		TechCounter('F', r'^(.+\W)?f(\W.+?)?$', 'Languages'),
		TechCounter('F#', r'^(.+\W)?f#(\W.+?)?', 'Languages'),
		TechCounter('Haskell', r'^(.+\W)?haskell(\W.+?)?', 'Languages'),
		TechCounter('Lua', r'^(.+\W)?lua(\W.+?)?$', 'Languages'),
		TechCounter('MATLAB', r'^(.+\W)?matlab(\W.+?)?', 'Languages'),
		TechCounter('PowerShell', r'^(.+\W)?powershell(\W.+?)?', 'Languages'),
		TechCounter('Elixir', r'^(.+\W)?elixir(\W.+?)?', 'Languages'),
		TechCounter('GraphQL', r'^(.+\W)?graphql(\W.+?)?', 'Languages'),
		TechCounter('D', r'^(.+\W)?d(\W.+?)?$', 'Languages'),


		TechCounter('React', r'^(.+\W)?react(.?js)?(\W(?!native).+?)?$', 'Frameworks/CMS'),
		TechCounter('Node', r'^(.+\W)?node(.?js)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Spring', r'^(.+\W)?spring([- ]?mvc)?([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Angular', r'^(.+\W)?angular(.?js)?([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Rails', r'^(.+\W)?(ruby[- ]?on[- ]?)?rails([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Django', r'^(.+\W)?django([- ]?(?!rest)\w+)?([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('ASP.NET', r'^(.+\W)?asp.net([- ]?mvc)?([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('React Native', r'^(.+\W)?react[- ]?native([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Ember', r'^(.+\W)?ember(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Vue', r'^(.+\W)?vue(.?js)?([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Flask', r'^(.+\W)?flask([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('DRF', r'^(.+\W)?drf(\W.+?)?$|^(.+\W)?django[- ]?rest[- ]?framework(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('CakePHP', r'^(.+\W)?cake(php)?([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Phoenix', r'^(.+\W)?phoenix([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Express', r'^(.+\W)?express(.?js)?([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Backbone', r'^(.+\W)?backbone(.?js)?([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Drupal', r'^(.+\W)?drupal([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Laravel', r'^(.+\W)?laravel([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Symfony', r'^(.+\W)?symfony([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Pyramid', r'^(.+\W)?pyramid([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Sinatra', r'^(.+\W)?sinatra([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('WordPress', r'^(.+\W)?wordpress([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),
		TechCounter('Magento', r'^(.+\W)?magento([- ]?framework)?(\W.+?)?$', 'Frameworks/CMS'),


		TechCounter('.NET', r'^(.+\W)?.net(\W.+?)?$', 'Platforms/Web Services'),
		TechCounter('Docker', r'^(.+\W)?docker(\W.+?)?$', 'Platforms/Web Services'),
		TechCounter('AWS', r'^(.+\W)?amazon([- ]?web[- ]?service(s)?)?(\W.+?)?$|^(.+\W)?aws(\W.+?)?$', 'Platforms/Web Services'),
		TechCounter('Azure', r'^(.+\W)?azure(\W.+?)?$', 'Platforms/Web Services'),
		TechCounter('Java EE', r'^(.+\W)?java[- ]?ee(\W.+?)?$', 'Platforms/Web Services'),
		TechCounter('Kubernetes', r'^(.+\W)?kubernetes(\W.+?)?$|^(.+\W)?k8s(\W.+?)?$', 'Platforms/Web Services'),
		TechCounter('Apache', r'^(.+\W)?apache(\W.+?)?$', 'Platforms/Web Services'),
		TechCounter('Google Cloud', r'^(.+\W)?google[- ]?cloud(\W.+?)?$', 'Platforms/Web Services'),
		TechCounter('Salesforce', r'^(.+\W)?salesforce(\W.+?)?$', 'Platforms/Web Services'),
		TechCounter('Oracle', r'^(.+\W)?oracle(\W.+?)?$', 'Platforms/Web Services'),
		TechCounter('ROS', r'^(.+\W)?ros(\W.+?)?$|^(.+\W)?robot[- ]?operating[- ]?system(\W.+?)?$', 'Platforms/Web Services'),


		TechCounter('Git', r'^(.+\W)?git(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Hadoop', r'^(.+\W)?(apache[- ])?hadoop(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Apache Spark', r'^(.+\W)?(apache[- ])?spark(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Jenkins', r'^(.+\W)?jenkins(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Chef', r'^(.+\W)?chef(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Redux', r'^(.+\W)?(\w+[- ]?)?redux(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Selenium', r'^(.+\W)?selenium(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Jquery', r'^(.+\W)?jquery(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Elasticsearch', r'^(.+\W)?elasticsearch(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Puppet', r'^(.+\W)?puppet(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Kafka', r'^(.+\W)?(apache[- ])?kafka(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Spring Boot', r'^(.+\W)?spring[- ]?boot(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Ansible', r'^(.+\W)?ansible(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Jira', r'^(.+\W)?(atlassian[- ]?)?jira(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('QT', r'^(.+\W)?(\w[- ]?)?qt([- ]?\d)?(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('TensorFlow', r'^(.+\W)?tensorflow(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Ajax', r'^(.+\W)?ajax(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Twitter Bootstrap', r'^(.+\W)?(twitter[- ]?)?bootstrap(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Bulma', r'^(.+\W)?bulma(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Cucumber', r'^(.+\W)?cucumber(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('Terraform', r'^(.+\W)?terraform(\W.+?)?$', 'Libraries/Tools'),
		TechCounter('SQLAlchemy', r'^(.+\W)?sqlalchemy(\W.+?)?$', 'Libraries/Tools'),


		TechCounter('Unity3D', r'^(.+\W)?unity(3d)?(\W.+?)?$', 'Game Engines'),
		TechCounter('Unreal Engine', r'^(.+\W)?unreal([- ]?engine)?(\W.+?)?$', 'Game Engines'),
		TechCounter('Cry Engine', r'^(.+\W)?cry([- ]?engine)?(\W.+?)?$', 'Game Engines'),


		TechCounter('Web Services', r'^(.+\W)?web[- ]?service(s)?(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Agile', r'^(.+\W)?agile(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Cloud', r'^(.+\W)?cloud(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('REST', r'^(.+\W)?rest(ful)?[- ]?(architecture)?(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Machine Learning', r'^(.+\W)?machine[- ]?learning(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('SysAdmin', r'^(.+\W)?sysadmin(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('DevOps', r'^(.+\W)?devops(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Testing', r'^(.+\W)?testing(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Security', r'^(.+\W)?(\w+)?[- ]?security(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('API ', r'^(.+\W)?api([- ]\w+)?(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('User Interface', r'^(.+\W)?ui(\W.+?)?$|^(.+\W)?user[- ]?interface(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Project Management', r'^(.+\W)?project[- ]?management(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Microservices', r'^(.+\W)?microservice(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('SaaS', r'^(.+\W)?saas(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Continuous Integration', r'^(.+\W)?ci(\W.+?)?$|^(.+\W)?continuous[- ]?integration(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Automation', r'^(.+\W)?automation(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('QA', r'^(.+\W)?qa(\W.+?)?$|^(.+\W)?quality[- ]?assurance(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Test Automation', r'^(.+\W)?test[- ]?automation(\W.+?)?$|^(.+\W)?automated[- ]?test(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Object Oriented Programming', r'^(.+\W)?oop(\W.+?)?$|^(.+\W)?object[- ]?oriented[- ]?programming(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Algorithms', r'^(.+\W)?algorithm(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Scrum', r'^(.+\W)?scrum(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('ETL', r'^(.+\W)?etl(\W.+?)?$|^(.+\W)?extract[,\- ]?transform[,\- ]?load(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Embedded', r'^(.+\W)?embedded(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Big Data', r'^(.+\W)?big[- ]?data(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Computer Science', r'^(.+\W)?cs(\W.+?)?$|^(.+\W)?computer[- ]?science(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('UX', r'^(.+\W)?ux(\W.+?)?$|^(.+\W)?user[- ]?experience(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Test Driven Development', r'^(.+\W)?tdd(\W.+?)?$|^(.+\W)?test[- ]?driven[- ]?develop(e)?ment(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Scalability', r'^(.+\W)?scalability(\W.+?)?$|^(.+\W)?scalable(\W.+?)?$|^(.+\W)?scaling(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Backend', r'^(.+\W)?back[- ]?end(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Frontend', r'^(.+\W)?front[- ]?end(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Unit Testing', r'^(.+\W)?unit[- ]?test(ing)?(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('MVC', r'^(.+\W)?mvc(\W.+?)?$|^(.+\W)?model[- ]?view[- ]?controller(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Neural Networks', r'^(.+\W)?neural[- ]?network', 'Concepts/Skills'),
		TechCounter('Debugging', r'^(.+\W)?debug(ging)?(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Web Applications', r'^(.+\W)?web[- ]?app(s)?(lication(s)?)?(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Design', r'^(.+\W)?design(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Architecture', r'^(\W.+?)?$(.+\W)?architecture(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Functional Programming', r'^(.+\W)?fp(\W.+?)?$|^(.+\W)?functional[- ]?programming(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Virtual Reality', r'^(.+\W)?vr(\W.+?)?$|^(.+\W)?virtual[- ]?reality(\W.+?)?$', 'Concepts/Skills'),
		TechCounter('Cryptography', r'^(.+\W)?crypto(graphy)?(\W.+?)?$', 'Concepts/Skills'),


		TechCounter('Linux', r'^(.+\W)?linux(\W.+?)?$', 'Operating Systems'),
		TechCounter('Android', r'^(.+\W)?android(\W.+?)?$', 'Operating Systems'),
		TechCounter('iOS', r'^(.+\W)?([a-z]+[- ])?ios|^(.+\W)?iphone(\W.+?)?$', 'Operating Systems'),
		TechCounter('Mobile', r'^(.+\W)?mobile(\W.+?)?$', 'Operating Systems'),
		TechCounter('Unix', r'^(.+\W)?unix(\W.+?)?$', 'Operating Systems'),
		TechCounter('Windows', r'^(.+\W)?windows(\W.+?)?$', 'Operating Systems'),


		TechCounter('MySQL', r'^(.+\W)?mysql(\W.+?)?$', 'Databases'),
		TechCounter('PostgreSQL', r'^(.+\W)?postgre(sql)?s?(\W.+?)?$', 'Databases'),
		TechCounter('Mongodb', r'^(.+\W)?mongo(db)?(\W.+?)?$', 'Databases'),
		TechCounter('SQL Server', r'^(.+\W)?(microsoft[- ]?)?sql[- ]?server(\W.+?)?$|^(.+\W)?mssql(\W.+?)?$', 'Databases'),
		TechCounter('NoSQL', r'^(.+\W)?nosql(\W.+?)?$', 'Databases'),
		TechCounter('Cassandra', r'^(.+\W)?(apache[- ])?cassandra(\W.+?)?$', 'Databases'),
		TechCounter('Redis', r'^(.+\W)?redis(\W.+?)?$', 'Databases'),
		TechCounter('SQLite', r'^(.+\W)?sqlite(\W.+?)?$', 'Databases'),
		TechCounter('MariaDB', r'^(.+\W)?maria([- ]?db)?(\W.+?)?$', 'Databases'),
	]