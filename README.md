SapiensQA (Question and Answer) is a proprietary Machine Learning algorithm for creating Natural Language Processing models where the answers are previously known.

# SapiensQA

The SapiensQA, or Sapiens for Questions and Answers, is a proprietary algorithm distributed freely for personal and/or commercial use. It is an Artificial Intelligence code that employs Machine Learning in creating expert language models. As an expert model, SapiensQA is focused on a single type of task, which is generating ready-made answers for predefined questions. Unlike Generative AI technologies like Transformers, SapiensQA doesn't use such approaches. Instead, it  applies a simple semantic comparison based on the Euclidean distance between input tokens to replicate the registered answer linked to the question that is geometrically closest to the user's prompt. This makes it much faster than generalist models and easily executable on machines with low processing power (1 core/4 GB or less of RAM memory) without the need for a GPU. It is ideal for the building customer service chatbots, query algorithms, systems for answering questions, and semantic search in files or documents.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install SapiensQA.

```bash
pip install sapiensqa
```

If you have a problem with one or more dependencies, you can install them manually via the requirements file.

```bash
pip install -r requirements.txt
```

## Usage
Basic usage example:
```python
from sapiensqa import SapiensQA # module import
sapiensqa = SapiensQA() # main class object instantiation
# record of answers for each possible question
sapiensqa.fineTuning('What is the SapiensQA?', 'The SapiensQA is an algorithm for creating language models.')
sapiensqa.fineTuning('Can I use SapiensQA commercially?', 'Yes, you can use SapiensQA commercially.')
# prints the answer linked to the registered question closest to the user's question
# note that it is not necessary to type the prediction question exactly the same as the registration question
sapiensqa.printPrediction('Please explain to me what is the SapiensQA.') # print: The SapiensQA is an algorithm for creating language models.
sapiensqa.printPrediction('Can I use it commercially?') # print: Yes, you can use SapiensQA commercially.
```
```bash
The SapiensQA is an algorithm for creating language models.
Yes, you can use SapiensQA commercially.
```
You can save your model so you don't have to retrain it every time a new prediction is run.
```python
from sapiensqa import SapiensQA # module import
sapiensqa = SapiensQA() # main class object instantiation
# record of answers for each possible question
sapiensqa.fineTuning('What is the SapiensQA?', 'The SapiensQA is an algorithm for creating language models.')
sapiensqa.fineTuning('Can I use SapiensQA commercially?', 'Yes, you can use SapiensQA commercially.')
'''
If no name is defined for the template file, a default name is applied.
The default name will start with "SapiensQA-Model-" and will be followed by an integer corresponding to the total number of saved model parameters (model size).
According to the international convention of language models, we use P for numbers less than a thousand parameters,
K for thousands of parameters, M for millions of parameters, B for billions of parameters and T for trillions of parameters.
Every SapiensQA model file will be of type QA (.qa extension).
'''
sapiensqa.saveModel() # saves the current training to a model file
```
If you wish, you can choose any name for your model by passing a string as a parameter to the "saveModel" method. The ".qa" extension is optional when defining the name and will be applied regardless of whether it is assigned or not.
```python
from sapiensqa import SapiensQA # module import
sapiensqa = SapiensQA() # main class object instantiation
# record of answers for each possible question
sapiensqa.fineTuning('What is the SapiensQA?', 'The SapiensQA is an algorithm for creating language models.')
sapiensqa.fineTuning('Can I use SapiensQA commercially?', 'Yes, you can use SapiensQA commercially.')
# it is also possible save your model with a custom name
sapiensqa.saveModel('name_of_your_choice') # the file will be saved with the prefix "name_of_your_choice"
# in this case we will have a model saved with the name "name_of_your_choice-127P.qa", where 127P is the number of model parameters
# if you prefer, you can rename the saved file to any name of your choice
```
For loading a saved model is very simple, just invoke the loadModel method passing as a parameter a string with the name of the model file that will be loaded.
```python
from sapiensqa import SapiensQA # module import
sapiensqa = SapiensQA() # main class object instantiation
# invoke the "loadModel" method to load a pre-trained model, this way you won't need to perform new training
sapiensqa.loadModel('name_of_your_choice-127P') # loads the name template "name_of_your_choice-127P" (the ".qa" extension is optional)
question = 'Please explain to me what is the SapiensQA.' # question to which you want an answer
sapiensqa.printPrediction(question) # prints the result of the prediction
```
```bash
The SapiensQA is an algorithm for creating language models.
```
```python
from sapiensqa import SapiensQA # module import
sapiensqa = SapiensQA() # main class object instantiation
# invoke the "loadModel" method to load a pre-trained model, this way you won't need to perform new training
sapiensqa.loadModel('name_of_your_choice-127P') # loads the name template "name_of_your_choice-127P" (the ".qa" extension is optional)
question = 'Can I use it commercially?' # question to which you want an answer
# you can assign a second integer parameter referring to the minimum tokens printing time (in seconds)
sapiensqa.printPrediction(question, 2) # prints all tokens in 2 seconds or more
```
```bash
Yes, you can use SapiensQA commercially.
```
With the "fit" method it is possible to train the model using a file with the text that will be used as a DataSet. The file does not need to be structured, but we advise you to clean it of any type of unwanted formatting and to eliminate special characters that are not part of the context. The recommendation is that you combine the texts of all other files that you want to use as a knowledge base into a single TXT file (preferably without blank lines). Although the recommendation is a TXT text file, PDF and DOCX files are also accepted. In the case of PDF files, you can use either a local file or the address of an online PDF file. WEB page addresses can also be used as a training source, in this case simply define a string with the address link as a method parameter.
```python
from sapiensqa import SapiensQA # module import
sapiensqa = SapiensQA() # main class object instantiation
# with the "fit" method you can train your model with a file (TXT, PDF or DOCX) or with a WEB page (PDF file links are also accepted)
sapiensqa.fit('file_name.txt') # just pass the training file path as a parameter (.txt, .pdf, .docx, online .pdf link or non-blocking web pages)
sapiensqa.saveModel() # use the "saveModel" method to save the model
```
```bash
Training progress: 005.2631578947%
Training progress: 010.5263157895%
Training progress: 015.7894736842%
Training progress: 021.0526315789%
Training progress: 026.3157894737%
Training progress: 031.5789473684%
Training progress: 036.8421052632%
Training progress: 042.1052631579%
Training progress: 047.3684210526%
Training progress: 052.6315789474%
Training progress: 057.8947368421%
Training progress: 063.1578947368%
Training progress: 068.4210526316%
Training progress: 073.6842105263%
Training progress: 078.9473684211%
Training progress: 084.2105263158%
Training progress: 089.4736842105%
Training progress: 094.7368421053%
Training progress: 100.0000000000%
```
Check out other data sources that can be accepted as training with the "fit" method below.
```python
sapiensqa.fit('file_name.docx') # training example using a microsoft word file as a data source
```
```python
sapiensqa.fit('file_name.pdf') # training example using an adobe portable document format file as a data source
```
```python
sapiensqa.fit('https://www.ibm.com/topics/artificial-intelligence') # training example using a web page as a data source
```
```python
sapiensqa.fit('https://ai.stanford.edu/~nilsson/MLBOOK.pdf') # training example using an online pdf document as a data source
```
Although not mandatory, it is always recommended to fine-tune possible questions and answers about the content of the training file. This way you will greatly increase the accuracy and effectiveness of your model. After the "fit" method, use the "fineTuning" method as many times as possible with example questions and answers about the file or link used in training. Fine-tuning can be a time-consuming process, but it is of fundamental importance in building good language models.
```python
from sapiensqa import SapiensQA # module import
sapiensqa = SapiensQA() # main class object instantiation
# with the "fit" method you can train your model with a file (TXT, PDF or DOCX) or with a WEB page (PDF file links are also accepted)
# you can hide the training progress by passing False in the second parameter of the "fit" method
sapiensqa.fit('https://en.wikipedia.org/wiki/Language_model', False) # example of training with a web page (False is optional)
# use the 'fineTuning' method as much as possible for a fine adjustment of quality
# note: to increase the accuracy of the model, you can optionally register variations of the same question for a single answer
sapiensqa.fineTuning('What is a language model?', 'A language model is a probabilistic model of a natural language.') # fine tuning 1
sapiensqa.fineTuning('When was the first statistical language model proposed?', 'In 1980, the first significant statistical language model was proposed.') # fine tuning 2
sapiensqa.fineTuning('What is a word n-gram language model?', 'A word n-gram language model is a purely statistical model of language.') # fine tuning 3
sapiensqa.fineTuning('What is a Skip-gram language model?', 'Skip-gram language model is an attempt at overcoming the data sparsity problem that preceding (i.e. word n-gram language model) faced.') # fine tuning 4
# sapiensqa.fineTuning... # fine tuning N
sapiensqa.saveModel('language_model') # the model will be saved with the name "language_model-8K.qa"
```
To capture the prediction return you can use the "predict" method which will return the string of the closest answer.
```python
from sapiensqa import SapiensQA # module import
sapiensqa = SapiensQA(.05) # if you want, you can define a value between 0 and 1 for the model temperature (level of variability in responses); default is .01
sapiensqa.loadModel('language_model-8K.qa') # loads the previously trained "language_model-8K.qa" model
answer = sapiensqa.predict('Do you know what an n-gram language model is?') # the "predict" method returns the answer to the question passed as a parameter
print(answer) # displays the response returned by the model
```
```bash
A word n-gram language model is a purely statistical model of language.
```
In addition to applying as much fine-tuning as possible, it is also good practice to adjust variations of the same question for the same answer. See an example of how to do this below:
```python
from sapiensqa import SapiensQA # module import
sapiensqa = SapiensQA() # main class object instantiation
sapiensqa.fit('file_name.docx') # training example with a microsoft word file
# example of fine tuning with variations of inputs for the same output
# with this technique it is possible to considerably increase the accuracy of the model
sapiensqa.fineTuning('Who are you?', "I'm SapiensQA.") # fine tuning 1
sapiensqa.fineTuning('Hello! Tell me who you are.', "I'm SapiensQA.") # fine tuning 2
sapiensqa.fineTuning('What is SapiensQA?', 'SapiensQA is an algorithm for creating specialized language models.') # fine tuning 3
sapiensqa.fineTuning('Could you explain to me what SapiensQA is all about?', 'SapiensQA is an algorithm for creating specialized language models.') # fine tuning 4
# sapiensqa.fineTuning... # fine tuning N
sapiensqa.saveModel('my_model') # method to save the pre-trained model
sapiensqa.printPrediction('Explain to me what SapiensQA is.') # displays the model response
```
```bash
SapiensQA is an algorithm for creating specialized language models.
```
You can also use a CSV table as a data source during the fine-tuning process. Assuming the CSV table below is named "table.csv", see how this would look using the pandas package:
| Question                                              | Answer                                                |
| ----------------------------------------------------- | ------------------------------------------------------ |
| Who are you?                                          | I'm SapiensQA.                                        |
| Hello! Tell me who you are.                            | I'm SapiensQA.                                        |
| What is SapiensQA?                                     | SapiensQA is an algorithm for creating specialized language models. |
| Could you explain to me what SapiensQA is all about?   | SapiensQA is an algorithm for creating specialized language models. |

