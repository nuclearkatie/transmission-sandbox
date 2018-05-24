from transmission_util import create_data_dict, cross_section_bounds, desired_isotopes, not_materials

def main(x,transmission,error):

    data = create_data_dict('isotopes.csv')

    #print([d['Sigma'] for d in data])

    Sigma = cross_section_bounds(x,transmission,error)

    desired_isotope = desired_isotopes(data,'all')
    print('The isotopes being checked are:\n' + str(desired_isotope) + '\n')

    outside = not_materials(data,desired_isotope,Sigma)

    print('The isotopes that can be ruled out from this measurement are:\n'
          + str(outside) + '\n')
    print('Please note that this tool is only for informal use\n')