from chatterbot import ChatBot

chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training With Own Questions 
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

chatbot.set_trainer(ListTrainer)
chatbot.train(training_data)

# Training With Corpus
#from chatterbot.trainers import ChatterBotCorpusTrainer

#chatbot.set_trainer(ChatterBotCorpusTrainer)

#chatbot.train("chatterbot.corpus.english")