First make sure you have the pandas package installed in your development environment.
```bash
pip install pandas
```
```python
from sapiensqa import SapiensQA # import sapiensqa main class
import pandas as pd # import pandas module renamed to pd
sapiensqa = SapiensQA() # main class object instantiation
# code structure for pandas
df = pd.read_csv('table.csv') # reading table from file as dataframe (stores in variable df)
questions = df['Question'].tolist() # converts the question column to a list of questions ("Question" key converted with tolist)
answers = df['Answer'].tolist() # converts the answers column to a list of answers ("Answer" key converted with tolist)
# uses a loop to cycle through both lists
for question, answer in zip(questions, answers): # as both lists have the same number of elements, we can use zip
    sapiensqa.fineTuning(question, answer) # inserts fine-tuning with question and answer data from the file
# to save the model just use the "saveModel" method
sapiensqa.saveModel('my_model') # method to save the pre-trained model
# if you want, you can perform a test to confirm the authenticity of the training
question = 'Hello! Tell me who you are.' # variable with a test question
sapiensqa.printPrediction(question) # prediction test
```
```bash
I'm SapiensQA.
```
With SapiensQA it is possible to perform a transfer learning routine to combine the parameters of two different models and generate a new, larger and more accurate model with the information learned by the previous two.
WARNING: joining very large models may cause the learning transfer completion time to increase considerably.
```python
from sapiensqa import SapiensQA # module import
sapiensqa = SapiensQA() # main class object instantiation
# to transfer learning from one model to another use the "transferLearning" method
# in the first parameter define the path or name of the model that will transfer your learning
# in the second parameter define the path or name of the model that will receive the learning
# in the third parameter define the path or name of the model that will be saved with the learning of the two previous models
sapiensqa.transferLearning('your_transmitter_model-8K.qa', 'your_receiver_model-2K.qa', 'new_model') # in this example, a new model will be saved with 10K total parameters (8K + 2K)
# "new_model-10K.qa" will be the name of the new model with the sum of the learning of the two models that were passed as a method parameter
```

