from bitvector import BitVector

def init_test() -> BitVector:
    vector = BitVector(32)
    assert vector.vector_value() == 32
    assert vector.get_length() == 6
    return vector

def length_test(vector : BitVector):
    vector.set_length(10)
    assert vector.get_length() == 10
    return vector

def set_test(vector : BitVector):
    vector.set(9,True)
    assert vector.bit_value(9) == True
    return vector

def flip_test(vector : BitVector):
    vector.flip(9)
    assert vector.bit_value(9) == False
    return vector

def invert_test(vector : BitVector):
    print(vector)
    vector.invert()
    print(vector)
    print(vector.vector_value())
    return vector


if __name__ == "__main__":
    vector = init_test()
    vector = length_test(vector)
    vector = set_test(vector)
    vector = flip_test(vector)
    vector = invert_test(vector)
    print("All test passed!")