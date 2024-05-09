    #Alumna Araujo González María Fernanda
                                                                         #PROGRAMMING LANGUAGE

class Undergraduate:
    def __init__ (self, academic_institution, academic_degree,  name, account_number, certifications, modality):
        self.academic_institution=academic_institution
        self.academic_degree=academic_degree
        self.name=name
        self.account_number=account_number
        self.certifications=certifications
        self.modality=modality

    def undergraduate_profile(self):
        return f"\nPERFIL UNIVERSITARIO\n\nInstitucion Academica: {self.academic_institution}\n\nGrado Academico: {self.academic_degree}\n\nNombre: {self.name}\n\nNumero de Cuenta: {self.account_number}\n\nCertificaciones: {self.certifications}\n\nModalidad: {self.modality}"

class Fisica(Undergraduate):
    def __init__ (self, academic_institution, academic_degree,  name, account_number, certifications, modality, experimental_laboratory):
        super().__init__(academic_institution, academic_degree,  name, account_number, certifications, modality)
        self.experimental_laboratory=experimental_laboratory

    def undergraduate_profile_physics(self):
        base_information_physics=super().undergraduate_profile()
        return f"{base_information_physics}\n\nCampo: {self.experimental_laboratory}"

class First_Semester_Fisica(Fisica):
    def __init__ (self, academic_institution, academic_degree,  name, account_number, certifications, modality, experimental_laboratory, calculo_diferencial, mecanica, metodos_experimentales, algebra_y_trigonometria, geometria_analitica):
        super().__init__(academic_institution, academic_degree,  name, account_number, certifications, modality, experimental_laboratory)
        self.calculo_diferencial=calculo_diferencial
        self.mecanica=mecanica
        self.metodos_experimentales=metodos_experimentales
        self.algebra_y_trigonometria=algebra_y_trigonometria
        self.geometria_analitica=geometria_analitica

    def undergraduate_profile_physics_first(self):
        base_information_physics_first=super().undergraduate_profile_physics()
        return f"{base_information_physics_first}\n\nCalificaciones\n Primer Semestre\n   Calculo Diferencial: {self.calculo_diferencial}\n   Mecanica: {self.mecanica}\n   Metodos Experimentales: {self.metodos_experimentales}\n   Algebra y Trigonometria: {self.algebra_y_trigonometria}\n   Geometria Analitica: {self.geometria_analitica}"

class Second_Semester_Fisica(First_Semester_Fisica):
    def __init__ (self, academic_institution, academic_degree,  name, account_number, certifications, modality, experimental_laboratory, calculo_diferencial, mecanica, metodos_experimentales, algebra_y_trigonometria, geometria_analitica, calculo_integral, fluidos_termodinámica_y_oscilaciones, laboratorio_de_mecanica, algebra_lineal, lenguajes_de_programacion):
        super().__init__(academic_institution, academic_degree,  name, account_number, certifications, modality, experimental_laboratory, calculo_diferencial, mecanica, metodos_experimentales, algebra_y_trigonometria, geometria_analitica)
        self.calculo_integral=calculo_integral
        self.fluidos_termodinámica_y_oscilaciones=fluidos_termodinámica_y_oscilaciones
        self.laboratorio_de_mecanica=laboratorio_de_mecanica
        self.algebra_lineal=algebra_lineal
        self.lenguajes_de_programacion=lenguajes_de_programacion

    def undergraduate_profile_physics_second(self):
        base_information_physics_second=super().undergraduate_profile_physics_first()
        return f"{base_information_physics_second}\n Segundo Semestre\n   Calculo Integral: {self.calculo_integral}\n   Fluidos, Termodinamica y Oscilaciones: {self.fluidos_termodinámica_y_oscilaciones}\n   Laboratorio de Mecanica: {self.laboratorio_de_mecanica}\n   Algebra Lineal: {self.algebra_lineal}\n   Lenguajes de Programacion: {self.lenguajes_de_programacion}"

