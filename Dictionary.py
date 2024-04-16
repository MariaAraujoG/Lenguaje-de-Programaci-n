    #Alumna Araujo González María Fernanda

from operator import itemgetter
#from tabulate import tabulate

MathGrade_Dictionary={
    "Crow Sosa Jesús Adán":9.96,
    "Jimenez Garibaldy Nilda Ivonne":7.86,
    "Blancas Castillo Omar Alberto":8.47,
    "Solano Madinaveytia Hilda Sofía":8.32,
    "Valenzuela Medina Dulce Gabriela":8.98,
    "Herrera Ochoa Dara Dalay":7.42,
    "Navarrete Díaz Luis Alejandro":8.76,
    "Arredondo Reyes Ian Jahel":6.78,
    "Felix Zazueta Victoria":7.54,
    "Lazcano Duerte Miguel Anguel":6.68
}

    #ALPHABETICAL REGISTER
Alphabetical_Register=dict(sorted(MathGrade_Dictionary.items()))

print("ALPHABETICAL REGISTER")
for key,value in Alphabetical_Register.items():
    print("The student's grade", key, "in the subject Mathematics is", value)
#print(tabulate(Alphabetical_Register, headers=["Student's Name", "Grade"]))
    

    #UPWARD REGISTER
Upward_Register=dict(sorted(MathGrade_Dictionary.items(), key=itemgetter(1)))

print("UPWARD REGISTER")
for key,value in Upward_Register.items():
    print("The student's grade", key, "in the subject Mathematics is", value)
#print(tabulate(Upward_Register, headers=["Student's Name", "Grade"]))


    #DESCENDING REGISTER
Descending_Register=dict(sorted(MathGrade_Dictionary.items(), key=itemgetter(1), reverse=True))

print("DESCENDING REGISTER")
for key,value in Descending_Register.items():
    print("The student's grade", key, "in the subject Mathematics is", value)
#print(tabulate(Descending_Register, headers=["Student's Name", "Grade"]))