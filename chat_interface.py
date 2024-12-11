from llama_chat import LlamaChat
import os
import argparse

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def chat(schema_file=None):
    chat_bot = LlamaChat()
    conversation = []
    
    if schema_file:
        # Carrega o schema do arquivo
        response = chat_bot.load_schema_from_file(schema_file)
        print(f"SQLlama: {response}")
    else:
        # Primeira mensagem solicitando o schema
        print("SQLlama: Send the path to the database schema file.")
        while not chat_bot.schema:
            schema_path = input("You: ")
            if schema_path.lower() == 'sair':
                return
            response = chat_bot.load_schema_from_file(schema_path)
            conversation.append(("Você", schema_path))
            conversation.append(("Modelo", response))
            if "Error" in response:
                print(f"SQLlama: {response}")
                continue
    
    print("\nSQLlama: Schema loaded. You can ask your questions!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
            
        response = chat_bot.generate_response(user_input)
            
        # Adiciona à conversa
        conversation.append(("You", user_input))
        conversation.append(("SQLlama", response))
        
        # Limpa a tela e mostra toda a conversa
        clear_screen()
        print("Chat (type 'exit' to end)\n")
        for speaker, message in conversation:
            print(f"{speaker}: {message}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Chat with SQLlama')
    parser.add_argument('--schema', type=str, help='Path to your SQL schema file')
    args = parser.parse_args()
    
    chat(args.schema) 