class Third_Semester_Fisica(Second_Semester_Fisica):
    def __init__ (self, academic_institution, academic_degree,  name, account_number, certifications, modality, experimental_laboratory, calculo_diferencial, mecanica, metodos_experimentales, algebra_y_trigonometria, geometria_analitica, calculo_integral, fluidos_termodinámica_y_oscilaciones, laboratorio_de_mecanica, algebra_lineal, lenguajes_de_programacion, calculo_vectorial, electromagnetismo, laboratorio_de_electromagnetismo, ecuaciones_diferenciales_ordinarias, metodologia_de_la_investigacion):
        super().__init__(academic_institution, academic_degree,  name, account_number, certifications, modality, experimental_laboratory,  calculo_diferencial, mecanica, metodos_experimentales, algebra_y_trigonometria, geometria_analitica, calculo_integral, fluidos_termodinámica_y_oscilaciones, laboratorio_de_mecanica, algebra_lineal, lenguajes_de_programacion)
        self.calculo_vectorial=calculo_vectorial
        self.electromagnetismo=electromagnetismo
        self.laboratorio_de_electromagnetismo=laboratorio_de_electromagnetismo
        self.ecuaciones_diferenciales_ordinarias=ecuaciones_diferenciales_ordinarias
        self.metodologia_de_la_investigacion=metodologia_de_la_investigacion

    def undergraduate_profile_physics_third(self):
        base_information_physics_third=super().undergraduate_profile_physics_second()
        return f"{base_information_physics_third}\n Tercer Semestre\n   Calculo Vectorial: {self.calculo_vectorial}\n   Electromagnetismo: {self.electromagnetismo}\n   Laboratorio de Electromagnetismo: {self.laboratorio_de_electromagnetismo}\n   Ecuaciones Diferenciales Ordinarias: {self.ecuaciones_diferenciales_ordinarias}\n   Metodologia de la Investigacion: {self.metodologia_de_la_investigacion}"


class Matematicas(Undergraduate):
    def __init__ (self, academic_institution, academic_degree,  name, account_number, certifications, modality, analytical_laboratory):
        super().__init__(academic_institution, academic_degree,  name, account_number, certifications, modality)
        self.analytical_laboratory=analytical_laboratory

    def undergraduate_profile_mathematics(self):
        base_information_mathematics=super().undergraduate_profile()
        return f"{base_information_mathematics}\n\nCampo: {self.analytical_laboratory}"        

class First_Semester_Matematicas(Matematicas):
    def __init__ (self, academic_institution, academic_degree,  name, account_number, certifications, modality, analytical_laboratory, calculo_diferencial, taller_de_calculo_diferencial, introduccion_al_algebra, geometria_euclidiana, geometria_analitica):
        super().__init__(academic_institution, academic_degree,  name, account_number, certifications, modality, analytical_laboratory)
        self.calculo_diferencial=calculo_diferencial
        self.taller_de_calculo_diferencial=taller_de_calculo_diferencial
        self.introduccion_al_algebra=introduccion_al_algebra
        self.geometria_euclidiana=geometria_euclidiana
        self.geometria_analitica=geometria_analitica

    def undergraduate_profile_mathematics_first(self):
        base_information_mathematics_first=super().undergraduate_profile_mathematics()
        return f"{base_information_mathematics_first}\n\nCalificaciones\n Primer Semestre\n   Calculo Diferencial: {self.calculo_diferencial}\n   Taller de Calculo Diferencial: {self.taller_de_calculo_diferencial}\n   Introduccion al Algebra: {self.introduccion_al_algebra}\n   Geometria Euclidiana: {self.geometria_euclidiana}\n   Geometria Analitica: {self.geometria_analitica}"

class Second_Semester_Matematicas(First_Semester_Matematicas):
    def __init__ (self, academic_institution, academic_degree,  name, account_number, certifications, modality, analytical_laboratory, calculo_diferencial, taller_de_calculo_diferencial, introduccion_al_algebra, geometria_euclidiana, geometria_analitica, calculo_integral, taller_de_calculo_integral, algebra_superior, geometria_vectorial,  matematicas_discretas):
        super().__init__(academic_institution, academic_degree,  name, account_number, certifications, modality, analytical_laboratory, calculo_diferencial, taller_de_calculo_diferencial, introduccion_al_algebra, geometria_euclidiana, geometria_analitica)
        self.calculo_integral=calculo_integral
        self.taller_de_calculo_integral=taller_de_calculo_integral
        self.algebra_superior=algebra_superior
        self.geometria_vectorial=geometria_vectorial
        self.matematicas_discretas=matematicas_discretas

    def undergraduate_profile_mathematics_second(self):
        base_information_mathematics_second=super().undergraduate_profile_mathematics_first()
        return f"{base_information_mathematics_second}\n Segundo Semestre\n   Calculo Integral: {self.calculo_integral}\n   Taller de Calculo Integral: {self.taller_de_calculo_integral}\n   Algebra Superior: {self.algebra_superior}\n   Geometria Vectorial: {self.geometria_vectorial}\n   Matematicas discretas: {self.matematicas_discretas}"
    

