from hashlib import sha256
import time

def aplicar_sha256(texto):
	return sha256(texto.encode('ascii')).hexdigest() # Codificando a partir do método SHA256

def	minerar(num_bloco, transacoes, hash_anterior, qntd_zeros): # Função de mineração
	nonce = 0 # Valor que definirá o hash atual
	while True:
		texto = str(num_bloco) + transacoes + hash_anterior
		meu_hash = aplicar_sha256(texto)
		if meu_hash.startswith("0" * qntd_zeros): # Se o hash estiver certo, me mostre ele
			return nonce, meu_hash
		nonce += 1 # Senão, começa de novo!

if __name__ == "__main__": # Testar somente nesse doc. Se importar depois, isso aqui não aparece.
	# Todos os dados são exempos irreais visando apenas teste
	num_bloco = 10 # Número do bloco
	transacoes = """
	Pedro->Adriana->12
	Adriana->Carla->8
	Carla->Gabriella->15""" # Fulano pagou para Ciclano o valor de R$ n
	qntd_zeros = 3 # Quantidade de 0's no começo do hash atual
	hash_anterior = "abc" # Hash anterior para poder calcular

	inicio = time.time()
	resultado = minerar(num_bloco, transacoes, hash_anterior, qntd_zeros) # Passando os valores declarados
	print(resultado) # O nonce e o hash atual!
	print('Você demorou', (time.time() - inicio), 'segundos para completar a mineração.') # Sério, cara. Precisa de um baita PC.