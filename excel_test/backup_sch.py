import glob
import shutil

path = 'C:/Users/USER/Documents/notebook_workspace/excel_test/'

for fname in glob.glob(path + 'origin/*.txt'):
	shutil.copy(fname, path + 'backup')

