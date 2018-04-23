

df = pd.read_csv('multi_level_interpolate.csv', sep='\t')

# Generate a dummy list to hold the monthly interpolated
# dataframe for each grouper object 
df_list = list()

# Generating the monthly data 
for i,j in df.groupby(['loanNumber', 'Wholesale_loanid']):
    j['date']=pd.to_datetime(j.date)
    j.set_index('date', inplace=True)
    df_list.append(j.resample('M').interpolate().fillna(method='pad'))

    
# Generating the final monthly interpolated dataframe 
fnl = pd.concat(df_list)