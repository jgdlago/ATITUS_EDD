binString = 'null'

while True:
    numDec = int (input('Digite o decimal para conversão: '))

    if numDec != int:
        break

    def dec2bin(numDec):
        remstack = Stack()

        while numDec > 0:
            rem = numDec % 2
            remstack.push(rem)
            decNumber = numDec // 2

        binString = ""
        while not remstack.isEmpty():
            binString = binString + str(remstack.pop())

        return binString

    def push(self, binString): # Empilha
        if not self.is_empty():
            self._vet.append(binString)

push(binString)

dec2bin(numDec)