class Third_Semester_Matematicas(Second_Semester_Matematicas):
    def __init__ (self, academic_institution, academic_degree,  name, account_number, certifications, modality, analytical_laboratory, calculo_diferencial, taller_de_calculo_diferencial, introduccion_al_algebra, geometria_euclidiana, geometria_analitica, calculo_integral, taller_de_calculo_integral, algebra_superior, geometria_vectorial,  matematicas_discretas, algebra_lineal, ecuaciones_diferenciales, calculo_diferencial_vectorial, computacion,  didactica_de_las_matematicas):
        super().__init__(academic_institution, academic_degree,  name, account_number, certifications, modality, analytical_laboratory, calculo_diferencial, taller_de_calculo_diferencial, introduccion_al_algebra, geometria_euclidiana, geometria_analitica, calculo_integral, taller_de_calculo_integral, algebra_superior, geometria_vectorial,  matematicas_discretas)
        self.algebra_lineal=algebra_lineal
        self.ecuaciones_diferenciales=ecuaciones_diferenciales
        self.calculo_diferencial_vectorial=calculo_diferencial_vectorial
        self.computacion=computacion
        self.didactica_de_las_matematicas=didactica_de_las_matematicas

    def undergraduate_profile_mathematics_third(self):
        base_information_mathematics_third=super().undergraduate_profile_mathematics_second()
        return f"{base_information_mathematics_third}\n Tercer Semestre\n   Algebra Lineal: {self.algebra_lineal}\n   Ecuaciones Diferenciales: {self.ecuaciones_diferenciales}\n   Calculo Diferencial Vectorial: {self.calculo_diferencial_vectorial}\n   Computacion: {self.computacion}\n   Didactica de las Matematicas: {self.didactica_de_las_matematicas}"


class Electronica(Undergraduate):
    def __init__ (self, academic_institution, academic_degree,  name, account_number, certifications, modality, electronic_laboratory):
        super().__init__(academic_institution, academic_degree,  name, account_number, certifications, modality)
        self.electronic_laboratory=electronic_laboratory

    def undergraduate_profile_electronic(self):
        base_information_electronic=super().undergraduate_profile()
        return f"{base_information_electronic}\n\nCampo: {self.electronic_laboratory}"       

class First_Semester_Electronica(Electronica):
    def __init__ (self, academic_institution, academic_degree,  name, account_number, certifications, modality, electronic_laboratory, calculo_diferencial, fisica_mecanica, diseño_asistido_por_computadora, mediciones_electricas, fundamentos_de_programacion, introduccion_a_la_electronica):
        super().__init__(academic_institution, academic_degree,  name, account_number, certifications, modality, electronic_laboratory)
        self.calculo_diferencial=calculo_diferencial
        self.fisica_mecanica=fisica_mecanica
        self.diseño_asistido_por_computadora=diseño_asistido_por_computadora
        self.mediciones_electricas=mediciones_electricas
        self.fundamentos_de_programacion=fundamentos_de_programacion
        self.introduccion_a_la_electronica=introduccion_a_la_electronica

    def undergraduate_profile_electronic_first(self):
        base_information_electronic_first=super().undergraduate_profile_electronic()
        return f"{base_information_electronic_first}\n\nCalificaciones\n Primer Semestre\n   Calculo Diferencial: {self.calculo_diferencial}\n   Fisica Mecanica: {self.fisica_mecanica}\n   Diseño Asistido por Computadora: {self.diseño_asistido_por_computadora}\n   Fundamentos de Programacion: {self.fundamentos_de_programacion}\n   Introduccion a la Electronica: {self.introduccion_a_la_electronica}"

