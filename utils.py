import pandas as pd 
import plotly.express as px

class data_handle():

    def make_country_df(data1 , data2):
        """
        Function to 
        Input : Dataframes, with different years complete data(2019,2018)
        Output: Dataframe, with country level data for each year as columns/variables
        """
        df = pd.DataFrame()
        
        ############2019#########
        country_data_1 = pd.DataFrame(data1.groupby('Country').MainBranch.agg('count'))
        country_data_1.reset_index(inplace = True)
        country_data_1.columns = ['Country', '2019']
        ############2018#########
        data2 = data2[data2['Student']=='No']
        country_data_2 = pd.DataFrame(data2.groupby('Country').DevType.agg('count'))
        country_data_2.reset_index(inplace = True)
        country_data_2.columns = ['Country', '2018']
        
        ##############Inner joining############# 
        temp = pd.merge(country_data_1 , country_data_2, on='Country')
        return temp
    
    def make_dev(data_1, data_2):
        """
        Function to make dataframe for 2019 and 2018 data with unique Developer Types
        Inputs : data_19 and data_18 dataframes 
        Outputs : data18 and data19 dataframes with uniques rows of Developer types 
        """
        ###########2019#########
        df1 = pd.DataFrame(data_1.set_index(data_1.columns.drop('DevType',1).tolist()).DevType.str.
                           split(';', expand=True).stack().reset_index().rename(columns={0:'DevType'}).loc[:, data_1.columns])
        ###########2018#########
        df2 = pd.DataFrame(data_2.set_index(data_2.columns.drop('DevType',1).tolist()).DevType.str.
                           split(';', expand=True).stack().reset_index().rename(columns={0:'DevType'}).loc[:, data_2.columns])

        return df1, df2
    
    
    def plot_missing(self,png=False):
        """
        Function to plot Missing data in the dataframe
        Input: dataframe
        Output: Bar-Plot
        """
        missing_data = self.isnull().sum()
        missing_df = pd.DataFrame(missing_data.drop(missing_data[missing_data == 0].index).sort_values(ascending=False),
                                 columns = ['values'])
        fig = px.bar(data_frame = missing_df, x = missing_df.index, y = missing_df.values, text =missing_df.values,
                  title = "Missing values count")
        if png:
            fig.show('png')
        else:
            fig.show()
            
            
    def make_lang(data_1, data_2):
        """
        Function to make dataframe for 2019 and 2018 data with unique Languages 
        Inputs : data_19 and data_18 dataframes 
        Outputs : data18 and data19 dataframes with uniques rows of Language  
        """
        ###########2019#########
        df1 = pd.DataFrame(data_1.set_index(data_1.columns.drop('LanguageWorkedWith',1).tolist()).LanguageWorkedWith.str.
                           split(';', expand=True).stack().reset_index().rename(columns={0:'LanguageWorkedWith'}).loc[:, data_1.columns])
        ###########2018#########
        df2 = pd.DataFrame(data_2.set_index(data_2.columns.drop('LanguageWorkedWith',1).tolist()).LanguageWorkedWith.str.
                           split(';', expand=True).stack().reset_index().rename(columns={0:'LanguageWorkedWith'}).loc[:, data_2.columns])
        return df1, df2
    
    
    def make_edu(data_1, data_2):
        """
        Function to make dataframe for 2019 and 2018 data with unique Languages 
        Inputs : data_19 and data_18 dataframes 
        Outputs : data18 and data19 dataframes with uniques rows of Language  
        """
        ###########2019#########
        df1 = pd.DataFrame(data_1.set_index(data_1.columns.drop('EduOther',1).tolist()).EduOther.str.
                           split(';', expand=True).stack().reset_index().rename(columns={0:'EduOther'}).loc[:, data_1.columns])
        ###########2018#########
        df2 = pd.DataFrame(data_2.set_index(data_2.columns.drop('EducationTypes',1).tolist()).EducationTypes.str.
                           split(';', expand=True).stack().reset_index().rename(columns={0:'EducationTypes'}).loc[:, data_2.columns])
        return df1, df2
