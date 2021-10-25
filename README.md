# Mineração de bitcoin

Esse código testa vários hashs diferentes até encontrar o certo. Você pode dar sorte e ficar rico com só uma tentativa ou investir milhares de reais nessa empreitada e perder para um indiano aleatório. Muitas possibilidades.

##

A lógica do sistema é simples:
 * Concatena o número do bloco, as transações do bloco e o hash anterior e em seguida, o codifica pro padrão SHA256;
 * Depois, ele pega esse texto codificado e testa ele até encontrar o padrão, a partir do nonce (que inicia em 0 e vai aumentando a cada tentativa falha);
 * Se o hash estiver com a quantidade certa de zeros no início, no padrão SHA256, ele te mostra o hash vencedor, o nonce que formou esse hash e quanto tempo você levou para achar ele.

Ou seja, como o hash atual é baseado nos parâmetros já sabidos e no nonce (que ainda não é conhecido), basta testar cada nonce possível até encontrar o hash certo.
Quando o hash estiver certo, você consegue minerar os bitcoins que eles te prometeram no site [Blockchain Explorer](https://www.blockchain.com/pt/explorer). Boa sorte!