class Second_Semester_Electronica(First_Semester_Electronica):
    def __init__ (self, academic_institution, academic_degree,  name, account_number, certifications, modality, electronic_laboratory, calculo_diferencial, fisica_mecanica, diseño_asistido_por_computadora, mediciones_electricas, fundamentos_de_programacion, introduccion_a_la_electronica, calculo_integral, algebra_lineal, probabilidad_y_estadistica, electricidad_y_magnetismo, lenguaje_de_programacion, metodologia_de_la_investigacion):
        super().__init__(academic_institution, academic_degree,  name, account_number, certifications, modality, electronic_laboratory, calculo_diferencial, fisica_mecanica, diseño_asistido_por_computadora, mediciones_electricas, fundamentos_de_programacion, introduccion_a_la_electronica)
        self.calculo_integral=calculo_integral
        self.algebra_lineal=algebra_lineal
        self.probabilidad_y_estadistica=probabilidad_y_estadistica
        self.electricidad_y_magnetismo=electricidad_y_magnetismo
        self.lenguaje_de_programacion=lenguaje_de_programacion
        self.metodologia_de_la_investigacion=metodologia_de_la_investigacion

    def undergraduate_profile_electronic_second(self):
        base_information_electronic_second=super().undergraduate_profile_electronic_first()
        return f"{base_information_electronic_second}\n Segundo Semestre\n   Calculo Integral: {self.calculo_integral}\n   Algebra Lineal: {self.algebra_lineal}\n   Probabilidad y Estadistica: {self.probabilidad_y_estadistica}\n   Electricidad y Magnetismo: {self.electricidad_y_magnetismo}\n   Lenguaje de Programacion: {self.lenguaje_de_programacion}\n   Metodologia de la investigacion: {self.metodologia_de_la_investigacion}"

class Third_Semester_Electronica(Second_Semester_Electronica):
    def __init__ (self, academic_institution, academic_degree,  name, account_number, certifications, modality, electronic_laboratory, calculo_diferencial, fisica_mecanica, diseño_asistido_por_computadora, mediciones_electricas, fundamentos_de_programacion, introduccion_a_la_electronica, calculo_integral, algebra_lineal, probabilidad_y_estadistica, electricidad_y_magnetismo, lenguaje_de_programacion, metodologia_de_la_investigacion, ecuaciones_diferenciales, analisis_vectorial, ciencias_de_datos, dispositivos_semiconductores, programacion_orientada_a_objetos, analisis_de_circuitos_en_corrientes_directas):
        super().__init__(academic_institution, academic_degree,  name, account_number, certifications, modality, electronic_laboratory, calculo_diferencial, fisica_mecanica, diseño_asistido_por_computadora, mediciones_electricas, fundamentos_de_programacion, introduccion_a_la_electronica, calculo_integral, algebra_lineal, probabilidad_y_estadistica, electricidad_y_magnetismo, lenguaje_de_programacion, metodologia_de_la_investigacion)
        self.ecuaciones_diferenciales=ecuaciones_diferenciales
        self.analisis_vectorial=analisis_vectorial
        self.ciencias_de_datos=ciencias_de_datos
        self.dispositivos_semiconductores=dispositivos_semiconductores
        self.programacion_orientada_a_objetos=programacion_orientada_a_objetos
        self.analisis_de_circuitos_en_corrientes_directas=analisis_de_circuitos_en_corrientes_directas

    def undergraduate_profile_electronic_third(self):
        base_information_electronic_third=super().undergraduate_profile_electronic_second()
        return f"{base_information_electronic_third}\n Tercer Semestre\n   Ecuaciones Diferenciales: {self.ecuaciones_diferenciales}\n   Analisis Vectorial: {self.analisis_vectorial}\n   Ciencias de Datos: {self.ciencias_de_datos}\n   Dispositivos Semiconductores: {self.dispositivos_semiconductores}\n   Programacion Orientada a Objetos: {self.programacion_orientada_a_objetos}\n   Analisis de Circuitos en Corrientes Directas: {self.analisis_de_circuitos_en_corrientes_directas}"


#Exemplifications

Undergrad_1=First_Semester_Fisica('Facultad de Ciencias Fisico-Matematicas | Universidad Autonoma de Sinaloa', 'Licenciatura', 'Crow Sosa Jesus Adan', '20405197', 'Segunda Lengua, Profesionalizantes', 'Presencial', 'Fisica', 10.0, 10.0, 10.0, 10.0, 9.0)
print(Undergrad_1.undergraduate_profile_physics_first())