## Methods
### Construtor: SapiensQA

Parameters
| Name         | Description                            | Type  | Default Value |
|--------------|----------------------------------------|-------|---------------|
| temperature  | Temperature of result variability    | float | .01           |

### fit: Train the model with a file or web address
Parameters
| Name          | Description                                       | Type | Default Value |
|---------------|---------------------------------------------------|------|---------------|
| path          | Path plus file name with extension or URL address | str  | ''            |
| show_progress | Enables or disables the display of training progress | bool | True          |

### fineTuning: Trains the model by fine-tuning pre-defined questions and answers
Parameters
| Name      | Description                                             | Type | Default Value |
|-----------|---------------------------------------------------------|------|---------------|
| question  | Possible question that may be asked by the user       | str  | ''            |
| answer    | Answer to be returned when the same or similar question is asked | str  | ''            |

### saveModel: Saves a file with the current model training
Parameters
| Name   | Description                                          | Type | Default Value |
|--------|------------------------------------------------------|------|---------------|
| path   | Path plus model name with or without the .qa extension | str  | ''            |

### loadModel: Load a pre-trained model
Parameters
| Name   | Description                                          | Type | Default Value |
|--------|------------------------------------------------------|------|---------------|
| path   | Path plus model name with or without the .qa extension | str  | ''            |

