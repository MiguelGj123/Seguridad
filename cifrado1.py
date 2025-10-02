from collections import Counter

# Texto cifrado
texto_cifrado = """
RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE 
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.

AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ 
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX 
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, 
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN 
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, 
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK 
HKCZJOI OKEJSZCNHE.
"""

# Quitar saltos de línea y dejar solo letras
solo_letras = "".join(c for c in texto_cifrado.upper() if c.isalpha())
contador = Counter(solo_letras)
total = sum(contador.values())

print("=== Frecuencias en el texto cifrado ===")
for letra, freq in contador.most_common():
    print(f"{letra}: {freq} ({freq/total:.2%})")

# Diccionario con algunas sustituciones iniciales

sustitucion = {
    # “AZKKZHC” → “DURRUTI”
    'A': 'd', 'Z': 'u', 'K': 'r', 'H': 't', 'C': 'i',
    # “AX” → “de”
    'X': 'e',
    # “JIvCXPQKX” → “NOVIEMBRE”  (ojo: la v se convierte en V con .upper())
    'J': 'n',
    'I': 'o',
    'V': 'y',
    'P': 'm',
    'Q': 'b',
    # “RIJ” → “CON”
    'R': 'c',
    'E': 'a',
    'D': 'p',
    'N': 's',
    'U': 'g',
    'S': 'q',
    'G': 'j',
    'T': 'l',
    'O': 'f',
    'F': 'x',
    'M': 'h',
    'L': 'z'
   }

def aplicar_sustitucion(texto, mapa):
    resultado = ""
    for c in texto:
        if c.isalpha():
            resultado += mapa.get(c, "_")  # "_" si no lo tenemos aún
        else:
            resultado += c
    return resultado

print("\n=== Texto con sustitución actual ===")
print(aplicar_sustitucion(texto_cifrado.upper(), sustitucion))

