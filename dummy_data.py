import pandas as pd
from faker import Faker
import streamlit as st

def dummy_data(col_name, col_type, number_of_records = 1000):
    rec = []
    
    if st.session_state.SQL_col == True:
        if col_type == 'int':
            for i in range(number_of_records):
                rec.insert(i,fk.random_int(1,st.session_state.number_of_rows))
        elif col_type.find('string') >= 0:
            x = int(col_type[len('string'):])
            for i in range(number_of_records):
                rec.insert(i,"'" + fk.text(max_nb_chars = x).replace("'","''") + "'")
        elif col_type == 'id':
            for i in range(number_of_records):
                rec.insert(i,i+1)
        elif col_type == 'phone number':
            for i in range(number_of_records):
                rec.insert(i,"'" + fk.phone_number().replace("'","''") + "'")
        elif col_type == 'address(full)':
            for i in range(number_of_records):
                rec.insert(i,"'" + fk.address().replace("'","''") + "'")
        elif col_type == 'address(street)':
            for i in range(number_of_records):
                rec.insert(i,"'" + fk.street_address().replace("'","''") + "'")
        elif col_type == 'name':
            for i in range(number_of_records):
                rec.insert(i,"'" + fk.name().replace("'","''") + "'")
        elif col_type == 'bool':
            for i in range(number_of_records):
                rec.insert(i,fk.pybool())
        elif col_type == 'alphanumeric':
            for i in range(number_of_records):
                rec.insert(i,"'" + fk.password(length=40, special_chars=False).replace("'","''") + "'")
        elif col_type == 'datetime':
            for i in range(number_of_records):
                t = fk.time()
                d = str(fk.date_between(start_date='-2y'))
                rec.insert(i,"'" + d + ' ' + t + "'")
        elif col_type == 'email':
            for i in range(number_of_records):
                rec.insert(i,"'" + fk.ascii_free_email() + "'")
    else:
        if col_type == 'int':
            for i in range(number_of_records):
                rec.insert(i,fk.random_int(1,st.session_state.number_of_rows))
        elif col_type.find('string') >= 0:
            x = int(col_type[len('string'):])
            for i in range(number_of_records):
                rec.insert(i,fk.text(max_nb_chars = x))
        elif col_type == 'id':
            for i in range(number_of_records):
                rec.insert(i,i+1)
        elif col_type == 'phone number':
            for i in range(number_of_records):
                rec.insert(i,fk.phone_number())
        elif col_type == 'address(full)':
            for i in range(number_of_records):
                rec.insert(i,fk.address())
        elif col_type == 'address(street)':
            for i in range(number_of_records):
                rec.insert(i,fk.street_address())
        elif col_type == 'name':
            for i in range(number_of_records):
                rec.insert(i,fk.name())
        elif col_type == 'bool':
            for i in range(number_of_records):
                rec.insert(i,fk.pybool())
        elif col_type == 'alphanumeric':
            for i in range(number_of_records):
                rec.insert(i,fk.password(length=40, special_chars=False))
        elif col_type == 'datetime':
            for i in range(number_of_records):
                t = fk.time()
                d = str(fk.date_between(start_date='-2y'))
                rec.insert(i,d + ' ' + t)
        elif col_type == 'email':
            for i in range(number_of_records):
                rec.insert(i,fk.ascii_free_email())
    
    fill_data.update({col_name : rec})

def col_count():
    st.session_state.col_num = st.session_state.col_num + 1
    # add_col()
def string_switch(t, n):
    if st.session_state[t] == 'string':
        st.session_state['sl_' + str(n) + '_dis'] = False
    else:
        st.session_state['sl_' + str(n)] = ''
        st.session_state['sl_' + str(n) + '_dis'] = True

def add_col():
    # print(st.session_state.col_num)
    if st.session_state.col_num == 1:
        if 'sl_' + str(st.session_state.col_num) not in st.session_state:
            st.session_state['sl_' + str(st.session_state.col_num) + '_dis'] = True
        ct.markdown('###')
        col1, col2, col3 = ct.columns(3)
        col1.text_input(label='column name',placeholder='Enter Column Name', key='ti_' + str(1))
        col2.selectbox(label='column type', options=opt, key='sb_' + str(1), on_change=string_switch, args=('sb_' + str(1),1),index=opt.index('id'))
        col3.text_input(label='string length',placeholder='If type string, specify length here', key='sl_' + str(1), disabled=st.session_state['sl_' + str(st.session_state.col_num) + '_dis'])
    else:
        for i in range(0,st.session_state.col_num):
            if 'sl_' + str(i + 1) not in st.session_state:
                st.session_state['sl_' + str(i + 1) + '_dis'] = True
            ct.markdown('###')
            col1, col2, col3 = ct.columns(3)
            col1.text_input(label='column name',placeholder='Enter Column Name', key='ti_' + str(i+1))
            col2.selectbox(label='column type', options=opt, key='sb_' + str(i+1), on_change=string_switch, args=('sb_' + str(i + 1), i + 1),index=opt.index('id'))
            col3.text_input(label='string length',placeholder='If type string, specify length here', key='sl_' + str(i+1), disabled=st.session_state['sl_' + str(i + 1) + '_dis'])
    

