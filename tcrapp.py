from tcrapi import TCRAPI
import sankey as sk

def main():

    # Initialize the API
    tcrapi = TCRAPI()
    tcrapi.load_tcr("tcr.csv")


    # search parameters
    diagnosis = 'Malignant'
    num_cases = 4
    countries = ['USA', 'Canada', 'Germany']

    # filter data to build the dataframe for sankey
    local = tcrapi.extract_local_network(diagnosis, num_cases, countries=countries)
    print(local)

    # Generate manually our sankey diagram
    sk.show_sankey(local, 'Diagnosis', 'Age', vals='ncases')



main()

