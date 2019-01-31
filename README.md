# RasaDemo
https://rasahq.github.io/rasa-nlu-trainer/

#command to train model
python -m rasa_nlu.train -c nlu_config.yml --data testData.json -o models --fixed_model_name nlu --project current --verbose