Undergrad_2=Second_Semester_Fisica('Facultad de Ciencias Fisico-Matematicas | Universidad Autonoma de Sinaloa', 'Licenciatura', 'Lopez Avendaño Cesar', '20523479', 'Segunda Lengua', 'Presencial', 'Fisica', 10.0, 10.0, 10.0, 8.0, 10.0, 9.0, 10.0, 10.0, 10.0, 10.0)
print(Undergrad_2.undergraduate_profile_physics_second())

Undergrad_3=Third_Semester_Fisica('Facultad de Ciencias Fisico-Matematicas | Universidad Autonoma de Sinaloa', 'Licenciatura', 'Muro Arellano Derek Guadalupe', '20199205', 'Segunda Lengua', 'Presencial', 'Fisica', 9.0, 9.0, 8.0, 7.0, 8.0, 10.0, 9.0, 5.0, 7.0, 8.0, 3.0, 8.0, 9.0, 10.0, 9.0)
print(Undergrad_3.undergraduate_profile_physics_third())

Undergrad_4=First_Semester_Matematicas('Facultad de Ciencias Fisico-Matematicas | Universidad Autonoma de Sinaloa', 'Licenciatura', 'Guerrero Vega Cesar Alid', '20712332', 'Segunda Lengua, Tecnologias de la Informacion', 'Presencial', 'Matematicas', 10.0, 10.0, 10.0, 10.0, 9.0)
print(Undergrad_4.undergraduate_profile_mathematics_first())

Undergrad_5=Second_Semester_Matematicas('Facultad de Ciencias Fisico-Matematicas | Universidad Autonoma de Sinaloa', 'Licenciatura', 'Zavala Gonzalez Ana Magali', '20712332', 'Segunda Lengua, Tecnologias de la Informacion', 'Presencial', 'Matematicas', 2.0, 6.0, 7.0, 9.0, 9.0, 5.0, 7.0, 8.0, 3.0, 8.0)
print(Undergrad_5.undergraduate_profile_mathematics_second())     

Undergrad_6=Third_Semester_Matematicas('Facultad de Ciencias Fisico-Matematicas | Universidad Autonoma de Sinaloa', 'Licenciatura', 'Valenzuela Vargas Andrea', '23214578', 'Tecnologias de la Informacion', 'Presencial', 'Matematicas', 9.0, 8.0, 6.0, 9.0, 9.0, 8.0, 7.0, 8.0, 7.0, 8.0, 9.0, 5.0, 7.0, 8.0, 3.0)
print(Undergrad_6.undergraduate_profile_mathematics_third()) 

Undergrad_7=First_Semester_Electronica('Facultad de Ciencias Fisico-Matematicas | Universidad Autonoma de Sinaloa', 'Licenciatura', 'Mizquiz Leal Luis Felipe', '21234813', 'Profesionalizantes', 'Presencial', 'Electronica', 4.0, 7.0, 8.0, 10.0, 9.0, 9.0)
print(Undergrad_7.undergraduate_profile_electronic_first())

Undergrad_8=Second_Semester_Electronica('Facultad de Ciencias Fisico-Matematicas | Universidad Autonoma de Sinaloa', 'Licenciatura', 'Rendon Olvera Sol Angel', '22456783', 'Segunda Lengua', 'Presencial', 'Electronica', 10.0, 10.0, 10.0, 8.0, 10.0, 9.0, 10.0, 10.0, 10.0, 10.0, 9.0, 8.0)
print(Undergrad_8.undergraduate_profile_electronic_second())

Undergrad_9=Third_Semester_Electronica('Facultad de Ciencias Fisico-Matematicas | Universidad Autonoma de Sinaloa', 'Licenciatura', 'Rivera Cazares Jonathan Magadiel', '21234213', 'Tecnologias de la Informacion', 'Presencial', 'Electronica', 9.0, 9.0, 8.0, 7.0, 8.0, 10.0, 9.0, 5.0, 7.0, 8.0, 3.0, 8.0, 9.0, 10.0, 9.0, 7.0, 8.0, 3.0)
print(Undergrad_9.undergraduate_profile_electronic_third())

Undergrad_10=First_Semester_Fisica('Facultad de Ciencias Fisico-Matematicas | Universidad Autonoma de Sinaloa', 'Licenciatura', 'Vazquez Valdez Jose Carlos', '23456789', 'Segunda Lengua, Profesionalizantes, Tecnologias de la Informacion', 'Presencial', 'Fisica', 10.0, 10.0, 10.0, 10.0, 10.0)
print(Undergrad_10.undergraduate_profile_physics_first())