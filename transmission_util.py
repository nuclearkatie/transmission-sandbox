import math
import csv
#from isotope import Isotope


def create_data_dict(file):
    """
    Takes csv file with isotopic information and turns it into an
    easily-searchable list of dictionaries

    inputs:
    * a file name (csv format) as a string, i.e. 'isotopes.csv' 
	
    outputs:
    * a list of dictionaries called data
    """
    with open(file, 'r') as f:
        readline = csv.reader(f, dialect="excel",
		                      quoting=csv.QUOTE_NONNUMERIC)
        isotope_list = list(readline)

    N_A = 6.02214*10**23

    data=[]    

    for i in range(1,len(isotope_list)):
        data.append(dict(zip(isotope_list[0], isotope_list[i])))
	
    for i in range(len(data)):
        data[i]['Sigma']=(data[i]['microscopic_a_xs']*data[i]['density']
                    *N_A/data[i]['A'])
 
    return data


def cross_section_bounds(x, transmission, error):
	"""
	Determines the experimental macroscopic cross section within a margin of
	error
	
	inputs:
	* thickness: in cm
	* transmission: as a fraction
	* error: as a fraction, such as 0.5
	
	outputs:
	* [min_Sig, max_Sig]: a list with two values, the minimum and maximum
	macroscopic cross sections within the margin of error 
	"""

	Sig_t = - math.log(transmission) / x
	
	min_Sig = Sig_t * (1-error)
	max_Sig = Sig_t * (1+error)
	
	return [min_Sig,max_Sig]


def desired_isotopes(data,isotopes='all'):
    """
	Returns a list of isotopes to search through. 
	
	inputs:
	isotopes_list: a string or list of strings with the isotopes to search.
	Default value is all isotopes. Current options to specify include:
	* 'all'
	* 'fissile'
	* 'radioactive'
	* a single isotope, i.e. '235U'
	* a list of isotopes, i.e. ['235U','239Pu']
	
	outputs:
	* a list of isotopes
	"""

    if isotopes=='fissile':
        desired_isotopes = ['233U', '235U', '239Pu']
    elif isotopes == 'radioactive':
        desired_isotopes = ['1A','3C','233U', '235U', '239Pu', '238U']
    elif isotopes=='all':
        desired_isotopes = [d['isotope'] for d in data]
    elif type(isotopes)==str:
        desired_isotopes = [isotopes]
    elif type(isotopes)==list:
        desired_isotopes = isotopes

    return desired_isotopes


def not_materials(data,desired_isotope,bounds):
    """
	Returns a list of isotopes that can be ruled out
	
	inputs:
	* data: isotope data
	* desired_isotopes: a list of isotopes to check
	* bounds: a list with two values, the minimum and maximum macroscopic xs
	
	outputs:
	* a list of isotopes that can be ruled out
	"""

    isotopes_outside=[]

    for iso in desired_isotope:
        #print(isotope + str([d['Sigma'] for d in data if d['isotope']==isotope]))
        isotopes_outside+=([d['isotope'] for d in data if d['isotope']==iso and (d['Sigma']<bounds[0] or d['Sigma']>bounds[1]
)])
        #print(isotopes_outside)
	
    return isotopes_outside