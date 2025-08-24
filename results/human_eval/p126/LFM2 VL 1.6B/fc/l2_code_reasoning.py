def filterList(inputList):
    outputList = []
    for i in range(len(inputList) - 1):
        if inputList[i] <= inputList[i + 1]:
            outputList.append(inputList[i])
    return outputList