from bardapi import Bard



token = 'XwitUVn4DiaU1wsaoGDnDm3SxxmWd_eyVgk917rUKPZlHIfgyzyz4aWrcA5KyVVthV6wBg.'
bard = Bard(token=token)
response =bard.get_answer("what is start?")['content']
print(response)