import re
from rasa_nlu.model import Interpreter


def sanitize_sms(sms):
    sms = sms.replace('no.', '')
    sms = re.sub('\S+@\S+', 'emailaddr', sms)
    sms = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] |[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 'httpaddr', sms)
    length = len(sms)

    for i, c in enumerate(sms):
        if c == '.':
            if i + 2 < length:
                if sms[i + 2] != ' ' and not sms[i + 2].isdigit():
                    sms = sms[:i + 1] + ' ' + sms[i + 1:]

    sms = sms.lower()
    sms = sms.strip()
    sms = sms.replace('ac ', 'account ')
    sms = sms.replace('a/c', 'account')
    sms = sms.replace('acct', 'account')
    sms = sms.replace('inr.', 'INR')
    sms = sms.replace('usd', 'rs ')
    sms = sms.replace('inr', 'rs ')
    sms = sms.replace('rs.', 'rs. ')
    sms = sms.replace(' rs', ' rs. ')
    sms = sms.replace('account no.', 'account ')
    sms = sms.replace('*', 'x')
    sms = sms.replace('  ', ' ')
    sms = sms.replace('   ', ' ')
    sms = sms.replace('. ', ' ')
    sms = sms.replace(':', ' ')
    sms = sms.replace('  ', ' ')
    sms = sms.replace('-', '/')
    sms = sms.replace('_', ' ')
    sms = sms.replace('/jan/', '/01/')
    sms = sms.replace('/feb/', '/02/')
    sms = sms.replace('/mar/', '/03/')
    sms = sms.replace('/apr/', '/04/')
    sms = sms.replace('/may/', '/05/')
    sms = sms.replace('/jun/', '/06/')
    sms = sms.replace('/jul/', '/07/')
    sms = sms.replace('/aug/', '/08/')
    sms = sms.replace('/sep/', '/09/')
    sms = sms.replace('/oct/', '/10/')
    sms = sms.replace('/nov/', '/11/')
    sms = sms.replace('/dec/', '/12/')
    sms = sms.replace('avbl', 'available balance')
    sms = sms.replace('avl bal', 'available balance')
    return sms

#   Train RASA  nlu model for spacy
# def train_nlu(data, config, model_dir):
#     training_data = load_data(data)
#     trainer = Trainer(RasaNLUConfig(config))
#     trainer.train(training_data)
#     model_directory = trainer.persist(model_dir, fixed_model_name='pfm')


# train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')

interpreter = Interpreter.load('./models/nlu/default/nluTensorflow')

sms = "Your a/c XX4567 is credited on  30/01/2019 by INR 25,700.00 towards Salary/Reimbursement. Avl Bal: INR26,000.40. To kno more login to m.sc.com/in -Stan"
sms = sanitize_sms(sms)
parsed_text = interpreter.parse(sms)
print (parsed_text)
sms = "Dear Customer, stmt for Credit Card XX0023 has been sent to  myemail@gmail.com. Total amt of Rs. 1357 or Min. amt of Rs. 520 is due by 30-JAN-19."
sms = sanitize_sms(sms)
parsed_text = interpreter.parse(sms)
print (parsed_text)
sms = "Dear Customer your Account XX4321 had been credited with INR 14,075.00 on 30-Jan-19. Info: NEFT-ICMS1805312342IY-AAW IT. The Available Balance is INR 365,985.60."
sms = sanitize_sms(sms)
print (sms)
parsed_text = interpreter.parse(sms)
print (parsed_text)
sms = "Hello, Your A/c no. 0245 had been credited with  Rs. 1000 on 30Jan19. The A/c balance is Rs. 97733.30. Info: IMPS/P2A/817999903740/919901211111/52. Call 18605005555 (if in India) if you have not done this transaction ."
sms = sanitize_sms(sms)
parsed_text = interpreter.parse(sms)
print (parsed_text)