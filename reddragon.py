# Dúvidas?   | \
# Ideias?    |    Me chame no telegram: https://t.me/rdzin9
# Bugs?      | /

import os
import sys
import re
import random
import requests
import bs4
import fake_useragent
import datetime
from time import sleep
from BanerScan import BanerScan

__AUTOR__ = "NANO"
__TELEGRAM__ = "https://t.me/rdzin9"
__VERSIONS__ = 1.0

class GetDadosUsuario:
	""" ETAPA 1 """

	def __init__(self,option=False,wordlist=False,dork=False):
		BanerScan()
		""" CONSTRUÇÃO DA ETAPA 1 """
		self.option = option
		self.wordlist = wordlist
		self.dork = dork
		self.Requisicao = requests.Session()
		self.UsersAgent = [fake_useragent.UserAgent()["google chrome"],fake_useragent.UserAgent().ff,fake_useragent.UserAgent().firefox,fake_useragent.UserAgent()["safari"]]
		self.NumPagesSchsWeb = []
		self.LinksFiltrados1 = []
		self.LinksFiltrados2 = []
		self.LinksParaTestes = []
		self.DorksBuscasWebs = []
		self.ErrorsSQL = [
		"SQL",
		"sql",
		"Aviso: mysql_fetch_array()",
		"NoSql",
		"nosql",
		"noSQL",
		"noSql",
		"noSqL",
		"sintaxe SQL",
		"SINTAXE SQL",
		"MySql",
		"Fatal Error",
		"Fatal error",
		"fatal error",
		"function fetch"
		]
		self.HeadersChromium = {'UserAgent':self.UsersAgent[random.randint(0,3)],"'referer'":"'https://www.google.com/'"}

