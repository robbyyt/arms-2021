import json
import bbc
import cnn
import guardian
import reporteris
import hotnews
import BBClinks as bbc_l
import ECONlinks as ecn_l
import ALJlinks as alj_l
import MFaxlinks as mf_l
import NWSRlinks as nws_l
import Libertatealinks as lbr_l
import HOTNWSlinks as hot_l
import RISlinks as ris_l
import TV5Mlinks as tv5_l
import TGDNlinks as tgdn_l
#bbc_links = bbc_l.get_bbcLinks()
#ecn_links = ecn_l.get_ecnLinks()
#alj_links = alj_l.get_aljLinks()
#mf_links = mf_l.get_mfLinks()
#nws_links = nws_l.get_nwsLinks()
#lbr_links = lbr_l.get_lbrLinks()
hot_links = hot_l.get_hotnwsLinks()
ris_links = ris_l.get_risLinks()
gdn_links = tgdn_l.get_gdnLinks()
cnn_links = ['https://edition.cnn.com/2021/03/10/us/derek-chauvin-trial-jurors/index.html','https://edition.cnn.com/2021/03/19/us/pew-research-data-race-discrimination-trnd/index.html','https://edition.cnn.com/2021/03/14/us/minneapolis-george-floyd-square-battleground-soh/index.html','https://edition.cnn.com/2021/03/12/us/george-floyd-minneapolis-settlement/index.html','https://edition.cnn.com/2021/03/11/us/derek-chauvin-george-floyd-charges/index.html','https://edition.cnn.com/2021/03/08/us/derek-chauvin-trial-jury/index.html','https://edition.cnn.com/videos/justice/2021/03/11/derek-chauvin-third-degree-charge-honig-nr-vpx.cnn','https://edition.cnn.com/2021/03/08/us/race-relations-george-floyd-poll/index.html']
tv5_links = ['https://information.tv5monde.com/video/etats-unis-la-famille-de-george-floyd-recoit-27-millions-de-dollars-de-dedommagement','https://information.tv5monde.com/video/qui-etait-george-floyd-cet-homme-devenu-un-symbole-des-violences-policieres','https://information.tv5monde.com/info/france-les-violences-policieres-en-debat-du-deni-la-crise-385468','https://information.tv5monde.com/video/etats-unis-derek-chauvin-le-policier-accuse-d-avoir-tue-george-floyd-libere-sous-caution','https://information.tv5monde.com/video/en-afrique-les-reactions-la-mort-de-george-floyd','https://information.tv5monde.com/info/george-floyd-le-destin-tragique-d-un-homme-devenu-l-incarnation-de-la-lutte-antiraciste-399404','https://information.tv5monde.com/video/mort-de-george-floyd-et-hardel-sherrell-aux-etats-unis-minneapolis-la-colere-ne-retombe-pas','https://information.tv5monde.com/info/le-jury-quasi-constitue-au-proces-du-meurtre-de-george-floyd-401551','https://information.tv5monde.com/video/etats-unis-comment-reconstruire-un-monde-plus-juste-apres-la-mort-de-george-floyd','https://information.tv5monde.com/video/george-floyd-symbole-mondial-du-racisme-et-des-violences-policieres','https://information.tv5monde.com/video/mort-de-george-floyd-symboles-et-monuments-en-ligne-de-mire','https://information.tv5monde.com/video/mort-de-george-floyd-heurts-et-feux-devant-la-maison-blanche','https://information.tv5monde.com/video/mort-de-george-floyd-aux-etats-unis-les-transformations-pour-mettre-fin-au-racisme-seront']
bbc_json = []
enc_json = []
alj_json = []
mf_json = []
nws_json = []
lbr_json = []
hot_json = []
ris_json = []
gdn_json = []
cnn_json = []
tv5_json = []
for i in gdn_links:
        article=guardian.Guardian(i)
        gdn_json.append(article.to_object())

print(ris_links)
"""
for i in cnn_links:
        article=cnn.CNN(i)
        cnn_json.append(article.to_object())
print(gdn_links)

for i in ris_links:
        article=reporteris.Reporteris(i)
        ris_json.append(article.to_object())

for i in hot_links:
        article=hotnews.Newsro(i)
        hot_json.append(article.to_object())
obj = open('cnn.json', 'w')

for j in range(len(cnn_json)):
        json_object = json.dumps(cnn_json[j], indent=4)
        obj.write(json_object)
obj.close()
print("CNN done..")
"""
"""
for j in range(len(gdn_json)):
        json_object = json.dumps(gdn_json[j], indent=4)
        obj.write(json_object)

for j in range(len(ris_json)):
        json_object = json.dumps(ris_json[j], indent=4)
        obj.write(json_object)

obj = open('hotnews.json', 'w')
for j in range(len(hot_json)):
        json_object = json.dumps(hot_json[j], indent=4)
        obj.write(json_object)
obj.close()
"""
print("HOTNEWS done..")

