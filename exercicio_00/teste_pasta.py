import os
def file_path(path):
	print(path)
	return [os.path.join(p,file) for p, _, files in os.walk(os.path.abspath(path)) for file in files]

print(file_path('alunos'))