# MÉTODO PARA CAPTURAR OS LINKS NAS PÁGINAS DE BUSCA

	def FiltrarURL(self):
		""" FILTRANDO TODAS AS URLS RECEBIDAS PELA CONEXÃO """

		self.RealLinkBuscaDork1 = "https://br.search.yahoo.com/search?ei=UTF-8&fr=crmas&p="

		if self.option == "-d":
			self.RealLinkBuscaDork2 = self.dork.replace(":","%3A")
			self.RealLinkBuscaDork3 = self.RealLinkBuscaDork2.replace("?","%3F")
			self.RealLinkBuscaDork4 = self.RealLinkBuscaDork3.replace("=","%3D&")
			self.RealLinkBuscaDork5 = self.RealLinkBuscaDork4
			self.RealLinkBuscaDork6 = self.RealLinkBuscaDork1+self.RealLinkBuscaDork5
			print("\033[1;32m[*]\033[m \033[1;33mBUSCANDO COM A DORK: \033[m\033[1;4m{}\033[m\n".format(self.dork))

		self.CookiesGoogle = {
		"1P_JAR":"2024-06-24-23",
		"AEC":"AQTF6HxkLdh9L5h_xMUL7yZdFGFmpWDnaCTbE706ZZM9ysby8SgK3A3lPsQ",
		"APISID":"me2_C91mNmk2T4ea/A9MTv7jYwQbL_MC8D",
		"DV":"M7Mjtrqpj91T0MwzaUe0CfwwkOLIBFlpedIjqK-QNgEAAFDp7JXFwc47TgAAAKhfz8hqWLzWHAAAALn1Nrq_BAmKEgAAAA",
		"HSID":"AU5PtybEnuyCQTbMd",
		"NID":"515=T8iJKxtcGN9lrTUhHzEdpz__5E2d5Bh3tXjpAOoBDLN_FUmhYOOuo4wJ9ak8ll-g7EfVwJ9Gfs1bR8U1cvBVy0-6aQAmTTVK7kf56iF_wAaO7Tp_WlOzVFj9IVIUv7DvhX9KPDl3JBjnMD9O4gySMZKGkZHJ_gqQtgjPz7XYMk0CSRMTyMc3ili4iXnQsCUMA53UadQ_Rem0-ZgNbYpJBJdm66Rt7GhX8o4QWp1fQ1ZW0hVjHSMjJqzy-5PTiwTEkpUcwdgeHIECqgK7C0oBgLSOHVWHgitB_o9momshwfxBanoO7xkF5lPOrDCAyAobLX-hR-s238Oa0XHEPZP5T1MMdg6Gs0jUgEtLiMUPF-gu2q9QkwEbh9Wrrz9WxnZdUwuqTmGU2Sn7wpgfwuH7RJDo1Xn5iiC0nFpNvt3uDtlK_Yw3DYnhDuhzd1-y71NI6UiZBIYvx2JmUZ1PSBQdAo0d53sY1kolqFckVRoMwKvBSMuhZdkgDxVF7NwJVVxPFhZL9zwYsbmHd-R7IxUmQlKKmO0MWsn3",
		"OSID":"g.a000gQimVXRiO29aP4uNI90Hb-L_r7Umosdy2VhCUrejYMjCq67ObmI7Vbo9LGOBC1PWTmFvJQACgYKAf0SAQASFQHGX2MieIxZe65negwacLSyFB6nERoVAUF8yKogCRVNp4xtUxpYUnNjmJzf0076",
		"SAPISID":"SAPISID",
		"SEARCH_SAMESITE":"CgQIy5oB",
		"SID":"g.a000lAimVdYFeeEowSBrNRE1eejNm1GwRWfQMKltl6e4H7ydosrk4dv0P_jxOO9xPouuh_fspwACgYKAWgSARESFQHGX2Mil0hnCMDtxg3r2VotN3kvvBoVAUF8yKpu1J71SW2IZoYCELtQm_V60076",
		"SIDCC":"AKEyXzXJzh9k732p12uD5lQYwrqv9CUwRpUAYYF5gKNrHeNhNnNl-5KXh72x2IGqGtQYhhxrM7I",
		"SSID":"AaKhRtTK8La-AGJVF",
		"__Secure-1PAPISID":"TqUlNBySdVnw27az/A17YUa39ImUc3sKZm",
		"__Secure-1PSID":"g.a000lAimVdYFeeEowSBrNRE1eejNm1GwRWfQMKltl6e4H7ydosrk9Qc3Q7Udr_HFxyXD8rQpKAACgYKAVkSARESFQHGX2MipYrvMFqlZFAeMOBXZGnElhoVAUF8yKrntQY0gHIdcm6h9j9sf_wq0076",
		"__Secure-1PSIDCC":"AKEyXzVQ-qCpdHN0UuwmC8Z_HfDy97bxsNsbsuHJjLEzcMoOsvXiskV1N4lFIpDI4lrQIR2Uur4",
		"__Secure-1PSIDTS":"sidts-CjIB3EgAEjOIfFEaTj_8K_nGosatZ1J5X9VEn-Y_nn4WiCrTHOfBA33TUBPVZyaeTzydjBAA",
		"__Secure-3PAPISID":"TqUlNBySdVnw27az/A17YUa39ImUc3sKZm",
		"__Secure-3PSID":"g.a000lAimVdYFeeEowSBrNRE1eejNm1GwRWfQMKltl6e4H7ydosrkrggLb-5R_4fdbeWHTyWX3wACgYKAZUSARESFQHGX2MiDi_5HAJWYISp9hAFLzrqsBoVAUF8yKp02yVgdYAGHfU0Tc-5gZ_u0076",
		"__Secure-3PSIDCC":"AKEyXzUGmEqw3ka9QAgYzuVyEERZKhV3-AYMe0phBF2Sy02bpJBxR3VM1MB0PnrfzWoz4y4GxQ",
		"__Secure-3PSIDTS":"sidts-CjIB3EgAEjOIfFEaTj_8K_nGosatZ1J5X9VEn-Y_nn4WiCrTHOfBA33TUBPVZyaeTzydjBAA",
		"__Secure-OSID":"g.a000gQimVXRiO29aP4uNI90Hb-L_r7Umosdy2VhCUrejYMjCq67OyoT5CWNh5Fj-QpYZ38hyxgACgYKARoSAQASFQHGX2MiDAAosHP6P2aM3uS-PGWCKRoVAUF8yKoaMWQw9w_0eyVkqdqrhaCJ0076",
		"_ga":"GA1.1.1761629692.1707431141",
		"_ga_6VGGZHMLM2":"GS1.1.1707431141.1.0.1707431141.0.0.0",
		}
		self.proxy1 = {"27.54.71.234":"8080"}
		self.proxy2 = {"45.173.231.15":"999"}

