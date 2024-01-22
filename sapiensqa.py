class SapiensQA:
    def __init__(self, temperature=.01):
        from .core import SapiensQA
        self.__sapiensqa = SapiensQA(temperature=temperature)
    def fit(self, path='', show_progress=True): self.__sapiensqa.fit(path=path, show_progress=show_progress)
    def fineTuning(self, question='', answer=''): self.__sapiensqa.fineTuning(question=question, answer=answer)
    def saveModel(self, path=''): self.__sapiensqa.saveModel(path=path)
    def loadModel(self, path=''): self.__sapiensqa.loadModel(path=path)
    def transferLearning(self, transmitter_path='', receiver_path='', rescue_path=''): self.__sapiensqa.transferLearning(transmitter_path=transmitter_path, receiver_path=receiver_path, rescue_path=rescue_path)
    def predict(self, question=''): return self.__sapiensqa.predict(question=question)
    def printPrediction(self, question='', wait=1): self.__sapiensqa.printPrediction(question=question, wait=wait)
