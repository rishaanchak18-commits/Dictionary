student_data={'id1':
              {'name':'Rishaan',
               'class':['VIII'],
               'subjects':['Maths', 'Science', 'English']
               },
                'id2':
                {'name':'Aarav',
                 'class':['VII'],
                 'subjects':['Maths', 'German', 'SST']
                },
                'id3':
                {'name':'Rishaan',
                 'class':['VIII'],
                 'subjects':['Science', 'Maths', 'English']
                },
                'id4':
                {'name':'Sophia',
                 'class':['VIII'],
                 'subjects':['French', 'German', 'Maths']
                }
}   
result={}
for key, value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)