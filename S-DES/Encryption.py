from key_generation import KeyGeneration
class Encryption:
    def __init__(self, pt, keys):
        self.pt = self.validateInputKey(pt)
        self.k1 = keys[0]
        self.k2 = keys[1]
        self.ipTable = (2,6,3,1,4,8,5,7)
        self.epTable = (4,1,2,3,2,3,4,1)
        self.s0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
        self.s1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
        self.p4Table = (2,4,3,1)
        self.ipi = (4,1,3,5,7,2,8,6)

    def validateInputKey(self, temp_pt):
        pt = []
        for i in temp_pt:
            i = str(i)
            if i == "0" or i == "1":
                pt.append(int(i))
            else:
                print("Invalid chars in Key!!")
                return
        return pt

    def getPlainText(self):
        return self.pt

    def initialPermutation(self, plainText):
        permuted = []
        for j in self.ipTable:
            permuted.append(plainText[j-1]) 
        return permuted

    def expansionPermutation(self, nibble):
        nibble_expanded = []
        for j in self.epTable:
            nibble_expanded.append(nibble[j-1])
        return nibble_expanded

    def getKeys(self):
        return (self.k1,self.k2)
    
    def xor(self, bin1, bin2):
        res = []
        for i in range(len(bin1)):
            res.append(bin1[i] ^ bin2[i])
        return res
    
    def resolveSBlocks(self, bin_left, bin_right):
        row = int(str(bin_left[0])+str(bin_left[3]),2)
        col = int(str(bin_left[1])+str(bin_left[2]),2)
        val1 = bin(self.s0[row][col]).replace("0b","")
        row = int(str(bin_right[0])+str(bin_right[3]),2)
        col = int(str(bin_right[1])+str(bin_right[2]),2)
        val2 = bin(self.s1[row][col]).replace("0b","")
        
        #to keep len equal to 2
        val1 = len(val1)>1 and val1 or "0"+val1
        val2 = len(val2)>1 and val2 or "0"+val2
        
        return [int(l) for l in val1 + val2]

    def permutationP4(self, bin):
        permuted = []
        for j in self.p4Table:
            permuted.append(bin[j-1]) 
        return permuted

    def initialPermutationInverse(self, partialCipher):
        permuted = []
        for j in self.ipi:
            permuted.append(partialCipher[j-1]) 
        return permuted

pt = "10010111"
start_key = "1010000010"
k = KeyGeneration(start_key)
e = Encryption(pt, k.generateKeys())
list_pt = e.getPlainText()

#1
ip = e.initialPermutation(list_pt)
initial_left_half = ip[:4]
initial_right_half = ip[4:]

for i in range(2):
    #2
    ep = e.expansionPermutation(initial_right_half)
    #3
    xor_res = e.xor(ep, e.getKeys()[i])
    #4
    left_half = xor_res[:4]
    right_half = xor_res[4:]
    s_combined = e.resolveSBlocks(left_half, right_half)
    #5
    p4 = e.permutationP4(s_combined)
    #6
    xor_after_p = e.xor(initial_left_half, p4)
    if i == 0:
        initial_left_half, initial_right_half = initial_right_half, xor_after_p
        
partial_cipher = xor_after_p + initial_right_half
print(e.initialPermutationInverse(partial_cipher))