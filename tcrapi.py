
import pandas as pd
import sankey as sk

class TCRAPI:

    def load_tcr(self, filename):
        self.tcr = pd.read_csv(filename) # our dataframe (database) - STATE VARIABLE
                                          # Lives as long as the object lives

    def get_diagnosis(self):
       # dhigh = self.tcr[self.tcr['Thyroid_Cancer_Risk'] == 'High']
        diag = self.tcr['Diagnosis'].unique()
        diag = [str(p) for p in diag if ";" not in str(p)]
        return sorted(diag)

    def get_countries(self):
            countries = self.tcr['Country'].dropna().unique()  # Drop any NaN values and get unique countries
            return sorted(countries)  # Sort the list alphabetically


    def extract_local_network(self, diagnosis, min_cases, countries=None):
        """
        Extract the diagnosis-country connections
        :param tcr: thyroid cancer data
        :param diagnosis:  patient diagnosis
        :param min_cases: # of cases of malignant cancer linked to age range
        :return: A new dataframe with the relevant diagnosis-age links --> sankey diagram
                 with columns: diagnosis, country, age, ncases
        """
        # filter columns
        tcr = self.tcr[['Diagnosis', 'Age', 'Country']]

        tcr['Diagnosis'] = tcr['Diagnosis'].astype(str)
        tcr['Country'] = tcr['Country'].astype(str)
        tcr['Age'] = tcr['Age'].apply(lambda x: 'Above 50' if x > 50 else 'Under 50')



        if countries:
            tcr = tcr[tcr['Country'].isin(countries)]

        # count the number of cases
        tcr = tcr.groupby(['Diagnosis', 'Age', 'Country']).size().reset_index(name='ncases')

        # sort data
        tcr.sort_values('ncases', ascending=True, inplace=True)

        # discard cases with less than <min_cases>
        tcr = tcr[tcr.ncases >= min_cases]

        # age range for diagnosis of interest
        tcr_diagnosis = tcr[tcr['Diagnosis'] == diagnosis]

        # Find all connections from diagnosis to age
        local = tcr[tcr['Age'].isin(tcr_diagnosis['Age'])]

        return local


def main():
    # Initialize API
    tcrapi = TCRAPI()
    tcrapi.load_tcr('tcr.csv')

    # search parameters
    diagnosis = 'Malignant'

    num_cases = 4
    countries = ['USA', 'Canada', 'Germany']

    # filter data to build the dataframe for sankey
    local = tcrapi.extract_local_network(diagnosis, num_cases, countries=countries)
    print(local)

    # Generate manually our sankey diagram
    sk.show_sankey(local, "Diagnosis", "Age", vals='ncases')




if __name__ == '__main__':
    main()

