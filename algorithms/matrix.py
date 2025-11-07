class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows: int = rows
        self.cols: int = cols
        self.matrix = [ [''*cols] * rows ]
    

    def __str__(self):
        result: str = f"Matrix({self.rows} x {self.cols}):\n"
        for cols in self.rows:
            result += cols
        return result

    def sum(matrixA: "Matrix", matrixB: "Matrix"):
        pass

#     __add__ → para permitir a + b

# __eq__ → para comparar objetos (==)

# __len__, __getitem__, __iter__, etc.

# _atributo → protegido (convenção)

# __atributo → privado (name mangling)

# @staticmethod: não depende de self nem cls

# @classmethod: depende da classe, não da instância

# @classmethod
# def identidade(cls, n: int) -> "Matrix":
#     m = cls(n, n)
#     for i in range(n):
#         m.matrix[i][i] = 1
#     return m


# def determinant(self) -> float:
#     """Calcula o determinante da matriz (apenas 2x2 por enquanto)."""
#     if self.rows == 2 and self.cols == 2:
#         a, b = self.matrix[0]
#         c, d = self.matrix[1]
#         return a*d - b*c
    # raise NotImplementedError

# .__and__(self, value)	instance & value
# .__rand__(self, value)	value & instance
# .__iand__(self, value)	instance &= value
# .__or__(self, value)	instance | value
# .__ror__(self, value)	value | instance
# .__ior__(self, value)	instance |= value
# .__xor__(self, value)	instance ^ value
# .__rxor__(self, value)	value ^ instance
# .__ixor__(self, value)	instance ^= value
# .__invert__(self)	~instance
# .__lshift__(self, value)	instance << value
# .__rlshift__(self, value)	value << instance
# .__ilshift__(self, value)	instance <<= value
# .__rshift__(self, value)	instance >> value
# .__rrshift__(self, value)	value >> instance
# .__irshift__(self, value)	instance >>= value

# >>> from collections import deque

# >>> class DoubleEndedQueue(deque):
# ...     def __lshift__(self, value):
# ...         self.append(value)
# ...
# ...     def __rrshift__(self, value):
# ...         self.appendleft(value)
# ...
# >>> items = DoubleEndedQueue(["middle"])
# >>> items << "last"
# >>> "first" >> items
# >>> items
# DoubleEndedQueue(['first', 'middle', 'last'])

# Operator	Supporting Method
# +	.__add__(self, other)
# -	.__sub__(self, other)
# *	.__mul__(self, other)
# /	.__truediv__(self, other)
# //	.__floordiv__(self, other)
# %	.__mod__(self, other)
# **	.__pow__(self, other[, modulo])

# Operator	Right-Hand Method
# +	.__radd__(self, other)
# -	.__rsub__(self, other)
# *	.__rmul__(self, other)
# /	.__rtruediv__(self, other)
# //	.__rfloordiv__(self, other)
# %	.__rmod__(self, other)
# **	.__rpow__(self, other[, modulo])


# Operator	Supporting Method	Description
# -	.__neg__(self)	Returns the target value with the opposite sign
# +	.__pos__(self)	Provides a complement to the negation without performing any transformation

# Operator	Supporting Method
# <	.__lt__(self, other)
# <=	.__le__(self, other)
# ==	.__eq__(self, other)
# !=	.__ne__(self, other)
# >=	.__ge__(self, other)
# >	.__gt__(self, other)

#   def __contains__(self, item):
#         for current_item in self.items:
#             if item == current_item:
#                 return True
#         return False

# Operator	Supporting Method
# +=	.__iadd__(self, other)
# -=	.__isub__(self, other)
# *=	.__imul__(self, other)
# /=	.__itruediv__(self, other)
# //=	.__ifloordiv__(self, other)
# %=	.__imod__(self, other)
# **=	.__ipow__(self, other[, modulo])

# Operator	Supporting Method
# &=	.__iand__(self, other)
# |=	.__ior__(self, other)
# ^=	.__ixor__(self, other)
# <<=	.__ilshift__(self, other)
# >>=	.__irshift__(self, other)

# Method	Description
# .__dir__()	Returns a list of attributes and methods of an object
# .__hasattr__()	Checks whether an object has a specific attribute
# .__instancecheck__()	Checks whether an object is an instance of a certain class
# .__subclasscheck__()	Checks whether a class is a subclass of a certain class

# ethod	Description
# .__getattribute__(self, name)	Runs when you access an attribute called name
# .__getattr__(self, name)	Runs when you access an attribute that doesn’t exist in the current object
# .__setattr__(self, name, value)	Runs when you assign value to the attribute called name
# .__delattr__(self, name)	Runs when you delete the attribute called name


# Method	Description
# .__get__(self, instance, type=None)	Getter method that allows you to retrieve the current value of the managed attribute
# .__set__(self, instance, value)	Setter method that allows you to set a new value to the managed attribute
# .__delete__(self, instance)	Deleter method that allows you to remove the managed attribute from the containing class
# .__set_name__(self, owner, name)	Name setter method that allows you to define a name for the managed attribute

# Method	Description
# .__iter__()	Called to initialize the iterator. It must return an iterator object.
# .__next__()	Called to iterate over the iterator. It must return the next value in the data stream.


# Method	Description
# .__getitem__()	Called when you access an item using indexing like in sequence[index]
# .__len__()	Called when you invoke the built-in len() function to get the number of items in the underlying sequence
# .__contains__()	Called when you use the sequence in a membership test with the in or not in operator
# .__reversed__()	Called when you use the built-in reversed() function to get a reversed version of the underlying sequence

# Method	Description
# .__enter__()	Sets up the runtime context, acquires resources, and may return an object that you can bind to a variable with the as specifier on the with header
# .__exit__()	Cleans up the runtime context, releases resources, handles exceptions, and returns a Boolean value indicating whether to propagate any exceptions that may occur in the context

# Algoritmo de Strassen
# multiplicar matrix

if __name__ == "__main__":
    a: Matrix = Matrix(3, 3) 
