import openai
import os
import json
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-3.5-turbo"

texto = """En una ciudad nocturna y lluviosa,
el detective Sam Roberts camina por las solitarias calles de Chicago, buscando
pistas sobre un caso de asesinato que ha mantenido a la ciudad en vilo durante
semanas. A medida que la lluvia golpea las aceras, una sombra oscura se
desliza por el callejón cercano, enviando un escalofrío por la espalda de Sam..."""

p1 = "¿Qué descubre en el oscuro callejón?"
p2 = "¿Qué peligros acechan?"

pl_js = '{"Error": "Descripción error","Pasos a seguir": [{"paso1": "descripcion paso1"},{"paso2": "descripcion paso2"}],"Conclusion": "conclusión"}'
pl_js2 = '{"Texto original": "texto","Continuacion": "contiuacion"}'

def openai_interaction(modelo=MODEL, role="AI assistant", user_message="", platilla_json={}, temp=0, frequency_penalty=0, presence_penalty=0):
    response = openai.chat.completions.create(
    model=modelo,
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "Tu rol especifico es" + role + ". Tienes que responder en español y en formato JSON de la siguiente manera: "+ platilla_json},
        {"role": "user", "content": user_message},
    ],
    temperature=temp,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty,
    seed=1234
    )
    
    res = response.choices[0].message.content
    
    return res


res = openai_interaction(MODEL, "experto en resolución de incidencias de configuración de Windows", "Python no se reconoce como un comando interno o externo", pl_js)
with open("resultado_bloque1_seed1234_prueba2.json", "w") as file:
    json.dump(res, file, indent=4)

print(res)
    
res1 = openai_interaction(MODEL, "escritor auxiliar", "Acaba la siguiente historia respondiendo las preguntas, " + p1 + " y " + p2 + " y añadiendo un giro inesperado o una revelación impactante: " + texto, pl_js2, frequency_penalty=0.5, presence_penalty=0.5)
with open("resultado_bloque2_seed1234_prueba2.json", "w") as file:
    json.dump(res1, file, indent=4)
    
print(res1)


