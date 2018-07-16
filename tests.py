def get_slicing_ends(records,records_per_page,current_beggining,my_data,target_table):
    '''
    function that determines the ends where the data will be sliced
    each page is assigned 20 records then stores them to database
    '''
    lenght = records / records_per_page
    list1 = []
    m = 0
    current_end = 0

    for i in range(0,int(lenght)):
        current_end = current_beggining + records_per_page
        list1.append([current_beggining,current_end])
       
        # list1.append(records_per_page * m)
        
        # access properties from each item and use it to create datasets for datatable as lists
        # sliced_data = my_data[current_beggining:current_end]
        # my_data1 = create_values(sliced_data)

        # the code below slices the data based on the on the given list of lenght and save the bunch to the database
        # new_cache = target_table(raw_table_data = {'datasets':my_data1[0],'columns':my_data1[1]},page = i)
        # new_cache.save() 
        current_beggining += records_per_page
        m +=1
    
    # add the last part here
    # list1.append([list1[len(list1)-1][1]])
        
    print (list1)

def create_values(data):
    '''
    Function that loops through the properties of each item in response.json['feature]
    and creates a list containing list with the arrays for the data table
    '''
    list_of_values = []

    # getting the column titles
    column_titles1 = data[0]['properties'].keys()
    column_titles = [{'title':value} for value in column_titles1]

    # looping through every single item given from the response
    for item in data:
        # temporary_list = []
        # getting values associated with every key in item['properties'] and appending to list of properties
        instance_values = item['properties'].values()
        # temporary_list.append(instance_values)
        list_of_values.append(instance_values)

    # the code below list of values and column titles inside one list
    return [list_of_values,column_titles]

records = 20
records_per_page = 2
current_beggining = 0
my_data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
target_table = 'Cache_Table_Data'

get_slicing_ends(records,records_per_page,current_beggining,my_data,target_table)

