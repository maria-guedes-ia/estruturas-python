class TextoAnalisado(object):
	
	def __init__(self,texto):
		
		# Substitui a pontuação por nada (ponto, interrogação, exclamação e vírgula)
		vtextoFormatado = texto.replace('.','').replace('?','').replace('!','').replace(',','')
		# Transforma o texto em letras minúsculas
		vtextoFormatado = vtextoFormatado.lower()
		# fmtTexto é variável resultante das operações realizadas dentro do construtor
		self.fmtTexto = vtextoFormatado

	def freqTodasPalavras(self):
		
		# Divide o texto em umas lista de palavras a partir do espaçamento
		vlistaPalavras = self.fmtTexto.split(' ')
	
		# Criação de dicionário a partir do percorrimento da lista, sendo as palavras a chave, 
		# e quantidade de vezes que a palavra aparece o valor
		dicfreqPalavras = {}
		for palavra in vlistaPalavras:
			dicfreqPalavras[palavra] = vlistaPalavras.count(palavra)
		
		return dicfreqPalavras

	def freqPalavraEspecif(self,palavra):
		
		# Conseguindo a frequência de todas as palavras
		freqDic = self.freqTodasPalavras()
		
		# Passando a entrada do usuário para minúsculo para assegurar que seja encontrada
		palavra = palavra.lower()

		# Analisando se a palavra consta no dicionário e retornando a quantidade
		if palavra in freqDic:
			return freqDic[palavra]
		else:
			return 0

texto_para_analise = "Carol foi para casa? Sim, ela foi! Ela já voltou? Não, ela ainda não voltou."

texTando = TextoAnalisado(texto_para_analise)
print(texTando.freqTodasPalavras())
print('\n',texTando.freqPalavraEspecif('Ela'))







