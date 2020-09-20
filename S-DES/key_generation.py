class KeyGeneration:
    def __init__(self, inputKey):
        self.inputKey = self.validateInputKey(inputKey)
        self.p10Table = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
        self.p8Table = (6, 3, 7, 4, 8, 5, 10, 9)
                
    def returnInputKey(self):
        return self.inputKey

    def validateInputKey(self, temp_key):
        key = []
        for i in  temp_key:
            i = str(i)
            if i == "0" or i == "1":
                key.append(int(i))
            else:
                print("Invalid chars in Key!!")
                return
        return key
        
    def performLeftShift(self, bin):
        temp = bin[0]
        le = len(bin)
        for i in range(le-1):
            bin[i] = bin[(i+1)%le]
        bin[le-1] = temp
        return bin

    def permutationP10(self, bin):
        key = []
        for j in self.p10Table:
            key.append(bin[j-1]) 
        return key

    def permutationP8(self, bin):
        key = []
        for j in self.p8Table:
            key.append(bin[j-1]) 
        return key


    def generateKeys(self):
        self.inputKey = self.permutationP10(self.inputKey)
        left_half = self.performLeftShift(self.inputKey[:len(self.inputKey)//2])
        right_half = self.performLeftShift(self.inputKey[len(self.inputKey)//2:])
        
        k1 = self.permutationP8(left_half + right_half)

        left_half = self.performLeftShift(self.performLeftShift(left_half))
        right_half = self.performLeftShift(self.performLeftShift(right_half))
        print(left_half,right_half)
        k2 = self.permutationP8(left_half + right_half)

        return (k1,k2)

#k1 = KeyGeneration("1010000010")
#print(k1.generateKeys())