fk =  Faker(['en_US'])
fill_data  = {}
opt = ['id','int','string','datetime','name','bool','phone number', 'address(full)', 'address(street)', 'alphanumeric', 'email']
opt.sort()
def create_data():
    if st.session_state.col_num == 1 and st.session_state['ti_1'] == '':
        st.error('No Columns Entered')
    else:
        columns = []
        columns_types = []
        if st.session_state.col_num == 1:
            columns.insert(0,st.session_state['ti_1'])

            if st.session_state['sb_1'] == 'string':
                columns_types.insert(1,st.session_state['sb_1'] + st.session_state['sl_1'])
            else:
                columns_types.insert(1,st.session_state['sb_1'])

        for i in range(0,st.session_state.col_num):
            columns.insert(i + 1,st.session_state['ti_' + str(i + 1)])

            if st.session_state['sb_' + str(i + 1)] == 'string':
                columns_types.insert(i + 1,st.session_state['sb_' + str(i + 1)] + st.session_state['sl_' + str(i + 1)])
            else:
                columns_types.insert(i + 1,st.session_state['sb_' + str(i + 1)])

        for c in range(len(columns)):
            dummy_data(columns[c], columns_types[c], st.session_state.number_of_rows)

            # print(fill_data)

        
        df = pd.DataFrame(fill_data)
        if st.session_state.SQL_col == True:
            col = '('

            for c in df.columns:
                col = col + c + ', '

            col = col[0:len(col)-2] + ')'

            if st.session_state.TableName == '':
                ins_st = 'insert into [TABLENAME] ' + col + ' values '
            else:
                ins_st = 'insert into ' + st.session_state.TableName + ' ' + col + ' values '

            df['SQL'] = ins_st + '(' + df.astype(str).apply(','.join, axis=1) + ')'


        ct.markdown('###')
        ct.dataframe(df)
        ct.download_button('Download Data', df.to_csv(),file_name='dummy_data.csv')

#page config
st.set_page_config(page_title='Dummy Data Creator', layout='wide',page_icon='https://cdn-icons-png.flaticon.com/512/149/149206.png')

if 'TableName' not in st.session_state:
    st.session_state['TableName'] = ''

#sidebar
sd = st.sidebar
sd.header('Column Types')
sd.markdown('---')
sd.markdown('- **address(full):** a full address Street City, State Zip')
sd.markdown('- **address(street):** street address only')
sd.markdown('- **alphanumeric:** a random alphanumeric string')
sd.markdown('- **bool:** assigns True and False randomly')
sd.markdown('- **datetime:** a random datetime in the last 2 years')
sd.markdown('- **email:** a random free email address')
sd.markdown('- **id:** main id for table, counts by row')
sd.markdown('- **int:** random integers between 1 and row count')
sd.markdown('- **name:** random name')
sd.markdown('- **phone number:** fake phone numbers')
sd.markdown('- **string:** a random block of text at desired length')

#main page
col1, col2 = st.columns([.2,5])
col1.image('https://cdn-icons-png.flaticon.com/512/149/149206.png',)
col2.title('Dummy Data Creator')
st.markdown('---')
if 'col_num' not in st.session_state:
    st.session_state.col_num = 1
col1, col2, col3= st.columns([1,1,1])
col1.button('Add Column', on_click=col_count)
col2.button('Create DF', on_click = create_data)
col2.number_input(label='Number of Rows',key='number_of_rows', value=1000)
col3.checkbox("Add SQL Insert Statement", value=True, key='SQL_col')
if st.session_state.SQL_col == True:
    col3.text_input('Table Name',key='TableName',)
st.markdown('###')
ct = st.container()
add_col()

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """


st.markdown(hide_st_style, unsafe_allow_html=True)
