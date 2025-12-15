#academic infomation
students_Name={'ade jimoh,olu jimi ,ojo dorcas,roqeeb yusuf ,peniel ayinde'}
students_Course={'agricultuiral science'}
students_Cgpa=3.51,2.34,4.71,5.0,4.10
students_Active='true'
coursesRegistered={"AEF301","ANP301","AGY309","AGY303","AGY301","ANP309","CPT301","AQT301","ANP303"}
students_Age={23,18,22,19,17}
matric_Number="22/10ac441","22/10ac442","22/10ac443","22/10ac444","22/10ac445"
students_Grade={
    "22/10AC441":{
        AEF301:"B",
        ANP301:"C",
        AGY309:"D",
        AGY303:"F",
        AGY301:'C',
        ANP309:'C',
        CPT301:"C",
        AQT301:'A',
        ANP303:'E',
    
    },
    '22/10AC442':{
        AEF301:"B",
        ANP301:"C",
        AGY309:"D",
        AGY303:"F",
        AGY301:'C',
        ANP309:'C',
        CPT301:"C",
        AQT301:'A',
        ANP303:'E',
    },
    '22/10AC443':{
        AEF301:"B",
        ANP301:"C",
        AGY309:"D",
        AGY303:"F",
        AGY301:'C',
        ANP309:'C',
        CPT301:"C",
        AQT301:'A',
        ANP303:'E',
    },
    '22/10AC444':{
        AEF301:"B",
        ANP301:"C",
        AGY309:"D",
        AGY303:"F",
        AGY301:'C',
        ANP309:'C',
        CPT301:"C",
        AQT301:'A',
        ANP303:'E',
    },    
    "22/10AC445":{
        AEF301:"B",
        ANP301:"C",
        AGY309:"D",
        AGY303:"F",
        AGY301:'C',
        ANP309:'C',
        CPT301:"C",
        AQT301:'A',
        ANP303:'E',
    }    
}
#TASK2 GRADING FUNCTIONS
def students_Grade(score):
    if score>=70 and score <=100:
        grade="A"
    if score>=60:
        grade="B"
    if score>=50:
        grade="c"
    if score>=45:
        grade="D"
    if score>=40:
        grade="E"
    else:
        grade='F'

    match grade:
        case 'A':
            print("Excellent result")
        case 'B':
            print('very good result')
        case "C":
            print('fair result')
        case 'D':
            print('poor result')
        case "E":
            print('FAILED,Need to improved')

        return grade
#TYPES CONVERSION AND VALIDATION
try:
    age_Input= input ('enter your age:')
    cgpa_input= input ("enter your cgpa:")

    age= int( age_input)
    cgpa= float(cgpa_input)

    if age < 16 or age > 40: 
        print("invalid age.age must be between 16 and 40.")
    else cgpa < 0.0 or cgpa >5.0:
        print("invalid cgpa.cgpa must be between 0.0 and 5.0.")
    else:
        print("age cgpa are valid.")
    except valueError:
        print('invalid input,please enter numeric values only')


#set operation (STUDENT WHO PASS AGY301)
set_pass={
    matric for matric, data in students.items()
    if "AGY301" in DATA['grade']
    and data["grade"]["AGY301"] !="F"

}
#STUDENTS WITH CGPA ABOVE 4.0
set_merit={
    matric for matric, data in students.items()
    if data ["cgpa"] > 4.0
}

#set operations
passed_and_merit=set_pass & set_merit
all_distinct_students=set_pass|set_merit
passed_not_merit=set_pass-set_merit


print("passed AGY301 and have merit:")
print("all distinct students:",all_distinct_students)
print("passed AGY301 but not merit:",passed_not_merit)


#part4:interactive menu
def veiw_all_students():
    for matric, data in students.items():
    print(matric,"-",data["name"], "|cgpa:",data["cgpa"])


def add_new_student():
    matric= input ("enter matric number:")
    name= input ("enter name:")
    age= int (input("enter age:"))
    cgpa= float(input("enter cgpa:"))

    students[matric]={
        "name":name,
        "age":age,
        "cgpa":cgpa,
        "is_active":true,
        "courses":[],
        "grades":{},
    }
    print("student added successfully.")


    def check_graduation():
        matric=input("enter matric number:")
        if matric in students:
            if students[matric]["cgpa"] >= 2
                print('eligible for graduation')
            else:
                print("not eligible for graduation")
            else:
                print("student not found.")

def find_topper_perfomer():
        top_student=max (students.items(),key=lambda x:x[1]["cgpa"])
        print('topper performer:',top_student[1]["name"],"|cgpa:",top_student[1]["cgpa"])
        

#menu loop
while true:
    print """===department menu===
    1.view all student
    2.add new student
    3.check eligibility for graduation
    4.find top performer
    5.exit
    """

    choice= input("select an option(1-5):")
    match choice:
    case "1"
       view_all_students()
    case "2"
       add_new_students()
    case "3"
       check_graduation()
    case "4"
       find_top_performer()
    case "5"
       print("existing system...")
       break
    case_:
    print("invalid option.try again.")

    #sample out  {student academic performance system}
    #loading strudent records...
    #student profiles loaded sucessfully


===departmental menu===
1.view all students
2.add new student
3.check eligibility For graduation
4.find top performer
5.exit


select an option(1-5):1
"22/10ac441"-ade jimoh|cgpa:4.32
"22/10ac442"-olu jimi|cgpa:3.85
"22/10ac443"-ojo dorcas|cgpa:4.71
"22/10ac444"-roqeeb yusuff|cgpa:5.00
"22/10ac445"-peniel ayinde|cgpa:4.10


===department menu===
1.view all student
2.add new student
3.check eligibility For graduation
4.find top performer
5.exiting system


select an option(1-5):3
enter matric number: '22/10ac443'
Eligible For graduation

select an option(1-5):4
Top Performer:roqeeb yusuff|cgpa:5.00


select an option(1-5):5
 exiting system