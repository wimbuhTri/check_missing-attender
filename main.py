import numpy as np 
import os, glob

nama_target = input("P:")
judul_praktikum = "P"+nama_target
nama_target = "p"+nama_target+".txt"



ref_file = np.loadtxt('ref.txt',delimiter='\n',dtype='str')
tar_file = np.loadtxt(nama_target,delimiter='\n',dtype='str')

def to_lowwer(array):
	count = 0
	for element in array:
		array[count] = element.lower()
		count += 1
	return array

ref =  to_lowwer(ref_file)
tar =  to_lowwer(tar_file)

def simplify_name(array):
	count = 0
	for student in array:
		student = student.split()
		array[count] = student[0] + " " + student[1]
		count += 1
	return array

ref = simplify_name(ref)
tar = simplify_name(tar)

file1 = open('rekap.txt', 'a')
for def_student in ref:
	is_found = False
	for attender in tar:
		if def_student == attender:
			is_found = True
	if is_found == False:
		file1.writelines(f'{def_student} : {judul_praktikum}\n')
		print(f'{def_student}') #' is belum ngumpul')
	else:
		if len(ref) == len(tar):
			print("ngumpul semua")
			file1.writelines(f'{judul_praktikum} OK\n')
			break
file1.writelines(f'\n')
file1.close()


myFiles = glob.glob('*.txt')

