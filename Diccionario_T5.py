    #Alumna Araujo González María Fernanda
                                             #PROGRAMMING LANGUAGE


#Exercise 1. Multiplying the elements of a dictionary
print("Exercise 1")

MBuber_Legacy=[]
Buber_Legacy={
    "I and Thou":1923,
    "Good and Evil":1953,
    "Paths in Utopia":1958,
    "The Origin And Meaning Of Hasidism":1960,
    "Die fünf Bücher der Weisung":1976,
    "Det mellanmänskliga":1938,
    "Il cammino dell'uomo":1931          
}


def Dictionary_values(Dictionary, list):
    if isinstance(Dictionary, dict):
        for dict_aux in Dictionary:
            list.append(Dictionary[dict_aux])
    return list

def Multiplication_product(values):
    if isinstance(values, list):
        Product=1
        for Factor in values:
            Product*=Factor
        return Product
    else:
        raise ValueError ("The recorded argument is not proper to a multiplication factor.")

Result=Multiplication_product(Dictionary_values(Buber_Legacy, MBuber_Legacy))
print("The product of the years of publication of the literary epitome of Martin Buber is {}.".format(Result))


#Exercise 2. Delete the key from a dictionary
print("Exercise 2")

def Remove_Key(key_prospecting):
    Buber_Legacy.pop(key_prospecting)
    print("Dictionary updated in concept of key deletion {}: {}.".format(key_prospecting, Buber_Legacy))

Remove_Key("I and Thou")


def Remove_Key(key_prospecting):
    del Buber_Legacy[key_prospecting]
    print("Dictionary updated in concept of key deletion {}: {}.".format(key_prospecting, Buber_Legacy))

Remove_Key("Good and Evil")


#Exercise 3. Convertir dos listas en un diccionario
print("Exercise 3")

from collections import defaultdict
Literary_Epitome=["I and Thou", "Good and Evil", "Paths in Utopia", "The Origin And Meaning Of Hasidism", "Die fünf Bücher der Weisung", "Det mellanmänskliga", "Il cammino dell'uomo"]
Year_Publication=[1923, 1953, 1958, 1960, 1976, 1938, 1931]

def Create_Dictionary(list_key, list_value):
    Dictionary=defaultdict(set)
    for key, value in zip(list_key, list_value):
        Dictionary[key]=value
    print("Dictionary formulated in duo of list concept: {}".format(Dictionary))
    return Dictionary

Create_Dictionary(Literary_Epitome, Year_Publication)


def Create_Dictionary(list_key, list_value):
    Dictionary=dict(zip(list_key, list_value))
    print("Dictionary formulated in list duo concept: {}".format(Dictionary))
    return Dictionary

Create_Dictionary(Literary_Epitome, Year_Publication)


    #Intuitive Method
def Create_Dictionary(list_key, list_value):
    Dictionary=dict()
    for key_aux in range(len(list_key)):
        for value_aux in range(len(list_value)):
            if key_aux==value_aux:
                Dictionary[list_key[key_aux]]=list_value[value_aux]
    print("Dictionary formulated in list duo concept: {}".format(Dictionary))
    return Dictionary

Martin_Legacy=Create_Dictionary(Literary_Epitome, Year_Publication)


#Exercise 4. Sort a dictionary by key
print("Exercise 4")

def Sort_Key(Dictionary):
    while True:
        try:
            Key_Criteria=str(input("Select the order criterion in key concept (Alphabetic/Reverse alphabetic): "))
        except Key_Criteria!="Alphabetic" or Key_Criteria!="Reverse alphabetic":
            print("Invalid entry. Register one of your own criteria to be selected.")
            continue
        else:
            break
    if Key_Criteria=="Alphabetic":
        Alphabetical_Register=dict(sorted(Dictionary.items()))
        print ("Dictionary sorted in alphabetical order: {}".format(Alphabetical_Register))
    elif Key_Criteria=="Reverse alphabetic":
        InverseAlphabetical_Register=dict(sorted(Dictionary.items(), reverse=True))
        print ("Dictionary sorted in reverse alphabetical order: {}".format(InverseAlphabetical_Register))

Sort_Key(Martin_Legacy)


#Exercise 5. Maximum and minimum value in a dictionary
print("Exercise 5")

    #Value
def MaxiandMin_Value(Dictionary):
    Duo_Maximum=max(zip(Dictionary.values(), Dictionary.keys()))
    Duo_Minimum=min(zip(Dictionary.values(), Dictionary.keys()))
    Value_Limit=[Duo_Maximum, Duo_Minimum]
    print ("The limit of values that delimits the dictionary {} is: {}.".format(Dictionary, Value_Limit))
    return Value_Limit

