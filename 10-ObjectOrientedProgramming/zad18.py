import contacts
import koneksje

puu=koneksje.koneksjelista()
puu.add_new(contacts.Contact('John Brown','brown@onet.pl',555234000))
puu.add_new(contacts.Contact('Anna May','am@o2.pl',232000199))
puu.add_new(contacts.Contact('George Small','smallg@google.pl',222999100))
puu.add_new(contacts.Contact('Paopla Big','bigpaola@poczta.pl',100200300))
puu.disp()