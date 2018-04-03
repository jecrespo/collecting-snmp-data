# --------------------------------------------------------------------------- # 
# PySNMP is a cross-platform, pure-Python SNMP engine implementation
# Instalación: pip install pysnmp
# Documentación librería pysnmp: http://pysnmp.sourceforge.net/
# --------------------------------------------------------------------------- # 

from pysnmp.hlapi import *

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in nextCmd(SnmpEngine(),
                          CommunityData('public'),
                          UdpTransportTarget(('192.168.1.100', 161)),
                          ContextData(),
                          ObjectType(ObjectIdentity('.1.3.6.1')),
                          lookupMib=False):

    if errorIndication:
        print(errorIndication)
        break
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))

# Obtener datos consumo por fase mediante SNMP
g = getCmd(SnmpEngine(), CommunityData('public'),UdpTransportTarget(('192.168.1.100', 161)), ContextData(),
	ObjectType(ObjectIdentity('.1.3.6.1.2.1.33.1.4.4.1.4.1')),
    ObjectType(ObjectIdentity('.1.3.6.1.2.1.33.1.4.4.1.4.2')),
    ObjectType(ObjectIdentity('.1.3.6.1.2.1.33.1.4.4.1.4.3')))
errorIndication, errorStatus, errorIndex, varBinds = next(g)

Total_Power = 0 # Dato consumo en trifasica

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
        Total_Power = Total_Power + (int(varBind[1]. prettyPrint()))/1000