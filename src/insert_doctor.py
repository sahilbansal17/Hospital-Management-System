from add_util import add_into_table

def add_doctor(Name, Gender, DOB, Qual, Contact, Address, email, salary):
	doctor = {
		'name': Name,
		'gender': Gender,
		'dob': DOB,
		'contact_no': Contact,
		'address': Address,
		'department': Department,
		'qualification': Qual,
		'email': email,
		'salary': salary
	}
	add_into_table("Doctor", doctor)