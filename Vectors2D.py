    #Alumna Araujo González María Fernanda
                                             #PROGRAMMING LANGUAGE

import math

class Vector2D():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return (self.x * other.x + self.y * other.y)
    
    def multiply_by_scalar(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def vector_norm(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def dot_product(self, other):
        return (self.x * other.x + self.y * other.y)
    
    def angle_between_vectors(self, other):
        angle_radian=math.acos(self.dot_product(other)/(self.vector_norm() * other.vector_norm()))
        return math.degrees(angle_radian)
    
    def angle_vectors(self, other):
        angle=math.acos(self*other/(self.vector_norm() * other.vector_norm()))
        return math.degrees(angle)
    
    def leading_cosine(self):
        vector=Vector2D(self.x/self.vector_norm(), self.y/self.vector_norm())
        return(vector.x,  vector.y)
    
    def abscissa_leading_cosine(self):
        return self.x/self.vector_norm()

    def orderly_leading_cosine(self):
        return self.y/self.vector_norm()
    
    def leading_angle(self):
        vector=Vector2D(self.x/self.vector_norm(), self.y/self.vector_norm())
        return math.degrees(math.acos(vector.x)), math.degrees(math.acos(vector.y))
    
    def abscissa_leading_angle(self):
        return math.degrees(math.acos(self.x/self.vector_norm()))

    def orderly_leading_angle(self):
        return math.degrees(math.acos(self.y/self.vector_norm()))
    
    def unit_vector(self):
        return Vector2D(self.x/self.vector_norm(), self.y/self.vector_norm())
    
    def vector_component(self, other):
        return self.dot_product(other)/other.vector_norm()
    
    def vector_projection(self, other):
        return Vector2D(other.unit_vector().x * self.vector_component(other),  other.unit_vector().y * self.vector_component(other))

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


#Exemplifications

Vector_1=Vector2D(4, 8)
Vector_2=Vector2D(3, 13)

Vector_Abscissa=Vector2D(1, 0)
Vector_Orderly=Vector2D(0, 1)

Vector_Addition=Vector_1+Vector_2
print('\nVector Sum \n{}+{}={}'.format(Vector_1, Vector_2, Vector_Addition))

Vector_Subtraction=Vector_1-Vector_2
print('\nVector Subtraction \n{}-{}={}'.format(Vector_1, Vector_2, Vector_Subtraction))

Scalar_Multiplication=Vector_1.multiply_by_scalar(3)
print('\nScalar Multiplication\n3*{}={}'.format(Vector_1, Scalar_Multiplication))

Vector_Norm=Vector_1.vector_norm()
print('\nVector Norm\n∥{}∥={}'.format(Vector_1, Vector_Norm))

Dot_Product=Vector_1.dot_product(Vector_2)
print('\nDot Product\n{}•{}={}'.format(Vector_1, Vector_2, Dot_Product))

Angle_Between_Vectors=Vector_1.angle_between_vectors(Vector_2)
print('\nAngle between vectors\n∠({}, {})={}°'.format(Vector_1, Vector_2, Angle_Between_Vectors))

Angle_Vectors=Vector_1.angle_vectors(Vector_1)
print('\nAngle between vectors\n∠({}, {})={}°'.format(Vector_1, Vector_2, Angle_Between_Vectors))

Leading_Cosine=Vector_1.leading_cosine()
print('\nLeading Cosine\n(cos α, cos β)({})={}'.format(Vector_1, Leading_Cosine))

Abscissa_Leading_Cosine=Vector_1.abscissa_leading_cosine()
print('\nAbscissa Leading Cosine\ncos α({})={}'.format(Vector_1, Abscissa_Leading_Cosine))

Orderly_Leading_Cosine=Vector_1.orderly_leading_cosine()
print('\nOrderly Leading Cosine\ncos β({})={}'.format(Vector_1, Orderly_Leading_Cosine))

Leading_Angle=Vector_1.leading_angle()
print('\nLeading Angle\n(α, β)({})={}°'.format(Vector_1, Leading_Angle))

Abscissa_Leading_Angle=Vector_1.abscissa_leading_angle()
print('\nAbscissa leading Angle\nα({})={}°'.format(Vector_1, Abscissa_Leading_Angle))

Orderly_Leading_Angle=Vector_1.orderly_leading_angle()
print('\nOrderly Leading Angle\nβ({})={}°'.format(Vector_1, Orderly_Leading_Angle))

Unit_Vector=Vector_1.unit_vector()
print('\nUnit Vector\n{}^={}'.format(Vector_1, Unit_Vector))

Vector_Component=Vector_1.vector_component(Vector_2)
print('\nVector Component\nComp{}({})={}'.format(Vector_2, Vector_1, Vector_Component))

Reciprocal_Vector_Component=Vector_2.vector_component(Vector_1)
print('\nVector Component\nComp{}({})={}'.format(Vector_1, Vector_2, Reciprocal_Vector_Component))

Vector_Projection=Vector_1.vector_projection(Vector_2)
print('\nVector Projection\nProj{}({})={}'.format(Vector_2, Vector_1, Vector_Projection))

Reciprocal_Vector_Projection=Vector_2.vector_projection(Vector_1)
print('\nVector Projection\nProj{}({})={}'.format(Vector_1, Vector_2, Reciprocal_Vector_Projection))

VectorComponent_AbscissaAxis=Vector_1.vector_component(Vector_Abscissa)
print('\nVector Component with respect to the Abscissa Axis\nCompX({})={}'.format(Vector_1, VectorComponent_AbscissaAxis))

VectorComponent_OrderlyAxis=Vector_1.vector_component(Vector_Orderly)
print('\nVector Component with respect to the Orderly Axis\nCompY({})={}'.format(Vector_1, VectorComponent_OrderlyAxis))

VectorProjection_AbscissaAxis=Vector_1.vector_projection(Vector_Abscissa)
print('\nVector Projection with respect to the Abscissa Axis\nProjX({})={}'.format(Vector_1, VectorProjection_AbscissaAxis))

VectorProjection_OrderlyAxis=Vector_1.vector_projection(Vector_Orderly)
print('\nVector Projection with respect to the Orderly Axis\nProjY({})={}'.format(Vector_1, VectorProjection_OrderlyAxis))