### transferLearning: Transfer learning from one model to another
Parameters
| Name             | Description                                                              | Type | Default Value |
|------------------|--------------------------------------------------------------------------|------|---------------|
| transmitter_path | Path plus model name with or without the .qa extension that will transmit the knowledge | str  | ''            |
| receiver_path    | Path plus name of the model with or without the .qa extension that will receive the knowledge | str  | ''            |
| rescue_path      | Path plus model name with or without the .qa extension that will be saved with the union of knowledge | str  | ''            |

### predict: Returns a str prediction with the current model
Parameters
| Name      | Description                           | Type | Default Value |
|-----------|---------------------------------------|------|---------------|
| question  | Question to which you want an answer | str  | ''            |

### printPrediction: Print a prediction with the current model
Parameters
| Name      | Description                                  | Type  | Default Value |
|-----------|----------------------------------------------|-------|---------------|
| question  | Question to which you want an answer        | str   | ''            |
| wait      | Minimum time in seconds for response display to complete | float | 1             |

## Complete Example With All Features
```python
from sapiensqa import SapiensQA
sapiensqa = SapiensQA(temperature=.2)

sapiensqa.fit(path='file_name.txt')
sapiensqa.saveModel(path='my_language_model-1')

sapiensqa.loadModel(path='my_language_model-1')
sapiensqa.fineTuning(question='Example number 1 of any question', answer='Example number 1 of an answer to the question')
sapiensqa.fineTuning(question='Example number 2 of any question', answer='Example number 2 of an answer to the question')
sapiensqa.fineTuning(question='Example number 3 of any question', answer='Example number 3 of an answer to the question')
sapiensqa.fineTuning(question='Example number 4 of any question', answer='Example number 4 of an answer to the question')
sapiensqa.fineTuning(question='Example number 5 of any question', answer='Example number 5 of an answer to the question')
sapiensqa.fineTuning(question='Example number 6 of any question', answer='Example number 6 of an answer to the question')
sapiensqa.fineTuning(question='Example number 7 of any question', answer='Example number 7 of an answer to the question')
sapiensqa.fineTuning(question='Example number 8 of any question', answer='Example number 8 of an answer to the question')
sapiensqa.fineTuning(question='Example number 9 of any question', answer='Example number 9 of an answer to the question')
sapiensqa.fineTuning(question='Example number N of any question', answer='Example number N of an answer to the question')

sapiensqa.saveModel(path='my_language_model-2')

sapiensqa.transferLearning(transmitter_path='my_language_model-1', receiver_path='my_language_model-2', rescue_path='my_language_model-3')

sapiensqa.loadModel(path='my_language_model-3')
question = 'Example number 5 of any question'
answer = sapiensqa.predict(question=question)
print(answer)

question = 'Example number 7 of any question'
sapiensqa.printPrediction(question=question)

```
```bash
Example number 5 of an answer to the question
Example number 7 of an answer to the question
```

## Contributing

We do not accept contributions that may result in changing the original code.

Make sure you are using the appropriate version.

## License

This is proprietary software and its alteration and/or distribution without the developer's authorization is not permitted.
