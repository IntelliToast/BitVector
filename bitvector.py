import math
    
class BitVectorError(Exception):
    pass

class BitVector():
    def __init__(self, vector : int = 0) -> None:
        if vector < 0:
            raise BitVectorError(f"Value {vector} is less than zero! BitVectors must be positive or zero!")
        self.vector = vector
        self.length = self.get_bit_len()

    def __str__(self):
        binary = format(self.vector,f"0{self.length}b")
        return "[ " +  " ".join([*binary]) + " ]"

    def get_bit_len(self) -> int:
        value = self.vector
        length = 0
        while(value):
            value >>= 1
            length+=1
        return length

    def get_length(self) -> int:
        return self.length
    
    def set_length(self, length : int):
        self.vector &= (2**length - 1)
        self.length = length
    
    def zero_out(self):
        inverted = ~self.vector
        self.vector &= inverted
    
    def vector_value(self) -> int:
        return self.vector
    
    def bit_value(self, index : int) -> bool:
        if index < self.length:
            return bool(self.vector & (1 << index))
        else:
            raise BitVectorError(f"Index {index} is out of bound for a vector of length {self.length}!")
    
    def set(self, index : int, value : bool):
        if index < self.length:
            if value:
                self.vector |= 1 << index
            else:
                self.vector &= ~(1 << index)
        else:
            raise BitVectorError(f"Index {index} is out of bound for a vector of length {self.length}!")
        
    def flip(self, index : int):
        if index < self.length:
            self.vector ^= 1 << index
        else:
            raise BitVectorError(f"Index {index} is out of bound for a vector of length {self.length}!")
        
    def invert(self):
        self.vector ^= (2**(self.length+1)-1)
        self.vector ^= 1 << self.length
        
    