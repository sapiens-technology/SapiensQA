class SapiensQA:
    def __init__(self, temperature=.01):
        from core import SapiensQA
        self.__sapiens_qa = SapiensQA(temperature=temperature)
    def fit(self, path='', show_progress=True): self.__sapiens_qa.fit(path=path, show_progress=show_progress)
    def fineTuning(self, question='', answer=''): self.__sapiens_qa.fineTuning(question=question, answer=answer)
    def saveModel(self, path=''): self.__sapiens_qa.saveModel(path=path)
    def loadModel(self, path=''): self.__sapiens_qa.loadModel(path=path)
    def transferLearning(self, transmitter_path='', receiver_path='', rescue_path=''): self.__sapiens_qa.transferLearning(transmitter_path=transmitter_path, receiver_path=receiver_path, rescue_path=rescue_path)
    def predict(self, question=''): return self.__sapiens_qa.predict(question=question)
    def printPrediction(self, question='', wait=1): self.__sapiens_qa.printPrediction(question=question, wait=wait)