MaxiandMin_Value(Martin_Legacy)



def MaxiandMin_Value(Dictionary):
    Maximum_Key=max(Dictionary.keys(), key=lambda k: Dictionary[k])
    Maximum_Value=Dictionary[Maximum_Key]
    Minimum_Key=min(Dictionary.keys(), key=lambda k: Dictionary[k])
    Minimum_Value=Dictionary[Minimum_Key]
    Value_Limit=[{Maximum_Key:Maximum_Value, Minimum_Key:Minimum_Value}]
    print ("The limit of values that delimits the dictionary {} is: {}.".format(Dictionary, Value_Limit))
    return Value_Limit

MaxiandMin_Value(Martin_Legacy)

    #Key
def MaxiandMin_Value(Dictionary):
    Duo_Maximum=max(zip(Dictionary.keys(), Dictionary.values()))
    Duo_Minimum=min(zip(Dictionary.keys(), Dictionary.values()))
    Key_Limit=[Duo_Maximum, Duo_Minimum]
    print ("The limit of keys that delimits the dictionary {} is: {}.".format(Dictionary, Key_Limit))
    return Key_Limit

MaxiandMin_Value(Martin_Legacy)


#Exercise 6. Generate dictionary based on object fields
print("Exercise 6")

class PhotographicCamera:
	def __init__(self):
		self.Image_Sensor="CMOS"
		self.Resolution_MP=120
		self.Sensitivity_Range="ISO"
		self.Lens_Type="Telephoto"
		self.File_Formats="RAW"
		self.Shooting_Mode="Timer"
		self.Connectivity="NFC"
		self.Sensor_Type="APSC"
    
Photographic_Camera=PhotographicCamera()

def Dictionary_ObjectsFields(Object):
    return{
        "Image_Sensor":Object.Image_Sensor,
        "Resolution":Object.Resolution_MP,
		"Sensitivity_Range":Object.Sensitivity_Range,
		"Lens_Type":Object.Lens_Type,
		"File_Formats":Object.File_Formats,
		"Shooting mode":Object.Shooting_Mode,
		"Connectivity":Object.Connectivity,
        "Sensor_Type":Object.Sensor_Type
    }

PC_Dictionary=Dictionary_ObjectsFields(Photographic_Camera)
print("Dictionary formulated in concept of object fields: {}".format(PC_Dictionary))


#Exercise 7. Remove duplicate dictionary
print("Exercise 7")

Pantone_Adventure={
    "Shade_1":{
        "Name":"Peach Fuzz",
        "Code":131023,
        "Category":"TCX"
    },
    "Shade_2":{
        "Name":"Bright Violet",
        "Code":193438,
        "Category":"TCN"
    },
    "Shade_3":{
        "Name":"Cactus Flower",
        "Code":182326,
        "Category":"TCP"
    },
    "Shade_4":{
        "Name":"Swedish Blue",
        "Code":184330,
        "Category":"TCM"
    },
    "Shade_5":{
        "Name":"Seafoam Green",
        "Code":121330,
        "Category":"TCJ"
    },
    "Shade_6":{
        "Name":"Swedish Blue",
        "Code":184330,
        "Category":"TCM"
    }
}

def Remove_Duplicate(Dictionary_Duplicated):
    Dictionary_Remove={}
    for key, value in Dictionary_Duplicated.items():
        if value not in Dictionary_Remove.values():
            Dictionary_Remove[key]=value
            Duplicate_Elements=len(Dictionary_Duplicated)-len(Dictionary_Remove)
    print("Dictionary formulated from the removal of {} duplicate elements present in the dictionary {}: ".format(Duplicate_Elements, Dictionary_Remove))
    return Dictionary_Remove

Remove_Duplicate(Pantone_Adventure)


#Exercise 8. Verify if a dictionary is empty
print("Exercise 8")

Principia={}
    #"else" corresponds to the operator "elif Empty_Criteria==False""

def Verify_Empty(Dictionary):
    Empty_Criteria=(len(Dictionary)==0)
    if Empty_Criteria==True:
        print("The dictionary is empty in terms of content.")
    else:
        print("The dictionary is not empty; it contains {} elements.".format(len(Dictionary)))

Verify_Empty(Principia)
Verify_Empty(Pantone_Adventure)


def Verify_Empty(Dictionary):
    Empty_Criteria=(not bool(Dictionary))
    if Empty_Criteria==True:
        print("The dictionary is empty in terms of content.")
    else:
        print("The dictionary is not empty; it contains {} elements.".format(len(Dictionary)))

Verify_Empty(Principia)
Verify_Empty(Pantone_Adventure)


