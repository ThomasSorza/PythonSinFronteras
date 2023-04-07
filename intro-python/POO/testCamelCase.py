from camelcase import CamelCase #imported module form python (needs to install using pip)

cc = CamelCase()
s = 'This sentence needs camel case'
sc = cc.hump(s)
print(sc)