# PEGAR PÁGINAS DE PESQUISA NO NAVEGADOR:

	def GetPagesSearch(self):

		print("\033[1;32m[+]\033[m \033[1;33mBUSCA INICIADA AS:\033[m [{}]\n".format(datetime.datetime.now().strftime("%H:%M:%S")))
		self.IniciarBuscaPage = self.Requisicao.get(self.RealLinkBuscaDork6,headers=self.HeadersChromium,cookies=self.CookiesGoogle,proxies=self.proxy1)
		self.BuscasPaginasWEB = bs4.BeautifulSoup(self.IniciarBuscaPage.text,"html.parser")

		# AQUI RETORNA AS PÁGINAS DE BUSCA
		self.ResultadosBuscas = self.BuscasPaginasWEB.find_all("a",{"referrerpolicy":"unsafe-url"},href=True)
		
		for pages in self.ResultadosBuscas:
			if pages["href"].startswith("https://br.search.yahoo.com/search?p="):
				self.NumPagesSchsWeb.append(pages["href"])


		for Num, LinksPages in enumerate(self.NumPagesSchsWeb):
			print("\033[1;32m[+]\033[m \033[1;33mRealizando buscas na página\033[m \033[1;32m{}\033[m: \033[1;36m{}\033[m".format(Num+1,LinksPages))
			self.IniciarBusca = self.Requisicao.get(LinksPages,headers=self.HeadersChromium,cookies=self.CookiesGoogle,proxies=self.proxy2)
			self.Htmls2 = bs4.BeautifulSoup(self.IniciarBusca.text,"html.parser")
			self.Data = self.Htmls2.find_all("a",{"referrerpolicy":"origin"},href=True)

			for LinkSitesWeb in self.Data:
				#self.LinksParaTestes.append(LinkSitesWeb["href"])
				validlinkf = re.search(r"^(http://|https://){1}(.)+(id\=[0-9]+|cat\=[0-9]+)$",str(LinkSitesWeb["href"]),re.IGNORECASE)
				if validlinkf:
					self.LinksFiltrados1.append(LinkSitesWeb["href"])

	def FilterURLForOnline(self):
		""" OPÇÕES DA ETAPA 1 """
		BanerScan()
		print("\n\033[1;32m[+]\033[m \033[1;33mFILTRANDO URL'S E VERIFICANDO SE OS SITES ESTÃO ONLINE PARA TESTES...:\n\033[m")
		for nums, urls in enumerate(self.LinksFiltrados1):
			try:
				self.IniciarBusca = self.Requisicao.get(urls,headers=self.HeadersChromium,cookies=self.CookiesGoogle,proxies=self.proxy2)
			except requests.exceptions.SSLError:
				print("\033[1;31m[!]\033[m \033[1;3mSite\033[m\033[1m:\033[m \033[1;32m{}\033[m \033[1mCom problemas de conexão SSL!\033[m".format(urls))
			except requests.exceptions.ConnectionError:
				print("\033[1;31m[!]\033[m \033[1;3mSite\033[m\033[1m:\033[m \033[1;32m{}\033[m \033[1mLink Quebrado ou Página removida!\033[m".format(urls))
			else:
				print("\033[1;32m[*]\033[m \033[1;3mSite\033[m\033[1m:\033[m \033[1;32m{}\033[m \033[1mONLINE!\033[m".format(urls))
				self.LinksFiltrados2.append(urls)

	def ExploreSQL(self):
		""" EXPLORANDO AS FALHAS SQLinjection """
		BanerScan()
		print("\n\033[1;32m[{}]\033[m\033[1;32m [+]\033[m \033[1;33mREALIZANDO TESTES PARA A FALHA: \033[1;4;36mSQLinjection\033[m:\n\033[m")
		print("\033[1;32m[{}]\033[m\033[1;36m [*]\033[m \033[1mSites filtrados:\033[m \033[1;33m[{}]\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),len(self.LinksFiltrados2)))
		print("\033[1;32m[{}]\033[m\033[1;36m [*]\033[m \033[1mEscaneando código da página...\033[m\n".format(datetime.datetime.now().strftime("%H:%M:%S")))
		sleep(4)
		for TestesURLfalhas in self.LinksFiltrados2:
			BanerScan()
			print("\033[1;32m[+]\033[m \033[1mEscaneando o site: {}\033[m\n".format(TestesURLfalhas))
			try:
				self.IniciarBuscasSQL = self.Requisicao.get(TestesURLfalhas+"'",headers=self.HeadersChromium,cookies=self.CookiesGoogle,proxies=self.proxy2)
			except requests.exceptions.SSLError:
				print("\033[1;31m[!]\033[m \033[1mSite com problemas de conexão SSL!\033[m")
			except requests.exceptions.ConnectionError:
				print("\033[1;31m[!]\033[m \033[1mSite com problemas de conexão!\033[m")
			else:
				self.SearchFalhasSQL = bs4.BeautifulSoup(self.IniciarBuscasSQL.text,"html.parser")
				self.ArmazenarFalhasSQL = self.SearchFalhasSQL.get_text()
				for NumFalhas, TesteFalhas in enumerate(self.ErrorsSQL):
					if TesteFalhas in self.ArmazenarFalhasSQL:
						print("\033[1;32m[{}]\033[m\033[1;33m [+] Site escaneado:\033[m \033[1m{} \033[m\033[1;4;36mSTATUS:\033[m \033[1;32m[VULNERÁVEL]\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),TestesURLfalhas))
						print("\033[1;32m[{}]\033[m\033[1;33m [*]\033[m Armanezando em\033[m\033[1;36m Vulners.txt\033[m")
						with open("Vulners.txt","a") as AddSQLError:
							AddSQLError.write("-----------------------------------------------------------\n")
							AddSQLError.write("Site:"+str(TestesURLfalhas)+"\n")
							AddSQLError.write("Horario consulta: {}\n".format(datetime.datetime.now().strftime("%H:%M:%S")))
							AddSQLError.write("-----------------------------------------------------------\n")
							AddSQLError.write("\n")
							AddSQLError.close()
						sleep(2)
						break
					else:
						print("\033[1;32m[{}]\033[m\033[1;31m [!]\033[m \033[1mSite escaneado: {}, \033[1;33mSTATUS\033[m: \033[1;31m[NOT VULN]\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),TestesURLfalhas))
						sleep(0.6)

class ScannerOnlyWebSite:
	""" CLASSE ESCANEAMENTO ÚNICO """
	def __init__(self,website):
		""" OPÇÃO PARA EXPLORAR UM SITE RETORNANDO TODOS OS LINKS DO MESMO """
		self.WebSite = website
		self.LinksWB = []
		self.Connect = requests.Session()
		self.HeaderW = [fake_useragent.UserAgent()["google chrome"],fake_useragent.UserAgent().ff,fake_useragent.UserAgent().firefox,fake_useragent.UserAgent()["safari"]]
		self.Proxies1 = {"41.65.67.167":"1976"}
		self.Proxies2 = {"159.224.232.194":"8888"}
		self.Proxies3 = {"211.253.36.172":"5001"}
		self.Proxies4 = {"103.156.233.157":"3456"}
		self.LinksFinalsPHP = []
		self.LinksFinalsTests = []
		self.SCANEAR = False
		self.ErrorsSQLi = [
		"SQL",
		"sql",
		"Aviso: mysql_fetch_array()",
		"NoSql",
		"nosql",
		"noSQL",
		"noSql",
		"noSqL",
		"sintaxe SQL",
		"SINTAXE SQL",
		"MySql",
		"Fatal Error",
		"Fatal error",
		"fatal error",
		"function fetch"
		]
		self.MORE = False

		self.CookieJs = {
		"1P_JAR":"2024-06-24-23",
		"AEC":"AQTF6HxkLdh9L5h_xMUL7yZdFGFmpWDnaCTbE706ZZM9ysby8SgK3A3lPsQ",
		"APISID":"me2_C91mNmk2T4ea/A9MTv7jYwQbL_MC8D",
		"DV":"M7Mjtrqpj91T0MwzaUe0CfwwkOLIBFlpedIjqK-QNgEAAFDp7JXFwc47TgAAAKhfz8hqWLzWHAAAALn1Nrq_BAmKEgAAAA",
		"HSID":"AU5PtybEnuyCQTbMd",
		"NID":"515=T8iJKxtcGN9lrTUhHzEdpz__5E2d5Bh3tXjpAOoBDLN_FUmhYOOuo4wJ9ak8ll-g7EfVwJ9Gfs1bR8U1cvBVy0-6aQAmTTVK7kf56iF_wAaO7Tp_WlOzVFj9IVIUv7DvhX9KPDl3JBjnMD9O4gySMZKGkZHJ_gqQtgjPz7XYMk0CSRMTyMc3ili4iXnQsCUMA53UadQ_Rem0-ZgNbYpJBJdm66Rt7GhX8o4QWp1fQ1ZW0hVjHSMjJqzy-5PTiwTEkpUcwdgeHIECqgK7C0oBgLSOHVWHgitB_o9momshwfxBanoO7xkF5lPOrDCAyAobLX-hR-s238Oa0XHEPZP5T1MMdg6Gs0jUgEtLiMUPF-gu2q9QkwEbh9Wrrz9WxnZdUwuqTmGU2Sn7wpgfwuH7RJDo1Xn5iiC0nFpNvt3uDtlK_Yw3DYnhDuhzd1-y71NI6UiZBIYvx2JmUZ1PSBQdAo0d53sY1kolqFckVRoMwKvBSMuhZdkgDxVF7NwJVVxPFhZL9zwYsbmHd-R7IxUmQlKKmO0MWsn3",
		"OSID":"g.a000gQimVXRiO29aP4uNI90Hb-L_r7Umosdy2VhCUrejYMjCq67ObmI7Vbo9LGOBC1PWTmFvJQACgYKAf0SAQASFQHGX2MieIxZe65negwacLSyFB6nERoVAUF8yKogCRVNp4xtUxpYUnNjmJzf0076",
		"SAPISID":"SAPISID",
		"SEARCH_SAMESITE":"CgQIy5oB",
		"SID":"g.a000lAimVdYFeeEowSBrNRE1eejNm1GwRWfQMKltl6e4H7ydosrk4dv0P_jxOO9xPouuh_fspwACgYKAWgSARESFQHGX2Mil0hnCMDtxg3r2VotN3kvvBoVAUF8yKpu1J71SW2IZoYCELtQm_V60076",
		"SIDCC":"AKEyXzXJzh9k732p12uD5lQYwrqv9CUwRpUAYYF5gKNrHeNhNnNl-5KXh72x2IGqGtQYhhxrM7I",
		"SSID":"AaKhRtTK8La-AGJVF",
		"__Secure-1PAPISID":"TqUlNBySdVnw27az/A17YUa39ImUc3sKZm",
		"__Secure-1PSID":"g.a000lAimVdYFeeEowSBrNRE1eejNm1GwRWfQMKltl6e4H7ydosrk9Qc3Q7Udr_HFxyXD8rQpKAACgYKAVkSARESFQHGX2MipYrvMFqlZFAeMOBXZGnElhoVAUF8yKrntQY0gHIdcm6h9j9sf_wq0076",
		"__Secure-1PSIDCC":"AKEyXzVQ-qCpdHN0UuwmC8Z_HfDy97bxsNsbsuHJjLEzcMoOsvXiskV1N4lFIpDI4lrQIR2Uur4",
		"__Secure-1PSIDTS":"sidts-CjIB3EgAEjOIfFEaTj_8K_nGosatZ1J5X9VEn-Y_nn4WiCrTHOfBA33TUBPVZyaeTzydjBAA",
		"__Secure-3PAPISID":"TqUlNBySdVnw27az/A17YUa39ImUc3sKZm",
		"__Secure-3PSID":"g.a000lAimVdYFeeEowSBrNRE1eejNm1GwRWfQMKltl6e4H7ydosrkrggLb-5R_4fdbeWHTyWX3wACgYKAZUSARESFQHGX2MiDi_5HAJWYISp9hAFLzrqsBoVAUF8yKp02yVgdYAGHfU0Tc-5gZ_u0076",
		"__Secure-3PSIDCC":"AKEyXzUGmEqw3ka9QAgYzuVyEERZKhV3-AYMe0phBF2Sy02bpJBxR3VM1MB0PnrfzWoz4y4GxQ",
		"__Secure-3PSIDTS":"sidts-CjIB3EgAEjOIfFEaTj_8K_nGosatZ1J5X9VEn-Y_nn4WiCrTHOfBA33TUBPVZyaeTzydjBAA",
		"__Secure-OSID":"g.a000gQimVXRiO29aP4uNI90Hb-L_r7Umosdy2VhCUrejYMjCq67OyoT5CWNh5Fj-QpYZ38hyxgACgYKARoSAQASFQHGX2MiDAAosHP6P2aM3uS-PGWCKRoVAUF8yKoaMWQw9w_0eyVkqdqrhaCJ0076",
		"_ga":"GA1.1.1761629692.1707431141",
		"_ga_6VGGZHMLM2":"GS1.1.1707431141.1.0.1707431141.0.0.0",
		}

		self.HeardersW = {"UserAgent":self.HeaderW[random.randint(0,3)],"'referer'":"'https://www.google.com/'"}

	def ScannerOnlyWebsite(self):
		BanerScan()
		print("\033[1;31m[!]\033[m \033[m Tentando me conectar ao site...\033[m")
		sleep(1)
		""" MÉTODO PARA SE CONECTAR AO SITE E RETORNAR OS LINKS """

		try:
			self.ConnectWebSites = self.Connect.get(self.WebSite,headers=self.HeardersW,proxies=self.Proxies3)
		except requests.exceptions.SSLError:
			print("\033[1;31m[!]\033[m \033[m Site com problemas de conexão SSL!\033[m")
			print("\033[1;31m[!]\033[m \033[m Tentando novamente...\033[m")
			sleep(1)
		except requests.exceptions.ConnectionError:
			print("\033[1;31m[!]\033[m \033[m Site com problemas de conexão!\033[m")
			print("\033[1;31m[!]\033[m \033[m Tentando novamente...\033[m")
			sleep(1)
		else:
			if self.ConnectWebSites.status_code == 200:
				BanerScan()
				print("\033[1;33m[*]\033[m\033[m\033[1m Varredura iniciada no site \033[1;36m{}\033[m\033[1m:\033[m\n".format(self.WebSite))
				sleep(2)
				self.ContentSite = bs4.BeautifulSoup(self.ConnectWebSites.text, "html.parser")
				self.ArmazenarContent = self.ContentSite.find_all("a",href=True)
				for BuscaLinksOnSites in self.ArmazenarContent:
					if "javascript" not in BuscaLinksOnSites["href"]:
						if BuscaLinksOnSites["href"].endswith(".php"):
							if BuscaLinksOnSites["href"] not in self.LinksFinalsPHP:
								self.LinksFinalsPHP.append(self.WebSite+str(BuscaLinksOnSites["href"]))
								print("\033[1;32m[{}]\033[m \033[1;32m[FOUND]\033[m \033[1mLinks dentro do Site: \033[m\033[1;4m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),self.WebSite+BuscaLinksOnSites["href"]))
								self.SCANEAR = True
				if self.SCANEAR == True:
					print("\n\033[1;32m[{}]\033[m \033[1;33m[*]\033[m \033[1mVerificando sublinks nos links encontrandos\033[m".format(datetime.datetime.now().strftime("%H:%M:%S")))
					sleep(1)
					print("\033[1;32m[{}]\033[m \033[1;33m[*]\033[m \033[1mBuscando por falhas...\033[m\n".format(datetime.datetime.now().strftime("%H:%M:%S")))

					self.MORE = False
					if len(self.LinksFinalsPHP) > 0:

						for GETMORELINKSPHP in self.LinksFinalsPHP:
							try:
								self.GetConnectWeb1 = self.Connect.get(GETMORELINKSPHP,headers=self.HeardersW,verify=True,proxies=self.Proxies2)
							except requests.exceptions.SSLError:
								print("\033[1;31m[!]\033[m \033[m Site com problemas de conexão SSL!\033[m")
							except requests.exceptions.ConnectionError:
								print("\033[1;31m[!]\033[m \033[m Site com problemas de conexão!\033[m")
							else:
								if self.GetConnectWeb1.status_code == 200:
									self.GetMoreLinksSameWebSite = bs4.BeautifulSoup(self.GetConnectWeb1.text, "html.parser")
									self.GetMoreLinksSame = self.GetMoreLinksSameWebSite.find_all("a",href=True)
									for AditionalLinks in self.GetMoreLinksSame:
										if "id=" in AditionalLinks["href"].lower():
											if AditionalLinks["href"] not in self.LinksFinalsTests:
												self.LinksFinalsTests.append(self.WebSite+(str(AditionalLinks["href"])))
												self.MORE = True
											else:
												pass
										elif "cat=" in AditionalLinks["href"].lower():
											if AditionalLinks["href"] not in self.LinksFinalsTests:
												self.LinksFinalsTests.append(self.WebSite+(str(AditionalLinks["href"])))
												self.MORE = True
											else:
												pass
										elif "artist=" in AditionalLinks["href"].lower():
											if AditionalLinks["href"] not in self.LinksFinalsTests:
												self.LinksFinalsTests.append(self.WebSite+(str(AditionalLinks["href"])))
												self.MORE = True
											else:
												pass
										elif "itemid=" in AditionalLinks["href"].lower():
											if AditionalLinks["href"] not in self.LinksFinalsTests:
												self.LinksFinalsTests.append(self.WebSite+(str(AditionalLinks["href"])))
												self.MORE = True
											else:
												pass
										elif "intprod=" in AditionalLinks["href"].lower():
											if AditionalLinks["href"] not in self.LinksFinalsTests:
												self.LinksFinalsTests.append(self.WebSite+(str(AditionalLinks["href"])))
												self.MORE = True
											else:
												pass
										elif "order_id=" in AditionalLinks["href"].lower():
											if AditionalLinks["href"] not in self.LinksFinalsTests:
												self.LinksFinalsTests.append(self.WebSite+(str(AditionalLinks["href"])))
												self.MORE = True
											else:
												pass
										elif "intcatalogid=" in AditionalLinks["href"].lower():
											if AditionalLinks["href"] not in self.LinksFinalsTests:
												self.LinksFinalsTests.append(self.WebSite+(str(AditionalLinks["href"])))
												self.MORE = True
											else:
												pass
										elif "item_id=" in AditionalLinks["href"].lower():
											if AditionalLinks["href"] not in self.LinksFinalsTests:
												self.LinksFinalsTests.append(self.WebSite+(str(AditionalLinks["href"])))
												self.MORE = True
											else:
												pass
										elif "catid=" in AditionalLinks["href"].lower():
											if AditionalLinks["href"] not in self.LinksFinalsTests:
												self.LinksFinalsTests.append(self.WebSite+(str(AditionalLinks["href"])))
												self.MORE = True
											else:
												pass
										elif "service_id=" in AditionalLinks["href"].lower():
											if AditionalLinks["href"] not in self.LinksFinalsTests:
												self.LinksFinalsTests.append(self.WebSite+(str(AditionalLinks["href"])))
												self.MORE = True
											else:
												pass
										elif "storeid=" in AditionalLinks["href"].lower():
											if AditionalLinks["href"] not in self.LinksFinalsTests:
												self.LinksFinalsTests.append(self.WebSite+(str(AditionalLinks["href"])))
												self.MORE = True
					if self.MORE == True:
						newtestes = []
						for p in self.LinksFinalsTests:
							validandotudo = re.search(r"^(http://|https://){1}(.)+(id\=[0-9]+|cat\=[0-9]+|catid\=[0-9]+|itemid\=[0-9]+|order_id\=[0-9]+|item_id\=[0-9]+|artist\=[0-9]+)$",p,flags=re.IGNORECASE)
							if validandotudo:
								if "aspx" not in p:
									if p in newtestes:
										pass
									else:
										newtestes.append(p)
						BanerScan()
						print("\033[1;32m[*]\033[m \033[1m Iniciando o scaner...\033[m\n")
						sleep(1.1)
						for getLINK in newtestes:
							try:
								self.CONECTANDOSITESUB = self.Connect.get(getLINK+"'",headers=self.HeardersW,verify=True,cookies=self.CookieJs,proxies=self.Proxies1)
							except requests.exceptions.SSLError:
								print("\033[1;31m[!]\033[m \033[m Site com problemas de conexão SSL!\033[m")
							except requests.exceptions.ConnectionError:
								print("\033[1;31m[!]\033[m \033[m Site com problemas de conexão!\033[m")
							else:
								if self.CONECTANDOSITESUB.status_code == 200:
									self.CONTEUDOPARAANALISAR = bs4.BeautifulSoup(self.CONECTANDOSITESUB.text, "html.parser")
									self.RESULTADOWEBSITES = self.CONTEUDOPARAANALISAR.get_text()
									for ERROSQLi in self.ErrorsSQLi:
										if ERROSQLi in self.RESULTADOWEBSITES:
											print("\033[1;33m[{}] \033[m\033[1;33mPágina:\033[m \033[1;36m{}\033[m \033[1m| Status:\033[m \033[1;;4;32mVulnerável!\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),getLINK))
											with open("OnlyScan.txt","a") as insereErros:
												insereErros.write("-----------------------------------------------------------\n")
												insereErros.write("Site: {}\n".format(self.WebSite))
												insereErros.write("Página vulnerável a SQLinjection: {}\n".format(getLINK))
												insereErros.write("Hórario consulta: {}\n".format(datetime.datetime.now().strftime("%H:%M:%S")))
												insereErros.write("-----------------------------------------------------------\n")
												insereErros.close()
											break
										else:
											print("\033[1;33m[{}] \033[m\033[1;33mPágina:\033[m \033[1;36m{}\033[m \033[1m| Status:\033[m \033[1;4;31mNão vulnerável\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),getLINK))
											sleep(0.8)
						print("\n{}\033[1;32m[+]\033[m \033[1m Retornando para a home...\033[m")
						sleep(1)

					elif len(self.LinksFinalsPHP) == None:
						print("\n{}\033[1;31m[!]\033[m \033[1m Nenhuma url com paramentros para testes encontrado ...\033[m")
						sleep(2)
				else:
					print("\n\033[1;32m[{}]\033[m \033[1;31m[!]\033[m\033[1m Não encontrei Sublinks para escanear!\033[m".format(datetime.datetime.now().strftime("%H:%M:%S")))
					sleep(3)
			else:
				print("\033[1;31m[!]\033[m \033[1;33mNão foi possível estabelecer uma conexão com o site:\033[m \033[1;4m{}\033[m".format(self.WebSite))
				print("\033[1;31m[!]\033[m \033[1;33mE por isso não foi possível localizar sublinks!\033[m")
				print("\033[1;31m[!]\033[m \033[1;33mVoltando ao menu...\n")
				sleep(3)

if __name__ == "__main__":

	while True:
		ListaVulnerabilidades = ["SQL","XSS","PHP","FTP","UPLOADARQUIVO"]
		BanerScan()
		print("""
\033[1;33m[1]\033[m\033[1m - Scan de vulnerabilidades\033[m
\033[1;33m[2]\033[m\033[1m - Escanear um site\033[m
\033[1;33m[3]\033[m\033[1m - Ver Lista de vulnerabilidades\033[m
\033[1;33m[4]\033[m\033[1m - Abrir Sites Vulneráveis da opção 1\033[m
\033[1;33m[5]\033[m\033[1m - Abrir Sites Vulneráveis da opção 2\033[m
\033[1;33m[X]\033[m\033[1m - Sair\033[m

			""")

		ChoiceUser = str(input("\033[1;31mset\033[m\033[1m-> \033[m")).strip().lower()
		if ChoiceUser == "1":
			BanerScan()
			Vulnerabilidade = str(input("\033[1;32m[+]\033[m\033[1m Escolha a vulnerabilidade: > \033[m")).upper().strip()
			while Vulnerabilidade not in ListaVulnerabilidades:
				Vulnerabilidade = str(input("\033[1;32m[+]\033[m\033[1m Escolha a vulnerabilidade: > \033[m")).upper().strip()
			if Vulnerabilidade == "SQL":
				DorkUsers = str(input("\033[1;32m[+]\033[m\033[1m Insira sua Dork: > \033[m")).strip()
				while DorkUsers == "":
					DorkUsers = str(input("\033[1;31m[+]\033[m\033[1m Insira sua Dork: > \033[m")).strip()
				IniciarVarredura = GetDadosUsuario(option="-d",wordlist=False,dork=DorkUsers)
				IniciarVarredura.FiltrarURL()
				IniciarVarredura.GetPagesSearch()
				IniciarVarredura.FilterURLForOnline()
				IniciarVarredura.ExploreSQL()
				BanerScan()
			elif Vulnerabilidade == "XSS":
				BanerScan()
				print("\033[1;31m[!]\033[m\033[1m Vulnerabilidade não configurada! Voltando... \033[m")
				sleep(2)
			elif Vulnerabilidade == "PHP":
				BanerScan()
				print("\033[1;31m[!]\033[m\033[1m Vulnerabilidade não configurada! Voltando... \033[m")
				sleep(2)
			elif Vulnerabilidade == "FTP":
				BanerScan()
				print("\033[1;31m[!]\033[m\033[1m Vulnerabilidade não configurada! Voltando... \033[m")
				sleep(2)
			elif Vulnerabilidade == "UPLOADARQUIVO":
				BanerScan()
				print("\033[1;31m[!]\033[m\033[1m Vulnerabilidade não configurada! Voltando... \033[m")
				sleep(2)
			else:
				BanerScan()
				print("\033[1;31m[!]\033[m\033[1m Escolha uma opção válida!\033[m")
				sleep(2)
		elif ChoiceUser == "2":
			BanerScan()
			print("\033[1;36m[*]\033[m \033[m\033[1m exemplo de url: https://example.com/ (www and .br-> opcional) \033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),))
			print("\033[1;36m[*]\033[m \033[m\033[1m Escaneamento completo de site único!\033[m\n".format(datetime.datetime.now().strftime("%H:%M:%S"),))
			UrlSiteUser = str(input("\033[1;31mUrl> \033[m")).strip()
			ValidarUrls = re.search(r"^(http://|https://){1}(www\.)?([a-zA-Z0-9\-\_])+.+(\.com/|\.br/|\.ch/|\.edu/|\.su/|\.org/|\.sp/\.mg/\.gov/)$",str(UrlSiteUser),flags=re.IGNORECASE)
			while not ValidarUrls:
				print("\033[1;31m[!]\033[m\033[1m Insira um link válido!\033[m")
				UrlSiteUser = str(input("\033[1;32m[+]\033[m \033[1m Url: \033[m")).strip()
				ValidarUrls = re.search(r"^(http://|https://){1}(www\.)?([a-zA-Z0-9\-\_])+.+(\.com/|\.br/|\.ch/|\.edu/|\.su/|\.org/|\.sp/\.mg/\.gov/)$",str(UrlSiteUser),flags=re.IGNORECASE)
			if ValidarUrls:
				EscanearWebSites = ScannerOnlyWebSite(website=UrlSiteUser)
				EscanearWebSites.ScannerOnlyWebsite()
				BanerScan()
		elif ChoiceUser == "3":
			BanerScan()
			print("\033[1;31m[*]\033[m\033[1m VULNERABILIDADES QUE O SCRIPT IRÁ EXPLORAR:\033[m")
			print("""
\033[1m[ VERDE JÁ FOI IMPLEMENTADO ]\033[m

\033[1;32m[*]\033[m\033[1m - SQL\033[m
\033[1;31m[*]\033[m\033[1m - XSS\033[m
\033[1;31m[*]\033[m\033[1m - PHP\033[m
\033[1;31m[*]\033[m\033[1m - UPLOAD ARQUIVOS\033[m
\033[1;31m[*]\033[m\033[1m - COOKIES\033[m
				""")
			input("\033[1;31m[*]\033[m\033[1m ENTER PARA VOLTAR AO MENU: \033[m")
		elif ChoiceUser == "4":
			BanerScan()
			print("\n\033[1;31m[*]\033[m\033[1m SITES ESCANEADOS E VULNERÁVEIS A SQL INJECTION:\n\033[m")
			caminho = os.getcwd()
			find = False
			for files in os.listdir(str(caminho)):
				if files == "Vulners.txt":
					with open("Vulners.txt","r") as SQLreader:
						for VULN in SQLreader:
							print(VULN.replace("\n",""))
						find = True
						input("\033[1;31m[*]\033[m\033[1m ENTER PARA VOLTAR AO MENU: \033[m")
						SQLreader.close()
					break
			if find == False:
				input("\n\033[1;31m[*]\033[m\033[1m Você não tem sites vulneráveis ainda! ENTER PARA VOLTAR AO MENU: \033[m")

		elif ChoiceUser == "5":
			BanerScan()
			finder = False
			print("\n\033[1;31m[*]\033[m\033[1m SITES ESCANEADOS:\n\033[m")
			caminho2 = os.getcwd()
			for arq in os.listdir(str(caminho2)):
				if arq == "OnlyScan.txt":
					with open("OnlyScan.txt","r") as ScanReader:
						for St in ScanReader:
							print(St.replace("\n",""))
						finder = True
						ScanReader.close()
			if finder == False:
				input("\n\033[1;31m[*]\033[m\033[1m Você não tem sites vulneráveis ainda! ENTER PARA VOLTAR AO MENU: \033[m")

		elif ChoiceUser == "x":
			BanerScan()
			print("\n\033[1;31m[*]\033[m\033[1m Saindo...\033[m")
			sys.exit()
#.