def Verify_Empty(Dictionary):
    Empty_Criteria=(not Dictionary)
    if Empty_Criteria==True:
        print("The dictionary is empty in terms of content.")
    else:
        print("The dictionary is not empty; it contains {} elements.".format(len(Dictionary)))

Verify_Empty(Principia)
Verify_Empty(Pantone_Adventure)


#Exercise 9. Extract list of values from a list of dictionaries
print("Exercise 9")

Qualifications=[{"Mathematics":90, "Science":92}, {"Mathematics":89, "Science":94}, {"Mathematics":92, "Science":88}]

def Parameter_ListDictionary(List):
    Subject=[]
    while True:
        try:
            Parameter=str(input("Select the order criterion in parameter concept (Mathematics/Science): "))
        except Parameter!="Alphabetic" or Parameter!="Reverse alphabetic":
            print("Invalid entry. Register one of your own parameter to be selected.")
            continue
        else:
            break
    for dict_aux in List:
        if Parameter in dict_aux:
            Subject.append(dict_aux[Parameter])
    print(Parameter, Subject)
    return Subject

Parameter_ListDictionary(Qualifications)


#Exercise 10. Extract a list of parameter-referenced values from a list of dictionaries
print("Exercise 10")

def Science_ListDictionary(List):
    Subject=[]

    for dict_aux in List:
        if "Science" in dict_aux:
            Subject.append(dict_aux["Science"])
    print("Science", Subject)
    return Subject

Science_ListDictionary(Qualifications)


#Exercise 11. Extract a list of parameter-referenced values from a list of dictionaries
print("Exercise 11")

def Mathematics_ListDictionary(List):
    Subject=[]

    for dict_aux in List:
        if "Mathematics" in dict_aux:
            Subject.append(dict_aux["Mathematics"])
    print("Mathematics", Subject)
    return Subject

Mathematics_ListDictionary(Qualifications)


#Exercise 12. Finding the length of a dictionary of values
print("Exercise 12")

def Length_Dictionary(Dictionary):
    Length=len(Dictionary)
    print("The length of the dictionary {} is: {}".format(Dictionary, Length))
    return Length

Length_Dictionary(Buber_Legacy)


#Exercise 13. Determine the depth of a dictionary
print("Exercise 13")

def Depth_Dictionary(Dictionary):
    if isinstance(Dictionary, dict):
        Depth=1+(max(map(Depth_Dictionary, Dictionary.values())) if Dictionary else 0)
        print("The depth of the dictionary {} is: {}".format(Dictionary, Depth))
        return Depth
    else:
        return 0

Depth_Dictionary(Pantone_Adventure)


#Exercise 14. Accessing the key element of a value by index
print("Exercise 14")

Kardex={
    "Physics":98,
    "Mathematics":95,
    "Biology":86,
    "Sociology":100,
    "Politics":92,
    "Philosophy":100,
    "Quimica":98
}

Index_List=[0, 1, 6]

def AccessingKey_Index(Dictionary, Index_list):
    Dictionary_List=list(Dictionary)
    Accessing_List=[]
    for index_aux in range(len(Index_list)):
        Index=Index_List[index_aux]
        Accessing_List.append(Dictionary_List[Index])
    print(Accessing_List)
    return Accessing_List

AccessingKey_Index(Kardex, Index_List)


#Exercise 15. Convert a dictionary into a list of lists
print("Exercise 15")

Colors_Dictionary={1: "Red", 2:"Green", 3:"Black", 4:"White", 5:"Black"}

def Dictionary_ListLists(Dictionary):
    ListOfList=[]
    for key, value in Dictionary.items():
        List=[key, value]
        ListOfList.append(List)
    print("Dictionary formulated in list of lists concept: {}".format(ListOfList))
    return ListOfList

Dictionary_ListLists(Colors_Dictionary)


#Exercise 16. Filtering even numbers from a dictionary of numeric values
print("Exercise 16")
Numeric_Values_1={"V":[1, 4, 6, 10], "VI":[1, 4, 12], "VII":[1, 3, 8]}
Numeric_Values_2={"V":[1, 3, 5], "VI":[1, 5], "VII":[2, 7, 9]}

def Filter_EvenValue(Dictionary):
    Filter_Dictionary={}
    for key, list in Dictionary.items():
        Even_Number=[]
        for value_aux in range(len(list)-1,-1,-1):
            value=list[value_aux]
            if value%2==0:
                Even_Number.append(value)
                Filter_Dictionary[key]=Even_Number[::-1]
    print("Reformulated dictionary in even-valued filtering concept: {}".format(Filter_Dictionary))
    return(Filter_Dictionary)

Filter_EvenValue(Numeric_Values_1)
Filter_EvenValue(Numeric_Values_2)