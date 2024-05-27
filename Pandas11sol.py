#1280. Students and Examinations
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    studentDict = {}
    students = students.sort_values(['student_id'])
    for  i in range (len(students)):
        s_id = students['student_id'][i]
        s_name = students['student_name'][i]
        studentDict[s_id] = s_name
    examDict = {}
    for i in range (len(examinations)):
        s_id = examinations['student_id'][i]
        s_name = examinations['subject_name'][i]
        if(s_id, s_name) not in examDict:
            examDict[(s_id,s_name)] = 0
        examDict[(s_id, s_name)] += 1
    subs = []
    subjects.sort_values(by =['subject_name'])
    for i in range (len(subjects)):
        subs.append(subjects['subject_name'][i])
    result =[]
    for key,value in studentDict.items():
        for i in range (len(subs)):
            cnt = 0
            if(key, subs[i]) in examDict:
                cnt = examDict[(key, subs[i])]
            result.append([key, value, subs[i], cnt])
    return pd.DataFrame(result, columns = ['student_id', 'student_name','subject_name', 'attended_exams']).sort_values(by = ['student_id', 'subject_name'])



import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    # Get groupby object size
    exams = examinations.groupby(['student_id', 'subject_name']).size().reset_index()
    exams.columns = ['student_id', 'subject_name', 'attended_exams']
    all_comb = pd.merge(students, subjects, how='cross')
    df = all_comb.merge(exams, on=['student_id', 'subject_name'], how='left')
    df['attended_exams'] = df['attended_exams'].fillna(0).astype(int)
    lst = ['student_id', 'student_name', 'subject_name', 'attended_exams']
    return df[lst].sort_values(by=['student_id', 'subject_name'])

#1378. Replace Employee ID With The Unique Identifier
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employees, employee_uni, on = 'id', how = 'left')
    result = df[['unique_id','name']]
    return result

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    mydictionary = {}
    for i in range (len(employee_uni)):
        mydictionary[employee_uni['id'][i]] = employee_uni['unique_id'][i]
    result =[]
    for i in range(len(employees)):
        _id = employees['id'][i]
        name = employees['name'][i]
        uid = np.NaN
        if _id in mydictionary:
            uid = mydictionary[_id]
        result.append([uid, name])
    return pd.DataFrame(result, columns = ['unique_id','name'])
