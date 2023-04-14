import paho.mqtt.client as mqtt

tasks = [{"id": 1, "description": "Verificar temperatura", "status": "em andamento"}]

def on_connect(client, userdata, flags, rc):
    print("Conectado com sucesso ao broker MQTT")
    client.subscribe("temperatura")

def on_message(client, userdata, msg):
    temperatura = float(msg.payload.decode())
    print("Temperatura recebida:", temperatura)
    if temperatura > 25:
        for task in tasks:
            if task["description"] == "Verificar temperatura":
                task["status"] = "concluída"
                print("Tarefa atualizada:", task)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.1", 1883, 60)

client.loop_forever()
