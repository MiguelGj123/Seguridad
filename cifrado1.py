# cifrado_examen.py
# Criptoanálisis por frecuencias (castellano) — ESQUELETO DE EXAMEN
# Basado en la tabla de frecuencias que se da en clase.

from collections import Counter
import unicodedata

# === 1) Pega aquí el TEXTO CIFRADO tal cual (no lo toques) ===
TEXTO_CIFRADO = r"""
RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
HKCZJOI OKEJSZCNHE
"""

# === 2) Tabla de frecuencias del castellano (la de la práctica) ===
# Ordenada de mayor a menor según la tabla que te van a dar.
FRECUENCIAS_CASTELLANO = [
    ("E", 16.78), ("A", 11.96), ("O", 8.69), ("L", 8.37), ("S", 7.88),
    ("N", 7.01), ("D", 6.87), ("R", 4.94), ("U", 4.80), ("I", 4.15),
    ("T", 3.31), ("C", 2.92), ("P", 2.776), ("M", 2.12), ("Y", 1.54),
    ("Q", 1.53), ("B", 0.92), ("H", 0.89), ("G", 0.73), ("F", 0.52),
    ("V", 0.39), ("J", 0.30), ("Ñ", 0.29), ("Z", 0.15), ("X", 0.06),
    ("K", 0.00), ("W", 0.00)
]

# Solo letras, para el mapeo
LETRAS_POR_FRECUENCIA = [l for l, _ in FRECUENCIAS_CASTELLANO]

# === 3) Ajustes manuales (vacío al principio, en examen lo rellenas) ===
ajustes_manuales = {
    # Ejemplo:
    # 'A': 'D',
    # 'X': 'E',
    "N": 's',
    "T": 'l'

}

# --------------------------------------------------------------
# Funciones de utilidad
# --------------------------------------------------------------

def quitar_acentos(s: str) -> str:
    norm = unicodedata.normalize('NFD', s)
    return "".join(ch for ch in norm if unicodedata.category(ch) != 'Mn')

def solo_letras(s: str) -> str:
    return "".join(ch for ch in s if ch.isalpha())

def normalizar_para_frecuencias(s: str) -> str:
    s = quitar_acentos(s)
    return s.upper()

def contar_frecuencias_letras(texto: str) -> Counter:
    t = normalizar_para_frecuencias(solo_letras(texto))
    return Counter(t)

def aplicar_sustitucion(texto: str, mapa: dict) -> str:
    res = []
    for ch in texto:
        if ch.isalpha():
            res.append(mapa.get(ch.upper(), "_"))  # "_" si no definido
        else:
            res.append(ch)
    return "".join(res)

# --------------------------------------------------------------
# Programa principal
# --------------------------------------------------------------

def main():
    # 1) Contar frecuencias en el texto cifrado
    freq_letras = contar_frecuencias_letras(TEXTO_CIFRADO)
    total = sum(freq_letras.values())

    print("=== Frecuencias de letras en el texto cifrado ===")
    for letra, cnt in freq_letras.most_common():
        print(f"{letra}: {cnt} ({cnt/total*100:.2f}%)")
    print()

    # 2) Construir mapeo automático por frecuencias
    cifradas_ordenadas = [l for l, _ in freq_letras.most_common()]
    mapeo_auto = {}
    for i, letra_cifrada in enumerate(cifradas_ordenadas):
        if i < len(LETRAS_POR_FRECUENCIA):
            mapeo_auto[letra_cifrada] = LETRAS_POR_FRECUENCIA[i]

    # 3) Aplicar tus ajustes manuales (sobrescriben el automático)
    mapeo_final = mapeo_auto.copy()
    for k, v in ajustes_manuales.items():
        mapeo_final[k.upper()] = v.upper()

    # 4) Mostrar mapeo propuesto
    print("=== Mapeo inicial (cifrada -> clara) ===")
    for c, claro in mapeo_final.items():
        print(f"{c} -> {claro}")
    print()

    # 5) Mostrar texto sustituto
    print("=== Texto con sustitución automática + ajustes ===")
    print(aplicar_sustitucion(TEXTO_CIFRADO, mapeo_final))

if __name__ == "__main__":
    main()
