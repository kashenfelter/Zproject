# Process the profiles in MongoDB collection 
# Of extended profiles to get the feature I will use
# I will define the follwing differnet methods:
import utils
import json
log = True
import pdb
from datetime import datetime

def compute_education_fields(profile):
	''' Returns the normalized values for educaiton '''
	
	parsed_ed_dict = {'phd_1': -1, 'phd_2': -1, "mas_1": -1, \
	 "mas_2" : -1, "bc_1": -1 , "bc_2": -1, "mba_1": -1, "mba_2": -1}
	# All lower
	mba_lookup = ['mba', 'm.b.a']
	phd_lookup =  ['phd', 'pd.d.', 'ph.d.', 'doctor of philosophy']
	master_lookup =  ['master', "ms", "m.s.", "m.s", "ma", "m.a.", "msc", 'm.sc.', 'meng']
	# Not sure if I want to add diploma
	bach_lookup = ['bachelor', 'bachelors', 'b.a.', 'bsc', 'b.s', 'b.sc',\
	 'b.sc.', 'B.E.', 'b.a', 'b.tech', 'bs', 'ba', 'b.sself.', 'b.s.']
	ed_fields = ['computer science', 'computer engineering', 'mathematics', 'physics', \
	'statistics', 'economics', 'psychology', 'engineering', 'bioinformatics', \
	'neuroscience', 'biology', 'astronomy', 'linguistics', 'electronics']

	# ed_type_lookup = [phd_lookup, master_lookup, bach_lookup]
	found_phd = 0
	found_master = 0
	found_bachelor = 0
	found_mba = 0
	# First check if the field is there and is empty
	# The step below parse the fields for 
	if len(profile['educations'])==0:
		return  parsed_ed_dict 
	else:
		if 'added_education' in profile:
			for education in profile['educations']:
				if ',' in education['description']:
					# I may want to construct an array of topics 
					is_phd = False
					is_mas = False
					is_bac = False
					is_mba = False
					ed_topic_list=[]
					ed_type = education['description'].split(',')[0].strip().lower()
					if len(education['description'].split(','))>2:
						for i in range(1, len(education['description'].split(','))):
							ed_topic_list.append(education['description'].split(',')[i].strip().lower())
					else:
							ed_topic_list.append(education['description'].split(',')[1].strip().lower())
					if log:
						print "Parsed education type: ", ed_type
						print "Parsed education topic: ", ed_topic_list
					
					# Refactor code below.
					# Check if is an MBA
					if ed_type in mba_lookup:
						is_mba = True
						found_mba+=1
					else:
						for mba in mba_lookup:
							if mba in ed_type:
								found_mba+=1
								is_mba = True
								break

					# Check if is a Phd
					if ed_type in phd_lookup:
						is_phd = True
						found_phd+=1
					else:
						for phd in phd_lookup:
							if phd in ed_type:
								found_phd+=1
								is_phd = True
								break
						
					# Checks if is a master
					if ed_type in master_lookup:
						is_mas = True
						found_master+=1
					else:
						for mas in master_lookup:
							if mas in ed_type.split(' '):
								found_master+=1
								is_mas = True
								break

					# Checks if is a Bachelor
					if ed_type in bach_lookup:
						is_bac = True
						found_bachelor+=1
					else:
						for bac in bach_lookup:
							if bac in ed_type.split(' '):
								found_bachelor+=1
								is_bac = True
								break
					
					# Parse the educaiton field for MBA 
					if is_mba:
						if found_mba==1:
							parsed_ed_dict['mba_1'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['mba_1'] = field
										break

						if found_mba==2:
							parsed_ed_dict['mba_2'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['mba_2'] = field
										break
					
					# Parse the educaiton fiels for Phd
					# pdb.set_trace()
					if is_phd:
						if found_phd==1:
							parsed_ed_dict['phd_1'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['phd_1'] = field
										break

						if found_phd==2:
							parsed_ed_dict['phd_2'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['phd_1'] = field
										break

					# Parse the educaiton fiels for Master
					if is_mas:
						if found_master==1:
							parsed_ed_dict['mas_1'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['mas_1'] = field
										break

						if found_master==2:
							parsed_ed_dict['mas_2'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['mas_2'] = field
										break

					# Parse the educaiton fiels for Bachelor
					if is_bac:			
						if found_bachelor==1:
							parsed_ed_dict['bc_1'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['bc_1'] = field
										break

						if found_bachelor==2:
							parsed_ed_dict['bc_2'] = 1	
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['bc_2'] = field
										break	
		else:
			print ("API education to be parsed")
			# Here parse My API information
			print profile
			num_ed = int(profile['educations']['_total'])
			if num_ed >0:
				print "Parsing educations"
				for i in range(num_ed):
					ed_topic_list=[]
					is_phd = False
					is_mas = False
					is_bac = False
					is_mba = False
					education = profile['educations']['values'][i]
					print education
					ed_type = education['degree'].strip().lower()
					if len(education['fieldOfStudy'].split(','))>1:
						for i in range(1, len(education['fieldOfStudy'].split(','))):
							ed_topic_list.append(education['fieldOfStudy'].split(',')[i].strip().lower())
					else:
							ed_topic_list.append(education['fieldOfStudy'].split(',')[0].strip().lower())
					if log:
						print "Parsed education type: ", ed_type
						print "Parsed education topic: ", ed_topic_list
						# pdb.set_trace()	
					# Here just do the same thing as before
					# Check if is an MBA
					if ed_type in mba_lookup:
						is_mba = True
						found_mba+=1
					else:
						for mba in mba_lookup:
							if mba in ed_type:
								found_mba+=1
								is_mba = True
								break

					# Check if is a Phd
					if ed_type in phd_lookup:
						is_phd = True
						found_phd+=1
					else:
						for phd in phd_lookup:
							if phd in ed_type:
								found_phd+=1
								is_phd = True
								break
						
					# Checks if is a master
					if ed_type in master_lookup:
						is_mas = True
						found_master+=1
					else:
						for mas in master_lookup:
							if mas in ed_type.split(' '):
								found_master+=1
								is_mas = True
								break

					# Checks if is a Bachelor
					if ed_type in bach_lookup:
						is_bac = True
						found_bachelor+=1
					else:
						for bac in bach_lookup:
							if bac in ed_type.split(' '):
								found_bachelor+=1
								is_bac = True
								break
					
					# Parse the education fields for MBA 
					if is_mba:
						if found_mba==1:
							parsed_ed_dict['mba_1'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['mba_1'] = field
										break

						if found_mba==2:
							parsed_ed_dict['mba_2'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['mba_2'] = field
										break
					
					# Parse the education fields for Phd
					# pdb.set_trace()
					if is_phd:
						if found_phd==1:
							parsed_ed_dict['phd_1'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['phd_1'] = field
										break

						if found_phd==2:
							parsed_ed_dict['phd_2'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['phd_1'] = field
										break

					# Parse the education fields for Master
					if is_mas:
						if found_master==1:
							parsed_ed_dict['mas_1'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['mas_1'] = field
										break

						if found_master==2:
							parsed_ed_dict['mas_2'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['mas_2'] = field
										break

					# Parse the education fields for Bachelor
					if is_bac:			
						if found_bachelor==1:
							parsed_ed_dict['bc_1'] = 1
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['bc_1'] = field
										break

						if found_bachelor==2:
							parsed_ed_dict['bc_2'] = 1	
							for field in ed_fields:
								for topic in ed_topic_list:
									if field in topic:
										parsed_ed_dict['bc_2'] = field
										break

			else:
				return parsed_ed_dict


	return parsed_ed_dict



def compute_ds_job_fields(profile):
	''' Returns the values for the data scientist
	job related fields'''
	ds_dict = {"ds_job_current": 0, "ds_job_past": 0 , \
	"ds_in_head": 0,  "ds_in_summary":0 }

	# Checks if the profile has data scientist in head
	if 'headline' in profile:
		headline = profile['headline']
		print headline
		if ("data scientist" in headline.lower()) or \
		("data science" in headline.lower()):
			print "Ds in head"
			ds_dict['ds_in_head'] = 1

	# Chekcs if profile has data scientist in summary
	if 'summary' in profile:
		summary  = profile['summary']
		print summary
		if "data scientist" in summary.lower():
			print "Ds in summary"
			ds_dict['ds_in_summary'] = 1

	# Check if profile has dat science in title of  positions
	num_positions = int(profile['positions']['_total'])
	for i in range(num_positions):
		position = profile['positions']['values'][i]
		title = position['title']
		is_current = position['isCurrent']
		if ("data scientist" in title.lower()) or\
		("data science" in title.lower()):
			if is_current:
				print "Data scientist in current position"
				ds_dict['ds_job_current'] = 1
			else:
				print "Data scientist in old position"
				ds_dict['ds_job_past'] = 1

	return ds_dict

def process_education(db, collection):
	''' Computes the fields for education and stores
	them in collection '''
	# Get a sample profile form the extended profiles:
	print collection
	# cut_date = datetime(2013, 11, 5)
	profiles = collection.find()
	for profile in profiles:
		print ("========================")
		
		if 'educations' in profile:
			computed_ed = compute_education_fields(profile)
			
			if log:
				print "Education fields:" , profile['educations']
				print computed_ed

			# The line below colelct things in a dict
			# It is more difficult with Pandas..
			computed_ed_dict = {"computed_ed" : computed_ed}
			date =  profile['date']
			# print date
			# if date > cut_date:
			# 	# pdb.set_trace()
			# 	print "Gotcha"
			# Insert the new fileds (currently not grouped)

			utils.addfields_profile(collection, computed_ed, profile['id'])

def process_ds_fields(db, collection):
	''' Computes the fields for ds jobs and stores
	them in collection '''
	# Get a sample profile form the extended profiles:
	profiles = collection.find()
	for profile in profiles:
		print ("========================")

		if 'positions' in profile:
			computed_ds_fields = compute_ds_job_fields(profile)
			if log:
				print "Positions: ",  profile['positions']
				print computed_ds_fields
			
			# The line below colelct things in a dict
			# It is more difficult with Pandas..
			computed_ds_filed_dict = {"computed_ds_fields": computed_ds_fields}

			# Now let's write the data on the db (currently not grouped)
			utils.addfields_profile(collection, computed_ds_fields, profile['id'])

def main():
	# Selecting the ext_profiles_education
	db, collection = utils.initializeDb("zproject", "new_math_ba_stat_se_ds_full_labels_good")
	# print collection
	process_education(db, collection)
	process_ds_fields(db, collection )

if __name__ == '__main__':
	main()

