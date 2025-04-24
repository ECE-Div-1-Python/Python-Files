import openpyxl
file= "files/file2.xlsx"
wb=openpyxl.load_workbook(file)
sheet=wb.active
st={}
for row in sheet.iter_rows(min_row=2,values_only=True):
    rollno,name,maths,physics,python=row
    total=maths+physics+python
    st[rollno]={
        "name":name,
        "marks":[maths,physics,python],
        "total":total
    }
print('student_record')
for roll,details in st.items():
    print(f"rollno={roll},name={details['name']},marks={details['marks']},total={details['total']}")