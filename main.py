import re
import getpass

# Expressões regulares para os campos com validação
PADROES_REGEX = {
    "email": r"^[\w\.-]+@[\w\.-]+\.\w{2,}$",
    "cpf": r"^\d{3}\.\d{3}\.\d{3}-\d{2}$",
    "telefone": r"^\(?\d{2}\)?\s?\d{4,5}-\d{4}$",
    "senha_forte": r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{8,}$"
}

usuarios = []

def validar_entrada(valor: str, tipo: str) -> bool:
    padrao = PADROES_REGEX.get(tipo)
    if not padrao:
        raise ValueError(f"Tipo de validação desconhecido: '{tipo}'")
    return bool(re.fullmatch(padrao, valor))

def menu():
    print("\nValidador e Cadastro de Usuários\n")
    print("Campos obrigatórios:")
    print(" - nome_usuario")
    for tipo in PADROES_REGEX:
        print(f" - {tipo}")
    print("Digite 'sair' a qualquer momento para encerrar.\n")

    while True:
        usuario = {}
        print("Novo usuário:")

        # Nome de usuário (sem regex)
        while True:
            nome = input("Informe o nome de usuário: ").strip().title()
            if nome.lower() == "sair":
                print("\nEncerrando cadastro...\n")
                exibir_usuarios()
                return
            if nome:
                usuario["nome_usuario"] = nome
                break
            else:
                print("Nome de usuário não pode estar vazio.")

        # Campos com validação
        for campo in PADROES_REGEX:
            while True:
                if campo == "senha_forte":
                    valor = getpass.getpass("Informe a senha forte (oculta): ").strip()
                else:
                    valor = input(f"Informe o {campo}: ").strip()

                if valor.lower() == "sair":
                    print("\nEncerrando cadastro...\n")
                    exibir_usuarios()
                    return

                if validar_entrada(valor, campo):
                    if campo == "senha_forte":
                        usuario[campo] = "********"  # Armazenar senha ocultada
                    else:
                        usuario[campo] = valor
                    break
                else:
                    print(f"{campo.upper()} inválido! Tente novamente.")

        usuarios.append(usuario)
        print("Usuário salvo com sucesso!\n")

def exibir_usuarios():
    print("================= USUÁRIOS CADASTRADOS =================")
    if not usuarios:
        print("Nenhum usuário foi registrado.")
    else:
        for i, user in enumerate(usuarios, start=1):
            print(f"\nUsuário {i}:")
            for chave, valor in user.items():
                print(f"  {chave}: {valor}")

# Executar programa
if __name__ == "__main__":
    menu()
