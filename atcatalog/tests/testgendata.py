# -*- coding: utf-8 -*-
'''
Test cases for the database model
'''
import faker
import random
from atcatalog import app
from unittest import TestCase, main
from atcatalog.data.gendata import *


class GenDataTest(TestCase):
	'''
	Test the generation of test data
	'''

	def test_create_random_code(self):
		'''
		Test the creation of a random code
		'''
		self.assertIn(create_random_code(), LANG_DICT.keys())

	def test_create_random_codes(self):
		'''
		Test the creation of a list of codes
		'''
		num = len(LANG_DICT.keys()) + 2
		for idx in range(1, num):
			for code in create_random_codes(idx):
				self.assertIn(code, LANG_DICT.keys())

	def test_create_all_codes(self):
		'''
		Test all codes are created
		'''
		self.assertEquals(create_all_codes(),LANG_DICT.keys())

	def test_create_random_user_data(self):
		'''
		Test the creation of user data with language codes
		'''
		num = len(LANG_DICT.keys()) + 2
		for idx in range(1, num):
			codes = create_random_codes(idx)
			user_data = create_random_user_data(codes)
    		self.assertEquals(user_data[2], codes)

	def test_create_random_sentence_data(self):
		'''
		Test the creation of sentence data
		'''
		lid = random.randint(1,100)
		uid = random.randint(1,100)
		self.assertEquals(create_random_sentence_data(lid, uid)[3], lid)
		self.assertEquals(create_random_sentence_data(lid, uid)[4], uid)


if __name__ == '__main__':
	main()
